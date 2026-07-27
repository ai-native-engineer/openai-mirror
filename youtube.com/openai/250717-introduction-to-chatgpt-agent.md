---
title: "Introduction to ChatGPT agent"
channel: openai
url: https://www.youtube.com/watch?v=1jn_RpbPbEc
youtube_id: 1jn_RpbPbEc
published: 2025-07-17
duration: "25:30"
captions: en-orig
---

# Introduction to ChatGPT agent

[![Introduction to ChatGPT agent](https://img.youtube.com/vi/1jn_RpbPbEc/hqdefault.jpg)](https://www.youtube.com/watch?v=1jn_RpbPbEc)

<details>
<summary>자막: Introduction to ChatGPT agent (25:30)</summary>

[00:00]
[Music]
Good morning. We have a banger for you
today. We're going to launch chatbt
agent. But before jumping into that, I'd
like to ask the team to introduce
themselves. Starting with Yosh.
>> Hi, I'm Yash. I work on agent team and
before that I used to work on operator.
>> Hi, I'm Jing. I work on agents research
previously on deep research.
>> Hi, I'm Casey. I'm a researcher on
agents formerly operator.
>> Hi, I'm Issa. I'm a researcher on agent
formerly on deep research.
>> So we we started launching agents
earlier this year. Uh we launched deep
research, we launched operator and
people were very excited about this.
People could see that now uh AI was
going off to do complex tasks for them.
But it became clear to us that what
people really wanted was for us to bring
those capabilities and more together.
People wanted a unified agent that could
go off, use its own computer and do real
complex tasks for them, that could uh
seamlessly transition from thinking
about something to taking actions to

[00:01]
using lots of tools using the terminal,
clicking around the web, even producing
things like spreadsheets and slides and
and much more. And wanted people want to
be able to do this over a long time
horizon and a sort of for universal
tasks. So the team has been working
super hard to bring that together. And
today we have chat with the agent. Um,
it's probably easier to show it to you
than to keep talking about it. It is one
of the feel the aon moments for me to
watch it work. So, let's take a look.
Awesome. Thanks, Sam. Hello, everyone.
Very excited to share chat GBD agent
with everybody. And as Sam said, let's
just dive right into the demo. Okay, so
we are on Chad GBD as we all know and
love. And to turn on the agent mode, you
just click the tools menu and select
agent. You can also just type agent in
the composer bar and it'll take you to
agent mode. Um, Edward and I have a
wedding to go to later this year. Uh,
it's for one of our mutual friends.
Should we should we have the Asian
planet?
>> Yeah, let's do it. I need an outfit. And
don't forget the gift.
>> Okay, great. We won't forget the gift.
Um, it's a little bit of a longer

[00:02]
prompt, so I have it copied in my
buffer, so I'm just going to go ahead
and paste it. Um, okay. So, let's see.
Let's see what it says. Our friends are
getting married later this year, as I
said, Minia and Sarah. And we want the
agent to help us find an outfit that
matches the dress code. uh propose a few
options. Nice mid luxury taking into
account venue and weather. We also want
to find us some hotels and as Edward
said, don't forget the gift. Um so let's
see and
send the prompt away. As Sam said, agent
uses a computer. Uh so in the beginning
it sets up its environment. It it you
know it'll take a minute or two or not
really 5 seconds to set up its
environment. And in this case, as you
see, it understands the prompt. It's
asking for me for a clarification. I'm
just going to let it just continue and
work. Anyway, um I think it got confused
by saying, "Oh, where's the um what
exactly is the time of the date of the
wedding?" I think it'll figure out using
the website. Okay, cool. So, now it's
kicked off. It's starting the process,

[00:03]
the prompt, and it's open up a browser.
And to walk you through what's
happening, here's
>> Yeah. So, as mentioned, we gave the
agent access to its own virtual
computer, and the computer has many
different tools installed, and it can
choose which to use as it's working
through the task. So, in chat GPT, you
can see a visualization of the agent's
computer screen, and you can see
overlaid its chain of thought in text,
and that's what it's thinking as it's
working through the task and deciding
what to do next. We gave the agent
access to two different ways to browse
the internet. First, we gave it a text
browser, and this is similar to the deep
research tool. And this is what lets it
really efficiently and quickly read many
web pages um um and search for them. And
we also gave it access to a visual
browser. And this is similar to the
operator tool. And this is what lets it
actually interact with the UI of a web
page. So it can um drag things. It can
use the cursor to click around. It can
open UI components. It can fill out
forms and enter text and text areas.
It's very flexible. So those two tools

[00:04]
are very complimentary. And then we also
gave it access to its own terminal so
that it can run code and it can also
generate and analyze files like slide
decks and spreadsheets. And then through
the terminal it's also able to call
APIs. So both public APIs and APIs to
access your private data sources like
Google Drive, Google Calendar, GitHub,
SharePoint and many others um and only
if you explicitly connect them similar
to deep research connectors. And then it
also has access to the image gen API so
it can create nice visuals for um slide
decks and other things as it's working
through its tasks.
How is deciding which tools to use here?
Yes, we train the model to move between
these capabilities with reinforcement
learning. This is the first model we
trained that has access to this unified
tool box. A text browser, a GUI browser
and a terminal all in one virtual
machine. To guide its learning, we
created hard tasks that require using
all these tools. This allows the model

[00:05]
not only to learn how to use these
tools, but also when to use which tool
depending on the task at hand. At the
beginning of the training, the model
might attempt to use all these tools to
solve a relatively simple problem. Over
time, as we reward the model for solving
problems correctly and efficiently, the
model will have smarter tool choice.
For example, if you ask a model to uh
find a restaurant with specific
requirements and make a reservation, the
model may typically just start a deep
research in the text browser to find
some candidates, then switch to the GUI
browser to view photos of food, uh check
availability, and complete the booking.
Similarly, for creative task like
creating an artifact, the model will
first search online for public
resources, then switch to the terminal
to do some code editing to compile the
artifact and finally verify the final
outputs in the GUI browser. With this,

[00:06]
we truly feel like we brought together
the best of deep research and operator
and added some extra sparkle.
That's right. Yeah. So to put this
project in context, I want to give a bit
of history. So a few months ago, we
shipped operator in January and this was
our agent that lets you do online tasks
like book reservations and um send
emails and then two weeks later we
shipped deep research and deep research
is a tool that lets you do in-depth
internet research and output highquality
um um research reports. And after launch
we realized that actually these two
approaches are actually deeply
complimentary.
Um for example operator has some trouble
reading super long articles. Um it has
to scroll. It takes a long time. But
that's something that deep research is
good at. Conversely operator uh uh deep
research isn't as good at interacting
with web pages interactive elements

[00:07]
visual uh highly visual web pages but
that's something that operator excels
at. So uh yeah we felt these approaches
were complimentary and then we we were
also looking at some customer feedback.
So for example one of our most highly
requested features for deep research was
the ability to log into websites and
access authenticated sources. That's
something that operator can do.
>> I've been waiting for that for a long
time.
>> Yeah.
Um another thing is that we were looking
at the prompts that people were trying
for operator and we saw that they were
actually more deep research type
prompts. for example, plan a trip and
then book it. And so, yeah, we we really
feel like we're bringing the best of
both worlds here. And on a personal
note, we've all been friends for a
while, and it's really exciting to be
working together. So, speaking of
matches made in heaven, how is the
wedding planning going?
>> It's amazing to watch. This is an
example of a task I hate doing. This can
like ruin like, you know, multiple hours
for me as I get sucked into these rabbit
holes. So, just watching this as you
guys have been talking click through
this and just like do the whole thing is

[00:08]
really quite remarkable. Yeah, totally.
Um, looks like it started off by
figuring out the weather. One of the
cool features, um, is that, you know, as
some of these tasks may take a little
bit longer, you can just go back and see
what it was doing. So, that's what we're
exactly going to do. Looks like it went
through the website to use the text
browser. Interestingly, for that, now
it's looking through the suits for
Edward. I think it'll find something
good. Here you can see it switched over
to actually a visual browser to make
sure suit will look really good on
Edward.
And now looks like yeah, it's got
chugging along, figuring out what to do.
Um, and still on suits and now probably
getting to the gifts section. Um, okay,
cool. So, this is going to take a while.
As Sam said, these tasks sometimes can
take a long time. So, it's going to
continue doing hopefully much faster
than we will do. Um, should we do
something else while it's doing it? I
think the team really wanted the um
stickers, some stickers for the for the
launch. Should we do that?
>> Yeah, cool.
>> All right. So, we have a team mascot,
which is one of our colleagues, Bunny

[00:09]
Doodle. really really cute tell you. Um
and we're going to try and bring um get
some laptop stickers for everybody. Uh
one of the favorite features for agent
is given that trajectories can take 15
minutes, 20 minutes, 30 minutes
depending on the complexity of the task.
Um a lot of times the you might need to
help the agent. Agent might need to ask
you clarifications, confirmations and
things like that. Um so I love to use it
on the go. So I'm going to use my mobile
phone to actually send the query this
time and then see how it goes.
Okay, so let's see. Okay, so we are on
Chad Gibbdi. Uh I have already selected
the agent mode. I've also inputed our uh
cute mascot and I'm going to quickly
paste a query. So query says make some
swag for the team one by one laptop
stickers and order 500 of them. I'll
also say I like sticker mule
which we have used in the past and send
it off.
Okay. So, just like it was doing on the

[00:10]
web, it's going to take some time, think
about like what's it doing, and it'll
kick off kick off the query. And as it's
going, it'll take some time to kick it
off. Is it Oh, there we go. So, it'll
start working on it. Looks like it's
starting to create the anime art. It'll
probably use image that Isa referred
earlier on to create hopefully an anime
art. We'll see how it comes out. While
that's going, anything else we want to
do?
>> Oh, yeah. I also need a pair of shoes
because my shoes got damaged.
>> How did they get damaged?
>> Uh, by the rain
>> in SF.
>> Yes.
>> Cool. All right. Uh, well, let's get
Edward a pair of shoes as well. So, oh,
can you also find us um pair of men's
dress black shoes in size
>> 9.5?
>> 9.5.
So, one of the key capabilities of the
model is being able to interrupt. I
think you know as trajectories take long
time or whatever time it's really
important for us to for it to feel very
multi-turn so the users can interject
user can direct it user can give it more

[00:11]
guidance less guidance whatever we want
to do and that's what we're doing here
we essentially the the model was
chugging along figuring out all the
things that we had asked before and in
this case we essentially said hey can
you also uh get us a pair of men's black
shoes and now it's thinking and soon
enough hopefully it'll take that into
account and keep going uh into its
trajectory. There we go. So, it said
acknowledge the interruption. It said,
"Okay, cool. I'll also research men's
black shoes in size 9.5." Um, and then
it'll probably get on its way. Um, but
maybe Issa can tell us a little bit more
about how that works.
>> Yeah, sure. So, as you can see, the
agent is very collaborative, and this
was really important to us when we were
training the model and building the
product. If you were asking another
person to do a task for you that would
take them a really long time to
complete, you'd probably give them some
instructions to start and then they
might ask you some clarifying questions
and then they'd start the task and maybe
realize, oh, they need more
clarification from you or they need your
permission to sign into something or do
something on your behalf and then you
might realize, oh, I forgot to mention

[00:12]
this thing or um what's your status? How
are you doing? Can I help redirect you
if you're getting along the wrong path
or something? And so similarly for these
really longrunning agentic tasks, it's
very important that both the user and
the agent are able to initiate
communication with each other so that um
the agent is able to most effectively
help you with your tasks. And so this is
something that we actually trained into
the model. We trained it to be able to
ask clarifying questions, not every
single time like deep research. Um we
also asked it we also trained it to be
interruptible as Yash just showed. And
also sometimes it will ask you for
clarification and confirmation
mid-trajectory.
>> Yeah. And part of working with agent is
that well sometimes it'll make mistakes.
And that's why we felt it was important
to train the model to ask you for
confirmation at the last step of
important steps. Um so for example maybe
before it's going to send the email um
it'll ask you to take a look at the
draft and whether it makes sense and
whether there are any embarrassing
typos. Um, and if there are, then you
can either ask it to fix it or you can

[00:13]
directly take over the browser and jump
right into the um, agents environment
and correct it yourself. And that way it
feels collaborative and you can um,
really work with the agent.
>> Should we look at maybe one more demo?
We've got this uh, sort of fun tradition
in live streams of using uh, using our
newest models to sort of evaluate
themselves or do something kind of meta.
Anything like that we could do?
>> Yeah, let's do it.
So um
>> I think people would love to know how
good the model is.
>> Yes. So this is a prompt we previously
gave the a agent yesterday. So basically
it asks the model to pull its own
evalution number from our Google job
connector and make some slides. So we
want to keep it simple like no
introduction no conclusion just present
the results with in the charts. As you
can see now the model is connecting to
the Google Drive API and uh then search
within API it right now it looks like
the first result is very relevant. So
it's reading the first result.

[00:14]
Now it's reading the first result uh in
details. Uh let's accelerate this uh
replay. So then the model might read
from the result again and write some
code.
So here you can see that the model is
using the image generation model called
image generation tool to generate some
decorations for the slides.
And let's see what's the first slide the
model made.
So here the model is writing some code
that will be compiled to be the final
slides. So this is the first slide the
model make in this demo which looks okay
but it's not polished enough.
One of the key feature in reinforcement
learning is that the model will re
review its own results and refine the
results to to deliver a good final
results. Let's see what's the finally
what the model give us.

[00:15]
We can click skip and then the model
give us a good uh PowerPoint file. So
it's a real PowerPoint that you can
download and open it in any software.
Let's open it in uh in the office. So
let's present the slides the model just
generated.
First are two intelligence benchmarks.
Humanities last exam is a benchmark that
measures AI's ability to solve a broad
range of subjects on hard problems. We
evaluate the models with two settings
with and without tool use.
We can see that the agent modes the raw
intelligence is already pretty nice and
with access to all tools nearly double
the performance to 42%.
When evaluating models on humanity's
last exam, especially with the browsing
ability, we have a two-layer

[00:16]
decontamination that ensure that the
model doesn't cheat on this benchmark.
Front TMS is a benchmark that measures
advanced mathematical reasoning ability
of models.
Different from our baseline of mini and
03 which use Python with function
coding. We give the agent model all
available tools like a browser, a
computer and a terminal. The agent
achieves new state art of 27% on this
benchmark with the help of all these
tools.
Next, we evaluated the model on two
agentic benchmarks. Web arena is a
benchmark that measures web agents
ability so to solve real world web
tasks. The agent model improves over
previous O3 model that powers the core.
Browse comp is a benchmark we introduced
earlier this year that measures the
browsing agents ability to search and
find uh how to locate information.

[00:17]
The agent model significantly
outperforms 03 and deep research on this
benchmark achieving 69% pass rate.
Finally, we care about how the users
will benefit from our model in the real
world. Spreadsheet bench is a benchmark
that measures the model's ability to
edit spreadsheets derived from the real
world use case. Here the agent model
with the liberal office and the computer
tool can already solve 30% of the task
when we give the model the access to the
raw Excel file in the terminal which
further boost the performance to 45%.
Finally we evated the model on an
internal banking benchmark. The bench
this benchmark evaluated the model's
ability to to conduct first to third
year investment bank uh banking analyst
tasks such as like putting together a
three statement financial model for

[00:18]
Fortune uh 500 company in this
benchmark. The agent model significantly
outperforms the previous deep research
and all three models. As you can see
this model is one of the most powerful
model we've ever trained.
It's not only good on benchmarks, it's
also capable of reasoning, browsing, and
tackling real world tasks at a level
that we cannot imagine three months ago.
That's right. Um, as Edward said, um, we
think we've trained a very powerful
model and a lot of the power comes from
its ability to browse the internet. And
as we know, the internet can be a scary
place. There are all sorts of hackers
trying to steal your information, scams,
uh fishing attempts. Um and agent isn't
immune to all these things. Um one
particular thing we're worried about is
a new uh attack called prompt
injections.
This is where let's say you ask agent to
buy you a book and you give it your

[00:19]
credit card information to do that.
Agent might stumble upon a malicious
website that asks it, "Oh, enter your
credit card information here. it'll help
you with your task. An agent, which is
trained to be helpful, might decide
that's a good idea.
We've done a lot of work to try to
ensure that this doesn't happen. We've
trained our model to ignore suspicious
instructions on on suspicious websites.
We've also have uh we also have layers
of monitors that kind of peer over the
agent's shoulder and watch it as it's
going um and stop the trajectory if
anything looks suspicious. We can even
update these in real time if new attacks
are found in the wild.
That said though, you know, this is a
cutting edge product. This is a new
surface and we can't stop everything.
And so that's why I feel it's very
important for the audience to be aware
of the risks involved in using agent.
And um we encourage users to be
proactive in kind of thinking about how
they share their information. You know,

[00:20]
if it's highly sensitive information,
maybe don't share that. um maybe um uh
use our features like takeover mode to
directly input your credit credit card
information into the browser instead of
um giving it to agent. Um we feel like
we've built a very powerful product but
again it's important for our users to
understand the risk involved.
>> Yeah, I really want to emphasize that I
think this is a new level of capability
in AI. It's a new way to use AI, but
there will be a new set of attacks that
come with that. And society and the
technology will have to evolve and learn
how we're going to mitigate things that
we can't even really imagine yet. Uh, as
people start doing more and more work
this way. Before I wrap up, should we
check in on some of the tasks you kicked
off?
>> Yeah, let's do it. Um, okay. So, I am
going to open a new tab and make sure
that we can see the progress of our um,
stickers as well. Okay. Let's see. All
right. So, sounds like stickers are
ready. Let me see what it actually Okay.

[00:21]
So, cool thing. This is sort of the end
end result of the took about 7 minutes.
Highly likely figured out everything.
We'll go back and look at the trajectory
and see how it did. But at the end
result, it looks like it's added to the
cart. This is the subtotal. I can just
go ahead and look at it and then figure
out uh I can just take over at this
point as Casey said to enter my credit
card information and then place the
order really quickly. model is asking
for confirmations, etc. as it's supposed
to do. Let's just quickly browse through
the trajectory and see what it actually
did. Oh, it looks like it generated some
stickers. Oh, look at that. That's what
it generated sticker. Cool. So, yeah,
that's the task. I think I can at this
point finish up by myself or I can ask
the model to actually go ahead and do it
for me as well. Let's check on the
wedding. Okay, great. Looks like it just
finished in the nick of time. Uh, okay,
cool. So in this case, as as we said, we
were looking for hotel, stress, uh
suits, and also shoes. So it's come out

[00:22]
with a pretty comprehensive report. It
looks like wedding venue, date, when it
is with the Zilla links, dress codes. It
figured out like what the suit
recommendation should be, where you can
buy. Now I can go ahead and buy myself
or I can ask the agent to go and buy for
me. Um also figured out footwear hurdle
options. It actually looked through all
the oop sorry it looked through all the
availability. You can see actually it
gives screenshots of what it checked. In
this case we use booking.com and it's
able to do that. Also has gift
suggestions etc. And next step I can ask
it as you said the agent says hey if you
need assistance purchasing any item or
have any further adjustments let me know
so we can do that. Um, and I want to
show one last demo which we didn't
really run live but I think it's really
cool and especially because the folks
who are getting married are really into
MLB. U so we asked the agent uh to go
and build an optimal itinary for
visiting all 30 MLB stadiums in just in

[00:23]
case you're thinking of a satical uh and
then design the optimal route prioritize
Hello Kitty nights and whatnot and
present a final plan as a detailed
spreadsheet. I'll really quickly run
through this. Um I think it's just so
fun to see. So again like as we have
thrown shown throughout the the live
stream it uses a multitude of tools uses
container the terminal use using the
browser working through all the details.
It'll probably use again back to the
browser figuring out Hello Kitty nights
and then sports stadium and whatnot. Oh
let's see did I miss the Oh go map.
building a map using code to actually
build it out and then overall we get
like a pretty solid result I think at
the end takes 25 minutes to work where
does the season start and what not you
have a spreadsheet that you can quickly
view inside just right inside Chad GBD
you can map the journey cool looking map
I guess and that's it so this is Chad

[00:24]
GBD agent we hope you really like it and
over to Sam
>> amazing work all of you and and to your
teams this is I think uh really
something that's going to help people
get worked done uh and have more time to
do the things they want to do. Um I
think it's it's really amazing how much
you've brought together to deliver this
experience and watching the agent sort
of use the internet, make these
spreadsheets, make PowerPoints, whatever
else uh and do all this work is is quite
amazing. We're going live today for pro
plus and team users. Pro users will get
uh 400 queries a month plus some team
users will get 40 a month. Uh the
rollout should be finished by the end of
the day for pro and very soon for plus
and team users. will try to be live for
enterprise and edu by the end of this
month. As Casey mentioned, although this
is an extremely exciting new technology,
there are new risks. Uh people learned
how to use the internet generally pretty
safely, although of course there are
still scammers and other attacks. People
are going to need to learn to use AI
agents. Uh and societyy's going to need
to learn to build up defenses against
attacks on AI agents as well. So we're

[00:25]
starting with a very robust system, lots
of warnings. We will relax that over
time as people get more comfortable with
it. But we do want people to treat this
as a new technology and a new risk
surface and use all of the caution that
Casey talked about. Um, but that said,
we hope you'll love it. Uh, this is
still very early. We will improve it
rapidly and we're excited to see where
it all goes. So, congrats again. Thank
you very much. Hope you enjoy.

</details>
