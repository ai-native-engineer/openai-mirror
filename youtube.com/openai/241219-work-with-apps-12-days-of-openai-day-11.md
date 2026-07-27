---
title: "Work with Apps—12 Days of OpenAI: Day 11"
channel: openai
url: https://www.youtube.com/watch?v=g_qxoznfa7E
youtube_id: g_qxoznfa7E
published: 2024-12-19
duration: "19:04"
captions: en-orig
---

# Work with Apps—12 Days of OpenAI: Day 11

[![Work with Apps—12 Days of OpenAI: Day 11](https://img.youtube.com/vi/g_qxoznfa7E/hqdefault.jpg)](https://www.youtube.com/watch?v=g_qxoznfa7E)

<details>
<summary>자막: Work with Apps—12 Days of OpenAI: Day 11 (19:04)</summary>

[00:00]
[Music]
hey everybody Welcome to day 11 I'm
Kevin wheel I lead product at open aai
and I am definitely outclassed by the
two gentlemen on my right who I'm told
did not just get these uh suits 48 hours
ago on Amazon definitely definitely own
this already 100% yeah all right so you
might have noticed we've been putting a
lot of effort into our desktop apps uh
so we we launched our Mac desktop app
about 6 months ago we launched our
Windows desktop app just a couple months
ago and as our models get increasingly
powerful jet GPT will more and more
become agentic uh and that means we'll
go beyond just questions and answers
Chet GPT will begin doing things for you
we're seeing that already uh with
products like canvas where uh you're
collaborating with chat gbt to help
improve the your writing and your code
and that shift will continue and we'll

[00:01]
do chat GPT will do more and more on
your behalf the desktop apps are a big
part of that too because being a desktop
app you can do so much more than you can
just in a browser tab that includes
things like with your permission of
course being able to see what's on your
screen and being able to automate a lot
of the work that you're doing on your
desktop so we'll have a lot more to say
on that as we go into 2025 but we've
also got some exciting stuff that we're
launching today so let's dive in all
right hi I'm John nastos and I work on
the chat GPT desktop team my name is
Justin Rushing and I also work on the
chat GPT desktop team uh we've got a lot
to show you today so I'm just going to
go ahead and get started
here um so first things first this right
here is the fully native chat GPT
desktop app for Mac uh it does all the
things that you know we've come to
expect from our clients um but what I
really love about it is that being
native it's really lightweight doesn't
use a lot of resources it uh it lives
its own window and um it I'm able to use

[00:02]
it without having to context switch away
from what I'm already doing right so
we've got this keyboard shortcut option
space that makes it really fast to show
and hi chat GPT so it's it's always
there when you need
it this button right here is our entry
point for working with apps on your
computer and the way that I like to
think about this feature is that we all
copy and paste things into chat GPT
right all the time all the time all the
time um this feature makes that way
Smoother by when we are working with an
app on your computer we'll automatically
pull that context in for you so you just
focus on asking your question and we we
handle the rest so you might notice that
I've also got this warp uh console
window open as well it's currently
navigated to a repository that that I'm
getting up to speed on um and it might
seem kind of silly but I want to figure
out how many commits per day are
happening in this repo you know we talk
about velocity a lot here so I want to
see that for myself I have no idea how
to do that that though so I'm going to

[00:03]
use chat
GPT so when I click on this button I'm
going to see all of the apps that are
currently running on my computer the
chat GPT can work with uh important note
until you select one of these we will
never look at the contents of another
app so you are always fully in control
over what you're sharing with chat GPT
so to get started I'm going to click on
warp and at this time huge shout out to
the warp team for all of their help in
getting this going uh when we first
announced working with apps we did not
have support for Warp and it was I think
literally the first request was adding
support um so huge shout out to the team
they worked really hard to help us uh
get it ready for today so thank you so
I'm going to get started by saying uh
write a command to get the number of
commits per day over the past two months
and now I don't need to tell chat GPT
that I use get because it can tell from
warp that I do um and it's just going to
give me the command that I need so I'll
push this button to copy and paste it

[00:04]
into warp and I I think this looks right
yeah it's looks like the right
information but it's also kind of hard
to tell what we're looking at right yeah
I'm I'm a visual learner myself so um
normally what I would do is I'd figure
out how to get this into a spreadsheet
make a chart there and then find that
spreadsheet again in three years but um
instead I'm just going to uh I'm just
going to ask for one so make a bar graph
with all of the
results why not make it holiday themed
great idea
and uh awesome so this is going to show
off what I think is the coolest part
about working with apps which is that it
works with all of the other features and
all of the other models in chat GPT so
in this case uh for decided to use
Advanced Data analysis to crunch some
numbers and give me back a bar graph and
what that means if you really think
about it is that when we build features
like Advanced Data analysis and bring
them to chat GPT it's kind of like we're
bringing them to every app that chat GPT
works with yeah that's great so while it
thinks about this um do you want to talk

[00:05]
a little bit about what the model is
actually seen is it just what we see on
the screen or is it something more great
question so an easy way to do this would
be to just grab a screenshot and and let
Vision do the rest um but we actually
can reach into the application to grab
ascreen content as well and so uh these
results will contain everything here not
just what you see on screen yeah I was
thinking hard about this it might be the
the holiday themed
part okay perfect all right I mean this
is that looks pretty holiday themed to
me what do you think John uh it's
holiday themed I don't know if it's as
holiday themed as we are in these suits
but it's not bad literally nothing is as
holiday themed as you are yeah perfect
perfect but I'd say it's good enough so
I'm just going to download this and now
I can share it with a teammate but with
that I'm going to hand it back to John
to talk a bit more about programming
great so I think that the use case that
Justin showed is really important and
useful to be able to interact with a
terminal but I want to show what it's
like to interact with code in an IDE so

[00:06]
I have xcode open here which is my IDE
of choice and it's running a sample app
that is actually a little bit of a peak
behind the scenes into how this work
with apps feature works the sample app
uses the Mac OS accessibility apis to
look at xcode and tell us some things
about what's on the screen so it's
telling us that there's a text field
with these Dimensions it tells us that
it has 37 lines and we can go down and
check that 37 lines yep and it shows us
the content of the text field and we
actually use this to make the feature
right that's right yeah this is a useful
sample app for us for sure so this is
nice but it doesn't do any live updating
so I'm going to use chat GPT to help add
that feature I'm going to bring up the
chat bar with a very similar shortcut to
what Justin showed earlier but with a
slight change I'm going to use option
shift one and what that does is it
brings up the chat bar with xcode
automatically paired to it xcode being
the topmost app that is open that we
support with this feature it makes it

[00:07]
super quick to start working with an app
yeah it's great and you get this
immediate feedback that it sees xcode
here so these accessibility apis are a
little bit inscrutable definitely hard
to remember how to use and pretty
complicated actually um so I'm going to
use the model selector here and I'm
going to switch this to 01 01 is one of
our new newer models here at open Ai and
it does a great job thinking about these
difficult coding problems
um and I should mention as well that uh
this feature is also available with 01
Pro if you really want to throw the deep
end coding problems that model yeah all
right so let's give it a prompt here I'm
going to say add an
observer uh so if selection
changes load text areas is
called and we'll kick off this request
to the model so o1 is one of our Chain
of Thought models and you can see that

[00:08]
it's thinking about this issue it's
going to tell us some of the steps that
it goes through as it considers and wow
that was a pretty fast response from it
didn't have to think too hard on that
one I guess I guess not you got to give
it a harder problem next time yeah wow
all right so it's generating some code
and you know I have a fair amount of uh
of trust in 's code here so as soon as
it's finished generating I'm just going
to copy this into xcode and we're going
to run it and see what happens I don't I
don't see anything that could go wrong
with that no demos Poss yeah live demos
work 100% of the time it was one of the
rules of the universe all right so I've
copied that code and I'm pasting it
directly into xcode I'm going to take a
quick scroll through it to see if it's
finding any issues right now it's
looking pretty promising all right so
let's run this and see what happens you
know it would be really cool if you
didn't have to copy and paste that back
into xcode though that would be cool and
you know people have been suggesting

[00:09]
that should I build that you should
definitely build that all right PM
approved great all right so uh let's
it's running again uh let's take a look
if I select content oh no it didn't it
didn't work like we thought okay should
we should we give it one more shot yeah
why don't we why don't we ask yeah all
right so I think I'm actually just going
to go back to our previous state since I
don't have a specific error here uh
let's try to discard the changes
all right let's give it one more shot
yeah one more shot yeah and while it's
working we can uh talk about some more
of the features here okay add an
observer so if selection
changes load text areas is called again
all right maybe it didn't think hard
enough on that we'll try it again got
overconfident yeah well it thinks about
this I should mention that I'm using X
code uh like I said this is my IDE of

[00:10]
choice when working with swift but we do
support a whole bunch of other idees um
that means vs code uh the jet brains
ecosystem which includes Android studio
and Pie charm Ruby mine things like that
some really uh standby Mac apps like
textmate and BB edit so we've got a a
whole lot of different support here yeah
I'm I'm actually unreasonably excited
for mat lab support I would have totally
used that in college yeah mat lab is is
another exting one I think some students
are really going to find that useful
okay it's uh it is still generating some
code there it goes it's done I'm going
to use this copy button again and again
with full trust that everything is going
to work I'm going to now we know what
could go wrong though right yeah sure
all right so let's run this again and uh
see if we have slightly better luck okay
it's
running hey look at that if I things it

[00:11]
changes wow it's a holiday Miracle you
got the incantation to the demo Gods
right the second time yeah exactly
awesome so we've been talking a lot
about coding today right uh but another
thing that I love to use chat GPT for is
helping me with my writing and I know
I'm not alone here um and so that's why
today we're announcing support for three
new applications Apple notes notion and
quip uh we think this is going to open
up a brand new set of use cases for
working with apps and so we can't wait
to see what you all do with it uh with
that uh John Kevin you already know this
but for the rest of you uh I give
walking history tours in San Francisco
outside of outside of work um big
history buff San Francisco's got a great
story to tell and I'm actually working
on a brand new walking tour and so why
don't we try out this feature and help
me out with that let's do it great so
here I have a notion document open on my
computer I always write my tours in
notion and this is actually a real
walking tour that I'm working on so
I I hope you all find it interesting um

[00:12]
but I'm actually working on a news stop
for my favorite character in San
Francisco History Emperor Norton um I
know some high level talking points he
was the self-proclaimed emperor of the
United States and protector of
Mexico who lived in San Francisco in the
1800s and uh he even made his own
currency that was actually valid in the
city for a while that's something you
can just do yeah apparently apparently
you can and uh I think it's going to
make for a great tour stop but I'm a
little bit fuzzy on the details and so
I'm going to use chat GPT to help me out
uh one option would be to copy and paste
these bullets over and I think chat
would do a pretty good job at at going
with that but it would be helpful if it
had context of the entire document right
and so instead I'm going to have chat
GPT work directly with notion so I'm
going to hit option space to bring up
chat GPT have it work with notion and
I'm actually going to go ahead and just
um highlight this stop here so that the
model knows what to pay attention to and
so now we can see we're working with
notion in the walking tour document

[00:13]
focused on selected lines and I'm just
going to go ahead and say fill out these
talking points right don't need to be
any more specific than that um but one
thing that is really important is that
this is a walking tour right this is a
history tour things need to be factually
correct and so to help with that I'm
going to push this button to turn on
search and now to answer my question
chat GPT is going to search the web and
everything it tells me is going to be
grounded in citation
right and so I want to find out more
about I can go ahead and click the links
and you really start to see this awesome
interaction Loop pop up where chat GPT
is helping me with my research in the
context of the document I'm
writing so awesome this looks like all
of the stuff that I'm hoping to cover
and so it doesn't really sound like me
though this sounds like you know
official results and so I'm going to
turn off search and just say uh make it
match the style
of the rest of the stops keep it short

[00:14]
two paragraphs and now chat GPT is going
to go out and read the rest of my
document learn how how I talk and how
I've written the rest of these and do
its best to imitate that and so awesome
this this looks great let me introduce
you to one of San Francisco's most
beloved characters you'll have to come
to the tour to find out the rest sounds
like
you so I'm just gonna go ahead and
highlight this to copy and paste it back
into notion and of course you know I
want to iterate from here I'd want to
refine this um but that's just a quick
example of using chat GPT to work with
notion that's awesome I think that it's
really compelling to work with your
documents like this um not just code
like I showed before but your uh written
Pros um this is excellent but it's just
one way to work with the model this sort
of text in text out method and what I'd
like to introduce today is support to
use advanced voice mode with this
feature we're really excited about this

[00:15]
we think that this Paradigm is a really
interesting way to talk with chat GPT
and get insight into your documents or
your code for that matter all right so
we're going to show one of mine in a
second here um when I'm not at open aai
I spend a lot of time as a professional
saxophone player and I've got this
holiday party set list that I'd like
some input on I think chat GPT would be
great about this but again I'm I want to
use the voice to do this is this why
your holiday parties are all so Good by
the way no that's a different okay okay
is it the suits yeah the suits help for
sure yeah all right so uh yeah I want
someone special to really help out with
this um so let's bring up chat GPT again
with the shortcut that I mentioned
earlier which is option shift one and
that brings up our chat bar it's
automatically paired with notes but this
time instead of typing to the model I'm
going to use this new advanced voice
mode support so I'll use this icon in
the bottom right to bring in our special

[00:16]
guest
great hey Santa are you
there yes I'm here how can I help you
today Santa get it is so great to talk
to you listen I've got this holiday set
list that I'm working on and I've got a
couple songs that I'm just not sure
about this one I've got my love to keep
me warm I honestly don't really know
that song very well can you recommend
something else
how about replacing I've got my love to
keep me warm with Frosty the Snowman oh
that's that's a good idea let's see the
Snowman did I get that
right not
quite oh keep
going sure thing so is there anything
else you'd like to know about your
holiday set list I I think Santa was
bored with the copy editing but we can

[00:17]
move on uh let's talk about the last
song of the second set Al Lang Z I mean
that's a little bit dreary I'm hoping
for something more energetic to really
get you and the elves dancing what do
you think what should I replace it
with dick the Halls would be a perfect
replacement it's Jolly festive and sure
to get everyone
dancing Santa I think that's a great
idea I think that song's really going to
slay
I think you know interacting with the
The Voice model like this is such a
great way to talk to your documents and
get live feedback on what you're doing
totally and and uh good news uh right
before we stepped on this live stream
actually we pushed the button to ship
all of the features we just showed off
so um they should be available for you
on your computer just make sure that you
are updated to the latest chaty BT app
for Mac OS awesome so that's day 11 it's
about using the desktop apps to see
understand and automate the work that

[00:18]
you're doing with chat GPT uh this is
coming this is available today as of
what 20 minutes ago on our Mac desktop
apps coming soon to
Windows I love the desktop apps that
they're they're in the background when
you're doing work and then it's a
keyboard shortcut and they're right
there and able to help you do whatever
you're working on so that's day 11 we
have one day left we'll be coming to you
tomorrow morning day 12 we got something
super exciting so don't miss it yeah we
can't wait to get these features out to
you we're really excited but in the
meantime I've got to start practicing
this yeah that Santa recommended all
right let's see
[Music]
w

</details>
