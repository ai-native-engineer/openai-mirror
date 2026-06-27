---
title: "OpenAI Codex Live Demo"
channel: openai
url: https://www.youtube.com/watch?v=SGUCcjHTmGY
youtube_id: SGUCcjHTmGY
published: 2021-08-10
duration: "29:42"
captions: en-orig
---

# OpenAI Codex Live Demo

[![OpenAI Codex Live Demo](https://img.youtube.com/vi/SGUCcjHTmGY/hqdefault.jpg)](https://www.youtube.com/watch?v=SGUCcjHTmGY)

<details>
<summary>자막: OpenAI Codex Live Demo (29:42)</summary>

[00:00]
hello everyone welcome to the open ai
codex live demo today we're going to be
showing you the latest version of our
model that can write code i'm greg
i'm voice and i'm ilia
before we get started i want to talk to
you a little bit about how we got here
so a year ago we released gpt 3 which is
a general purpose language model it
could basically do any language task you
would ask it
so the thing that was funny for us was
to see that the applications that most
captured people's imaginations ones that
most inspired people were the
programming applications
because we didn't make that model to be
good at coding at all
and so we knew if we put in some effort
we could probably make something happen
so voice check and the team sat down to
really make it really make it reality so
actually that was a quarter of company
being involved in the effort i bounced
ideas with ilya
for a year and actually even in reality
for multiple years we're dreaming about
models that can code and greg personally
he was babysitting

[00:01]
this model
so when we started we created the
benchmark on our benchmark you know
despite the fact that gpt3 had some
rudimentary coding capability it
achieved
zero percent uh accuracy in the
meanwhile we got to the models that can
in 27 percent write entire multiple
lines of code and solve our coding
benchmarks today we are
presenting model that solves 37 percent
of problems but of course these are just
their raw numbers how does it feel
you're gonna see today
and before we jump into the demos i want
to talk about how you can get access to
codex and that's really the point of
this demonstration we want to help
inspire people to see the kinds of
things that codecs can do and we know
that we're actually just scratching the
surface of what's possible so we
actually really need your help to really
dive deep into this model
so the first announcement of the day is
that starting today
the codex model will be available in

[00:02]
openai api so we're going to be doing a
beta please go and sign up get on that
that wait list we're going to go and
scale up as quickly as we can and try to
get this out to everyone
so the second way that you can get
access to codex is we're going to be
hosting a new kind of programming
competition
this will be held on thursday at 10 a.m
pacific i everyone's going to get access
to codex as their teammate it will also
be a competitor on the leaderboard so
it'll be really interesting to see what
it's like to work with codex everyone's
going to be able to play with it and be
able to really experience the kinds of
things we're showing you today so please
show up it's going to be a lot of fun
and i think a very unique event
it's all right let's get started with
the demos
cool thank you friends have fun all
right see you later wojciech
all right hello greg hey ellia so you
have a coding demo we do so there's only
one way to start a coding demo and that
is hello world all right of course
so what you see here is that greg is
typing say hello world into the text box

[00:03]
now he'll press the green play button
the model will produce the code and then
you will see its output below and so
exactly right so what you're seeing here
is a sim simple interface we built on
top of the codex api so everything
you're going to see today is just using
the same api everyone's going to get
access to um so you could build the
exact same thing so this very simple
interface all that we do is we format
the instruction to the model and we
happen to format it a little bit like a
python docs string so that you know it
looks a little bit like a like a comment
um
the model generates code
which we then just execute and the
output is displayed here so as a user of
this kind of system
you just kind of ask the computer to do
something and it actually does it well
it looks like he did a good job with
hello world but let's make it a little
bit more complicated let's say
hello world with empathy
say hello world of empathy interesting
all right
it's just a slightly ambiguous
instruction do you know what you would

[00:04]
say to this
i mean
i can think of multiple things i want to
know what the model is all right let's
see what happens
i think that's actually a very
reasonable choice
and you know you can you can ask the
model you can you can modify your
instructions to the model as well um so
the kind of thing that you can do is you
can also ask it for information that is
kind of stored in a session so now i'm
going to say instead of saying hello
world with empathy i'm going to say it
with empathy and again the model is kind
of free to make a choice of what it
wants to do with that um in this case
you know it decided to do the same thing
which i think is is a reasonable choice
it formatted the code a little bit
differently um but fundamentally if you
notice it now has to kind of back
reference
to to the previous part of the
conversation and under the hood this is
just a single request to the codex api
that we're formatting just like you
would a gpt3 request so it's almost like
a chat session of
human
model human model and so forth so it
looks like the model did a satisfactory
job with saying hello world with empathy

[00:05]
but
could it say it five times okay
that's an awful lot of empathy i think
it did not a bad job but it's not quite
exactly what i wanted i didn't i wanted
to be hello world with empathy
with each line which each one of those
things appearing on you on a new line
now if you if you
if you want to look at the code you can
that's the great thing about a model
like this this is very interpretable and
so you can actually
look and see hey this just did print
where it multiplied by five so you
couldn't say and still instead say now
instead
do it with a for loop
which again starts to be a lot of back
referencing
but there we go
is that what you wanted it also did what
i wanted as a byproduct in addition to
doing it with the for loop so i'd say
it's it's not it's not a bad start or a
hello world demo yes but i think we can
go further all right we should say
exponentially more hello world by making
it we should make a web page we've got
to make a web page if we really want to

[00:06]
broadcast our message of hello world to
the world um so first of all i make a
web page that says
let's say our message and save it to a
file
oh oh yeah
taking a little bit of risk here it
worked there we go so i if you notice if
you can see the code it's actually
writing python that then emits some html
and that's again one of the powers of
this model is it's a single model that's
proficient in over a dozen programming
languages and that means it can kind of
just seamlessly figure out okay i'm
supposed to do html here or if you want
to translate from one language to
another it's quite good at that um and i
think this shows you why you really want
all of that capability in a single model
okay so is is that all we need for a web
page well we should probably let people
see the web page seems like a good idea
all right so let's start a python
web server to serve that page
let's give that a try
it looks like pretty complicated

[00:07]
specialized code yes um so let's
actually take a look so we have web
server running on port 8000 so we'll
take a look
oops oh close to 8 000 excuse me
and there we go hello world with empathy
oh
i would i would say it's a success i
think it's a success yes so this is the
first time we've ever generated this
particular message so we actually didn't
know what it's going to say um so you
know that this particular web page was
in fact generated just now on the fly
for all you viewers out there
i think that was nice to say hello world
with a web page but we should go further
even still i think we should and so you
know first of all i do want to point out
that this particular example of writing
a python web server is something i've
done a dozen two dozen times and i still
never remember how to do it because
between python two and python three the
exact like structure of the modules
changed uh that you have to like create
this handler object you pass it to a tcp
server that you pass the address here
and a port and oh yeah your address
could be an empty string if you want and
then you do serve forever and this

[00:08]
it's complicated and this kind of stuff
is not the fun part of programming right
the fun part of programming you know i'd
say programming is kind of two things
one is understand the problem and that
includes talking to your users that
includes thinking super hard about it
and decomposing into smaller pieces this
is the like really cognitive aspects of
building something
and then there's a second piece which is
map a small piece of functionality to
code right whether it's an existing
library an existing function whether
it's in your own code base or out there
in the world and that second part is
where this model really shines like i
think it's better than i am at it
because it really has seen the whole
universe of how people use code you
should think of it as a model that's you
know gpt was trained on all the text out
there this model's been trained on all
the text and all the public code um so
it really i think accelerates me as a
programmer and takes away the boring
stuff so i can focus on the fun ones
okay so that is a working
web page that you've got but
wouldn't it be nice if you could send
lots of emails with hello world to
everyone who is listening to us on the

[00:09]
on the live stream
yes so here's here's a moment for for
everyone to participate um so if you
would like to receive an email as part
of this demo from codex i i think that
we should be posting a link to sign up
in to the chat now i should also be
displayed on the screen so please go
ahead and sign up and
will we'll give you a moment to do that
and while we are waiting for you to sign
up i want to point out
how insane it is that what we are
showing to you works at all
it is fundamentally impossible to build
such a system except by training a large
neural network to do really good card
auto complete that's all we did
it is really simple conceptually
although perhaps not in practice to just
set up a large neural network which is a
large digital brain which has a
mathematically sound learning procedure
and that part can be understood and it
is relatively simple

[00:10]
and then you make it work you make the
neural network big
you train it on code autocomplete and by
being
good enough at code autocomplete we get
the capabilities that you see here it
actually reads all the letters
all the words that we are giving it
it chews and digests them inside of its
neural activations inside of its neurons
and then it emits the code that we see
and because the autocomplete is so
accurate the code actually runs and it
runs correctly
so now let's show you how to hook codecs
up to sending email so we're going to be
using the mailchimp api in order to do
this um and you know codex again has
seen all the public code out there but i
wanted to use my mailchimp account and
maybe i have a particular way that i
want to call the api so it's very easy
to
give
codecs new capabilities almost the same
way that you explain to a programmer how
to use a new method you can do the same
thing for codex and so i want to show
you the only magic that's going on here
is that we have uh this plugin where on

[00:11]
the left is instructions for humans uh
for humans and uh we can take a look at
the actual code that is supposed to be
installed on our system it's just a very
simple wrapper around the mailchimp api
where i plugged in the api key
already and now we can simply take this
documentation written
you know in very readable form and paste
it to the model so literally just those
three lines of text
is enough for the model to understand
how to use the api exactly um but before
we send the message what actual message
should we send to people i mean they
should obviously hello world as well as
something truly useful
like the price of bitcoin that sounds
extremely useful
so we'll ask the model to look up the
current bitcoin let's see if it works
all right so it seems to have done
something and by the way this particular
api i guess is used enough out there in
public code that the model failed is
worth its while to to memorize exactly

[00:12]
how it works um and now let's actually
send the email blast now send everyone
in
email telling them a hello world and b
the current bitcoin price
so we'll leave it a little bit up to the
model to decide exactly how it wants to
format that email yeah i'm curious what
messages will choose let's see what
happens
all right oh looks like a very sensible
message indeed so now it's calling the
the mailchimp api
so let's give it a moment spinner is
still spinning yeah so it will probably
oh there we go that's a lot of emails
yeah so we're sending
1472 emails it may take a little bit of
time for these to deliver
again at this point codex has done its
job uh at this point we've made the call
to mailchimp mailchimp is cueing these
emails up on its servers as we speak but
as you receive the emails please post on
twitch chat so everyone knows that they
were received
so i feel like it was a pretty
satisfactory hello world demo i think
this is the world's most advanced hello
world demo and while 1472 lucky

[00:13]
recipients are waiting for the email
it's time for us to move to our next
stage i think so let us build a game all
right so we've shown
building you know sort of very simple
functionality right so that it's kind of
single shot you know it required a
little bit of back referencing but
mostly it's you ask for a particular
thing you want done right away and maybe
it involves doing some complicated
import of a particular api and use it in
a specific way but what we want to show
now is building up a more complex
program actually you know sort of
building building something that spans
many lines of code that's right and the
game i have in mind is one where a
person will be trying to dodge the
boulder all right well let's give that a
try um
so
first of all i'm going to look up
a silhouette of a person
i figure we should probably not use a
real image of a person for this because
they're going to get squashed by a
boulder that is a very wise choice and
what you see here is something very
similar to the previous demo where greg

[00:14]
is typing the instruction to the text
box then he presses play
the model does its neural magic and
produces code and now we get this
oversized person on the page yep and i
want to point out so the the only
difference here as far as the output is
concerned is this is outputting
javascript as opposed to python it's
actually the same model under the hood
so the only piece of magic we're not
showing you right now is that we provide
a little bit of context to the model in
the case of python we have just one
example of following an instruction in
python in the case of javascript we have
like two examples of doing it
and from there the model latches on and
just continues and continues
yeah so i feel like it was a good first
step but what i would really like is for
the person to be a lot smaller and for
it to be controllable with the left and
right arrow keys great and we also just
got a report that the emails have
started rolling in so i think that's a
success for for mailchimp and for uh for
codex so i think that's great um so
let's see how big we want to make the
person maybe 100 pixels does that seem
about right let's find out all right

[00:15]
let's give that a try and actually what
i'm going to also do is i just want to
show people the full prompt that's being
sent so that you can really see what's
going on without any magic so i just
opened up the chrome inspector we have a
completions endpoint and you can
actually just uh scroll to this is the
post message and you can look at the
entire
bit of the prompt
and let me show you
what that looks like expand it out and
to just to just explain what you're
seeing here the way this neural network
works is that it's a really really good
pattern completion system that happens
to work on patterns in code it's like
the world's best yes and improv actor
whose domain happens to be code rather
than improv exactly and so we simply
provide it with this context of oh
you're supposed to follow some
instructions and then the model realizes
my job is to latch on to instructions
okay so let's get back to building
so we've got the person's 100 pixels
look pretty good i think so all right

[00:16]
now what do you want me to happen next
next so i want it to be
at a reasonable position at the bottom
of the space of the screen and to be
controllable with arrows all right well
let's do that so first let's set its
position to
uh let's say you know 500 pixels down
and 400 pixels from the left
seems reasonable as far as i can tell
all right let's see what happens
all right perfect and now make it
controllable with the left and right
arrow keys
now this is a pretty high level
instruction you know exactly what's
supposed to happen when you push left
and what's supposed to happen when you
push right you know the model really has
to infer
what's going on in here and it can't
look at the screen the model only has
access to all of this text over here and
so from that alone it has to infer what
to do but let's see if it worked let's
see i'm curious myself the code looks
reasonable
okay
it's quite good
but this looks like something i don't
quite like
i don't want it to be able to get out of

[00:17]
the screen right you found the problem
but it is alive which i think is pretty
good but let's see if we can fix that
problem so constantly check if the
person
is
off screen
and put it back on the screen if so so
again pretty high level um it's possible
that the model won't quite know what
we're asking for but let's give it a try
okay let's test it
okay this side looks pretty good to me
pretty good what about the other side
let's see what's happening there
okay so that looks good too except that
you see this flickering scrollbar at the
bottom that is no good well fortunately
you can just say disable scroll bars by
the way i actually don't know how to do
this in javascript that's the model now
let's test
the model does no there we go so phase
one complete the person is movable um so
there is there is a suggestion from
twitch to see if we can make it move
upwards if you press spacebar all right
well let's give it a try um so also make
the person move upwards
if you press space bar

[00:18]
let's give that a try
all right you think it's going to work
let's find out
oh
and there we go that is nice we need to
make it also move downwards oh no
okay and make it move downwards if you
press the down arrow key
so we now have this nice flying person
let's see
okay so now we have given it full okay
all directional control good good good
all right perfect so we now have this
very nice game where the person can go
anywhere with very unintuitive usage of
a space bar
right you know if you want to modify
this uh please feel free to try it at
home one of the great things about this
playground is that
it's very easy to export these commands
you know you can almost think of this
text as the new kind of source code and
people can modify it and fork it so i
think we're going to see lots and lots
of games appear once people start
playing with codecs okay so a moving
person is quite nice but we need to get
a boulder that we'll be dodging all
right so let's search for an image of a

[00:19]
boulder
this one definitely this boulder all
right that's a very nice boulder i i
could not agree more i would not want to
be that person having to run away from
this okay so once again we just request
for the boulder to appear
and it appears i i hope it will appear
oh it does appear an oversized massive
massive boulder let's make it smaller
all right uh how many pixels um
can you just ask it to be small
that's a great point make it small
okay this is too small can you ask it to
be four times as large
let's give it a try
that's actually interesting so it
actually used uh it used a
style.transform now you might want to do
it that way if you want to do it a
different way you can also just say
you know set the width to be 4x larger
and the great thing about
i all this javascript just running
directly in your browser and so we
actually have all of this this this
playground set up so that if you don't
like an instruction you can just delete
it if you want to modify it you can

[00:20]
always just edit it and then you can
edit the code directly yeah so i like
the size of this of this boulder perfect
but now i want it to fall down okay and
then when it hits the ground i want it
to reappear from the top again
somewhere else now the thing about codex
is that you know again coding is two
things it's deeply understanding a
problem figuring out how to chunk it up
into smaller pieces and it is secondly
mapping a small chunk of problem
statement to code
and codex really excels at that first
part the first part if you ask for too
much at once it won't succeed and so
let's actually let's actually give it a
try just to say you know now fall from
the sky and wrap around
okay i wonder if it will work let's find
out so this is going to require doing a
lot of things um so in fact if you
notice all that it did is it just did
the first part of saying you know what i
got to get it absolutely positioned i
put it in a particular location um it
didn't do the second part and so when
when codex fails like this the kind of
thing you can do is you can just try
again and i think that again like one
really nice thing about doing this in
javascript is there's no punishment for

[00:21]
getting it wrong right you have a system
that's very stateless that you can just
re-execute and try again your iteration
cycle can be just truly immense and that
for me has been kind of the most
exciting part about working with codex
is that it just kind of means that you
get to just think about what you want
and you spend less time of like okay now
i need to go to stack overflow and
figure out how you know whatever uh you
know what whatever property it is to
disable the scroll bars which i have
already forgotten um but let's now try
breaking down this instruction into
smaller pieces so first you know i think
codex had a good good point that we
should set uh first position it um
uh to you know let's set its position
to the top
of the screen at a random horizontal
location
hopefully that's a simpler instruction
that it could do seems pretty good and
it did it yep and if we want to verify
it's actually random we can just kind of
re-execute this code multiple times it
seems pretty random to me now have it
fall from the sky and wrap around let's
give this a try so again still a lot
going on in the construct this

[00:22]
instruction so it may not work the code
is since oh it's moving it's going down
okay we got something we've got some
signs of life got some signs of life
he's going back and yes there we go all
right very nice this is very very nice
indeed it is alive all right great so i
think in order to uh in order to put a
capstone on this game uh we just need to
indeed there's no game if you can't lose
sad sad to say but we do need to
implement that loss condition so first
define what happens when you lose
clear the screen and
show a message
saying you got squashed it should be an
encouraging message ideally um okay well
let's let's so i just kicked this one
off let's make it encouraging so now
modify that function now rewrite that
function
to
also include some words of encouragement
excellent i'm also curious what words of
encouragement the model will choose
so you can do it um so that that's
that's pretty good
and uh so so the only thing is that the

[00:23]
way that this actually was implemented
is implemented as a key down listener
and what we really want is we want a
function that gets called when you lose
so we can get rid of both of these and
we could try this one more time
and so how would you make it different
so you can say
define a function
so make a function
that gets called
okay let's see if it works oh it is a
function it is called you lose
and now rewrite that function to include
words of encouragement all right let's
see what happens here
and sure enough it makes a new
eye try again all right let's let's see
what happens now we actually have to
wire this function up so when the person
and the boulder
overlap at all so constantly check
if the person to boulder up over up at
all and if so you lose
so i'm not even going to say explicitly

[00:24]
call that function
just it's got to figure out that that's
what we want so we'll see if that
happened um yeah do you want to do the
honors definitely oh man all right
moment of truth here moana truth success
you got squashed and a very encouraging
message to try again i think that's very
good life advice from codex right there
okay
i feel like it was a nice game that we
built in a small number of minutes i
think so so we have one more thing to
show you
and that uh with this demo we want to
help expand your mind to the you know to
the possibilities the codex can really
offer and indeed
one of the things that we showed you in
the hello world demo
is that it's very easy
to teach the codex model to use whatever
api you want api doesn't know
and conveniently
all your favorite software comes with an
api in fact i used to work at a company
whose entire
job is to build an api apis are out
there that these days the world is

[00:25]
really programmable and codex is able to
hook into those apis on your behalf and
so that the kind of end-to-end
functionality that i think starts to be
unlocked is that you talk to your
computer and it actually does what you
ask
all right let's let's see how it works
all right so here we have my ipad with
just vanilla microsoft word installed on
it um there's one little one little
secret within it that we'll get to in a
moment um but it turns out that
microsoft word like many pieces of
software has an api in fact it has a
javascript api and hey we built a model
that is pretty good at javascript quite
convenient very convenient so all we did
is that we took this api reference and
we formatted it for codecs and so you
know we kind of trimmed it down it's not
the whole whole implementation of the
whole api um but it's enough to make a
very interesting proof of concept and so
let me show you
the kinds of things you can do so here
is a poem that was actually one of my
favorite poems as a child really oh yeah
yeah it's called the jabberwocky uh it's
very fun um
so i'm gonna paste it into microsoft

[00:26]
word and uh oh shoot let me get rid of
these leading spaces before we start
sorry on this greg this will take
forever hold on hold on
you know what fortunately with the codex
add-in
i don't have to delete them
delete all initial spaces
and it worked it did work the initial
spaces are gone
but all the other spaces are still there
still there and just like before the
instruction at the top was turned into
code which was then run by microsoft
word exactly and so we're just using the
standard microsoft word api here so they
provide a function functionality for you
to get your little sidebar that we show
here and we just basically reuse the
exact same code that we've written for
those other demos and so all that's
going on here is that we use the
built-in speech recognizer so we didn't
write that so if it has transcription
errors
we take no responsibility for it um

[00:27]
but then
we send whatever request is put here to
the api and it generates
actual code in the microsoft word api
and what you see here is a taste of the
future
as the model gets really good as the
neural network gets really good at
turning instructions
to correct api calls it will become
possible to do more and more
sophisticated things with your software
just by telling it what to do and i
think this is the biggest contrast with
gpt-3 like the biggest step on top of
gpd3 in my mind and this wasn't obvious
to us going in but i think it's kind of
emerged from what we've built
gpd3 is a system that you talk to and it
talks back to you so the only impact it
has is in your mind
with codex you talk to it it generates
code which means it can actually
manipulate or you know it can actually
act in the computer world on your behalf
and i think that that's a really
powerful thing that you actually have a
system that can can carry out commands

[00:28]
on your behalf
for example let's do something a little
bit more complicated yep um so uh do you
want to give it a try yes
now make every fifth line bold
okay few i was really worried about the
speech recognition part yes well there
we go oh a success a success indeed so i
think that's pretty good and you know i
think that that
what this kind of demo shows you is what
today's voice assistants have really
been lacking
that i think that what you really need
is you need a system that has the kind
of gpt world understanding so it can
flexibly sort of interpret between
different languages and can really
understand the intent that you're you're
putting forth and while we are very
happy with the neural network that we're
showing you today which is a better code
model than the one we had previously it
is still only just a step
the neural networks the code neural
networks you'll have in the future will
be far better than this so this is only

[00:29]
the beginning of
an exciting future
and so that's the end of our demos uh
we're really excited that you were able
to join us and so just to review uh
today we showed you the latest
generation of the codex model it's
available in open eyes api starting
today so please sign up on on the beta
list
if you want to be able to play with
codex in the context of a pretty awesome
new kind of programming competition that
will be thursday 10 a.m uh we're really
excited for you to get a chance to play
with it so thank you very much for for
tuning in we're excited to see what
you're going to build and thank you for
joining us to experience the magic of
neural networks

</details>
