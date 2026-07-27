---
title: "OpenAI o3 and o3-mini—12 Days of OpenAI: Day 12"
channel: openai
url: https://www.youtube.com/watch?v=SKBG1sqdyIU
youtube_id: SKBG1sqdyIU
published: 2024-12-20
duration: "22:04"
captions: en-orig
---

# OpenAI o3 and o3-mini—12 Days of OpenAI: Day 12

[![OpenAI o3 and o3-mini—12 Days of OpenAI: Day 12](https://img.youtube.com/vi/SKBG1sqdyIU/hqdefault.jpg)](https://www.youtube.com/watch?v=SKBG1sqdyIU)

<details>
<summary>자막: OpenAI o3 and o3-mini—12 Days of OpenAI: Day 12 (22:04)</summary>

[00:00]
[Music]
good morning we have an exciting one for
you today we started this 12-day event
12 days ago with the launch of 01 our
first reasoning model it's been amazing
to see what people are doing with that
and very gratifying to hear how much
people like it we view this as sort of
the beginning of the next phase of AI
where you can use these models to do
increasingly complex tasks that require
a lot of reasoning and so for the last
day of this event um we thought it would
be fun to go from one Frontier Model to
our next Frontier Model today we're
going to talk about that next Frontier
Model um which you would think logically
maybe should be called O2 um but out of
respect to our friends at telica and in
the grand tradition of open AI being
really truly bad at names it's going to
be called 03 actually we're going to
launch uh not launch we're going to
announce two models today 03 and O3 mini
03 is a very very smart model uh 03 mini
is an incredibly smart model but still
uh but a really good performance and

[00:01]
cost so to get the bad news out of the
way first we're not going to publicly
launch these today um the good news is
we're going to make them available for
Public Safety testing starting today you
can apply and we'll talk about that
later we've taken safety Tes testing
seriously as our models get uh more and
more capable and at this new level of
capability we want to try adding a new
part of our safety testing procedure
which is to allow uh Public Access for
researchers that want to help us test
we'll talk more at the end about when
these models uh when we expect to make
these models models generally available
but we're so excited uh to show you what
they can do to talk about their
performance got a little surprise we'll
show you some demos uh and without
further Ado I'll hand it over to Mark to
talk about it cool thank you so much Sam
so my name is Mark I lead research at
openai and I want to talk a little bit
about O's capabilities now O is a really
strong model at very hard technical
benchmarks and I want to start with
coding benchmarks if you can bring those
up so on software style benchmarks we
have sweet bench verified which is a
benchmark consisting of real world

[00:02]
software tasks we're seeing that 03
performs at about
71.7% accuracy which is over 20% better
than our 01 models now this really
signifies that we're really climbing the
frontier of utility as well on
competition code we see that 01 achieves
an ELO on this contest coding site
called code forces about 1891 at our
most aggressive High test time compute
settings we're able to achieve almost
like a 2727 ELO here ju so Mark was a
competitive programmer actually still
coaches competitive programming very
very good what what is your I think my
best at a comparable site was about 2500
that's tough well I I will say you know
our chief scientist um this is also
better than our chief scientist yakov's
score I think there's one guy at opening
eye who's still like a 3,000 something
yeah a few more months to yeah enoy
hopefully we have a couple months to
enjoy there great that's I mean this is
it's in this model is incredible at
programming yeah and not just programing
but also mathematics

[00:03]
so we see that on competition math
benchmarks just like competitive
programming we achieve very very strong
scores so 03 gets about 96.7% accuracy
versus an 01 performance of 83.3% on the
Amy what's your best Amy score I did get
a perfect score once so I'm safe but
yeah um really what this signifies is
that 03 um often just misses one
question whenever we tested on this very
hard feeder exam for the USA
mathematical Olympian there's another
very tough Benchmark which is called gpq
Diamond and this measures the model's
performance on PhD level science
questions here we get another
state-of-the-art number
87.7% which is about 10% better than our
01 performance which was at 78% just to
put this in perspective if you take an
expert PhD they typically get about 70%
in kind of their field of strength here
so one thing that you might notice yeah
from from some of these benchmarks is
that we're reaching saturation for a lot

[00:04]
of them or nearing saturation so the
last year has really highlighted the
need for really harder benchmarks to
accurately assess where our Frontier
models lie and I think a couple have
emerged as fairly promising over the
last months one in particular I want to
call out is epic ai's Frontier math
benchmark now you can see the scores
look a lot lower than they did for the
the previous benchmarks we showed and
this is because this is considered today
the toughest mathematical Benchmark out
there this is a data set that consists
of Novel unpublished and also very hard
to extremely hard yeah very very hard
problems even turns houses you know it
would take professional mathematicians
hours or even days to solve one of these
problems and today all offerings out
there um have less than 2% accuracy um
on on this Benchmark and we're seeing
with 03 in aggressive test time settings
we're able to get over
25% yeah um that's awesome in addition

[00:05]
to Epic ai's Frontier math benchmark we
have one more surprise for you guys so I
want to talk about the arc Benchmark at
this point but I would love to invite
one of our friends Greg who is the
president of the Ark foundation on to
talk about this Benchmark wonderful Sam
and mark thank you very much for having
us today of course hello everybody my
name is Greg camad and I the president
of the arc prise Foundation now Arc
prise is a nonprofit with the mission of
being a North star towards AGI through
and during benchmarks so so our first
Benchmark Arc AGI was developed in 2019
by Francois cholle in his paper on the
measure of intelligence however it has
been unbeaten for 5 years now in AI
world that's like it feels like
centuries is where it is so the system
that beats Ark AGI is going to be an
important Milestone towards general
intelligence but I'm excited to say
today that we have a new
state-of-the-art score to announce
before I get into that though I want to
talk about what Arc AGI is so I would

[00:06]
love to show you an example here Arc AGI
is all about having input examples and
output examples well they're good
they're good okay input examples and
output examples now the goal is you want
to understand the rule of the
transformation and guess it on the
output so Sam what do you think is
happening in here probably putting a
dark blue square in the empty space see
yes that is exactly it now that is
really um it's easy for humans to uh
intu guess what that is it's actually
surprisingly hard for AI to know to
understand what's going on so I want to
show one more hard example here now Mark
I'm going to put you on the spot what do
you think is going on in this uh task
okay so you take each of these yellow
squares you count the number of colored
kind of squares there and you create a
border of that with that that is exactly
and that's much quicker than most people
so congratulations on that um what's
interesting though is AI has not been
able to get this problem thus far and

[00:07]
even though that we verified that a
panel of humans could actually do it now
the unique part about AR AGI is every
task requires distinct skills and what I
mean by that is we won't ask there won't
be another task that you need to fill in
the corners with blue squares and but we
do that on purpose and the reason why we
do that is because we want to test the
model's ability to learn new skills on
the Fly we don't just want it to uh
repeat what it's already memorized that
that's the whole Point here now Arc AGI
version 1 took 5 years to go from 0% to
5% with leading Frontier models however
today I'm very excited to say that 03
has scored a new state-of-the-art score
that we have
verified on low compute for uh 03 it has
scored
75.7 on Arc ai's semi private holdout
set now this is extremely impressive
because this is within the uh compute
requirement that we have for our public

[00:08]
leader board and this is the new number
one entry on rkg Pub so congratulations
to that thank so much yeah now uh as a
capabilities demonstration when we ask
o03 to think longer and we actually ramp
up to high compute 03 was able to score
85.7% on the same hidden holdout set
this is especially important .5 sorry
87.5 yes this is especially important
because um Human Performance is is
comparable at 85% threshold so being
Above This is a major Milestone and we
have never tested A system that has done
this or any model that has done this
beforehand so this is new territory in
the rcgi world congratulations with that
congratulations for making such a great
Benchmark yeah um when I look at these
scores I realize um I need to switch my
worldview a little bit I need to fix my
AI intuitions about what AI can actually
do and what it's capable of uh
especially in this 03 world but the work
also is not over yet and these are still

[00:09]
the early days of AI so um we need more
enduring benchmarks like Arc AGI to help
measure and guide progress and I am
excited to accelerate that progress and
I'm excited to partner with open AI next
year to develop our next Frontier
Benchmark amazing you know it's also a
benchmark that we've been targeting and
been on our mind for a very long time so
excited to work with you in the future
worth mentioning that we didn't we
Target and we think it's an awesome Ben
we didn't go do specif
you the general but yeah really
appreciate the partnership this was a
fun one to do absolutely and even though
this has done so well AR priz will
continue in 2025 and anybody can find
out more at ARC pri.org great thank you
so much
absolutely okay so next up we're going
to talk about o03 mini um O3 mini is a
thing that we're really really excited
about and hongu who trained the model
will come out and join us hey hey you
hey
um hi everyone um I'm H uran I'm open

[00:10]
air researcher uh working on reasoning
so this September we released 01 mini uh
which is a efficient reasoning model
that you the 01 family that's really
capable of uh math and coding probably
among the best in the world given the
low cost so now together with 03 I'm
very happy to uh tell you more about uh
03 mini which is a brand new model in
the 03 family that truly defines a new
cost efficient reasoning Frontier it's
incredible um yeah though it's not
available to our users today we are
opening access to the model to uh our
safety and the security researchers to
test the model out um with the release
of adaptive thinking time in the API a
couple days ago for all three mini will
support three different options low
median and high reasoning effort so the
users can freely adjust the uh thinking
time based on their different use cases
so for example for some we may want the

[00:11]
model to think longer for more
complicated problems and think shorter
uh with like simpler
ones um with that I'm happy to show the
first set of evals of all three
mini um so on the left hand side we show
the coding evals so it's like code
forces ELO which measures how good a
programmer is uh and the higher is
better so as we can see on the plot with
more thinking time all3 mini is able to
have like increasing Yow all all
performing all1 mini and with like
median thinking time is able to measure
even better than all1 yeah so it's like
for an order of magnitude more speed and
cost we can deliver the same code
performance on this for even better
insurance right so although it's like
the ultra Min high is still like a
couple hundred points away from Mark
it's not far that's better than me
probably um but just an incredible sort
of cost to Performance gain over been
able to offer with o1 and we think

[00:12]
people will really love this yeah I hope
so so on the right hand plot we show the
estimated cost versus Cod forces yellow
tradeoff uh so it's pretty clear that
all3 un defines like a new uh cost
efficient reasoning Frontier on coding
uh so it's achieve like better
performance compar better performance
than all1 is a fractional cost amazing
um with that being said um I would like
to do a live demo on ult Mini
uh so um and hopefully you can test out
all the three different like low medium
high uh thinking time of the model so
let me P the
problem um so I'm testing out all three
mini High first and the task is that um
asking the model to uh use Python to

[00:13]
implement a code generator and executor
so if I launch this uh run this like
python script it will launch a server um
and um locally with a with a with a UI
that contains a text box and then we can
uh make coding requests in a text box it
will send the request to call ult Mini
API and Al mini API will solve the task
and return a piece of code and it will
then uh save the code locally on my
desktop and then open a terminal to
execute the code automatically so it's a
very complicated pretty complicated
house right um and it out puts like a
big triangle code so if we copy the
code and paste it to our
server and then we like to run launch
This Server so we should get a text box
when you're launching it yeah okay great
oh yeah I see hope so
to be launching something

[00:14]
um okay oh great we have a we have a UI
where we can enter some coding prps
let's try out a simple one like PR open
the eye and a random
number submit so it's sending the
request to all3 mini medium so you
should be pretty fast right so on this 4
terminal yeah 41 that's the magic number
right so you say the generated code to
this like local script um on a desktop
and print out open 41 um is there any
other task you guys want toy test it out
I wonder if you could get it to get its
own GP QA
numbers that is that's a great ask just
as what I expected we practice a lot
yesterday um okay so now let me copy the
code and send it in the

[00:15]
UI so in this task we asked the model to
evaluate all three mini with the low
reasoning effort on this hard gpq data
set and the model needs to First
download the the the raw file from this
URL and then you need to figure out
which part is a question which part is a
um which part is the answer and or which
part is the options right and then
formulate all the questions and to and
then ask the model to answer it and then
par the result and then to grade it
that's actually blazingly fast yeah and
it's actually really fast because it's
calling the all3 mini with low reasoning
effort um yeah let's see how it goes I
guess two tasks are really hard here
yeah the long tail open the
problem go
go yeah g is a hard data set yes yeah it
contain is like maybe 196 easy problems

[00:16]
and two really hard
problems
um while we're waiting for this do you
want to show the what the request was
again mhm oh it's actually Returns the
results it's uh
61.6% 6 6% right this a low reasoning
effort model it's actually pretty fast
then full evaluation in the uh in the A
minut and somehow very cool to like just
ask a model to evaluate itself like this
yeah exactly right and if you just
summarize what we just did we asked the
model to write a script to evaluate
itself um through on this like hard GQ
Set uh from a UI right from this code
generator and executor created by the
model itself in the first place next
year we're going to bring you on and
you're going to have to improve ask the
model to improve itself yeah let's
definely ask the model to improve it
next time maybe not
um so um besides code forces and gpq the

[00:17]
model is also a pretty good um um math
model so we we show on this plot uh with
like on this am 2024 data set also3 Min
low achieves um comparable performance
with all1 mini and 03 mini medium
achieves like comparable better
performance than 01 we check the solid
bar which are passle ones and we can
further push the performance with all3
mini high right and on the right hand
side plot when we measure the latency on
this like anonymized o preview traffic
we show that all3 mini low drastically
reduce the latency of 01 mini right
almost like achieving comparable latency
with uh gbt 40 where under a second so
probably is like instant response and
also Mei medium is like half the latency
of
o1 um and here's another set of eval I'm
even more excited to to show you guys is
um uh API features right we get a lot of

[00:18]
requests from our developer communities
to support like function calling
structured outputs developer messages on
all mini series models and here um all3
mini will support all these features
same as o1 um and notably it achieves
like comparable better performance than
for all on most of the evil providing a
more cost effective solution to our
developers cool um and if you actually
enil the True gbq damond Performance
that I run a couple days ago uh it
actually also mean l is actually 62%
right we basically ask model to eval
itself yeah right next time we should
totally just ask model to automatically
do the evaluation instead of
ask um yeah so with that um that's it
for alter Mei and I hope our user can
have a much better user experience in
already next year fantastic work yeah
thank great thank you cool so I know
you're excited to get this in your own

[00:19]
hands um and we're very working very
hard to postra this model to do some uh
safety interventions on top of the model
and we're doing a lot of internal safety
testing right now but something new
we're doing this time is we're also
opening up this model to external safety
testing starting today with O3 mini and
also eventually with 03 so how do you
get Early Access as a safety researcher
or a security researcher you can go to
our website and you can see a form like
this one that you see on the screen and
and applications for this form are
rolling they'll close on January 10th
and we really invite you to apply uh
we're excited to see what kind of things
that you can explore with this and what
kind of um jailbreaks and other things
you
discover cool great so one other thing
that I'm excited to talk about is a a
new report that we published I think
yesterday or today um that advances our
safety program and this is a new
technique called deliberative alignment
typically when we do safety training on
top of our model we're trying to learn
this decision boundary of what's safe

[00:20]
and what's unsafe right and usually it's
uh just through showing examples pure
examples of this is a safe prompt this
is an unsafe prompt but we can now
leverage the reasoning capabilities that
we have from our models to find a more
accurate safety boundary here and this
technique called deliberative alignment
allows us to take a safety spec allows
the model to reason over a prompt and
also just tell you know is this a safe
prompt or not often times within the
reasoning it would just uncover that hey
you know this user is trying to trick me
or they're expressing this kind of
intent that's hidden so even if you kind
of try to Cipher your your prompts often
times the reasoning will break that and
the primary result you see is in this
figure that's shown over here we have um
our performance on a rejection Benchmark
on the x-axis and on over refusals on
the y- AIS and here uh to the right is
better so this is our ability to
accurately tell when we should reject
something also our ability to tell when
we should review something and typically

[00:21]
you think of these two metrics as having
some sort of tradeoff it's really hard
to do well I'm it is really hard to yeah
um but it seems with deliberative
alignment that we can get these two
green points on the top right whereas
the previous models the red and blue
points um signify the performance of our
previous models so we're really starting
to leverage safety to get sorry leverage
reasoning to get better safety yeah I
think this is a really great result of
safety yeah fantastic Okay so to sum
this up 03 mini and 03 apply please if
you'd like for safety testing to help us
uh test these models as an additional
step we plan to launch 03 mini around
the end of January and full 03 shortly
after that but uh that will you know the
more people can help us safety test the
more we can uh make sure we hit that so
please check it out uh and thanks for
following along with us with this it's
been a lot of fun for us we hope you've
enjoyed it too Merry Christmas Merry
Christmas Merry Christmas

[00:22]
[Music]

</details>
