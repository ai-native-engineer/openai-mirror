---
title: "Music Generation | Christine Payne | OpenAI Scholars Demo Day 2018"
channel: openai
url: https://www.youtube.com/watch?v=-tPX_glPDWo
youtube_id: -tPX_glPDWo
published: 2020-07-02
duration: "11:34"
captions: en-orig
---

# Music Generation | Christine Payne | OpenAI Scholars Demo Day 2018

[![Music Generation | Christine Payne | OpenAI Scholars Demo Day 2018](https://img.youtube.com/vi/-tPX_glPDWo/hqdefault.jpg)](https://www.youtube.com/watch?v=-tPX_glPDWo)

<details>
<summary>자막: Music Generation | Christine Payne | OpenAI Scholars Demo Day 2018 (11:34)</summary>

[00:00]
thank you hi I'm Christine Payne
I'm really excited to be here and want
to thank you all for being here as well
and I want to say thank you especially
to opening I for sponsoring us this
summer it really has been an incredible
program so I thought I would dive right
in presentation that's not clicking
sorry with some sample generations so
this summer I was working on training an
lsdm to generate music so this first one
is a sample when I train my LFE M on
classical piano music
[Music]

[00:01]
okay and then when I took the same
neural net and instead of training out
in classical music I trained it on jazz
music and then asked it to generate new
pieces
all right so a nice way to think about
music generation is to think about it as
a language model problem so I won't get
into the details now but for language
modeling we usually use an architecture
maybe something like an LST or a
transformer and we treat it on the task
we give it a prompt sentence and then
our sequence of words and then we ask it
what should the next word be and once
you have a model that's really good at
this it's actually pretty convenient to
turn it into a generator you just take

[00:02]
this word that's predicted feed it back
into the model and then ask it to
predict the next word and so forth and
you can create a text or a piece of
music as long as we'd want the trouble
of course is what we need to do would be
able to translate music into tokens that
we could then feed sequentially into a
model like this so people have tried to
do this in the past but often times
because it's a difficult problem we have
some pretty strong limitations on what
you can do with music
so it's kind of clear how if you had one
note at a time you could ask the machine
at the model to predict the next note
and maybe you come ajan and say like
every time step will have exactly four
nodes and then predict the next set of
four nodes so if you're doing Bach
Corral's that could work really well
we're another limit you might have is
like how many notes you could have so
the lowest note to the highest note but
might be a pretty small range but I was
really curious about could we extend
this and make it more general the
problem is when you start looking at

[00:03]
general music it's really complicated so
you know effectively you can have any
number of notes at any time it could be
any combination of that so I'm defining
here what I call a musical time step and
so ideally we want to tell the model
that at this moment in time we're
playing a D and a B and then you move
forward into a G then you afford an you
clean up and so forth you go and you do
a genus E but here we've run into a
problem right because here we notice
we're gonna try to fit in an extra D but
it's faster than where we were sampling
things and so this causes a problem so
we can imagine sampling
more often but then you know this also
causes other issues because I'm will end
up with lots of moments where nothing's
happening at all and Ella stamps don't
really love it we have basically species
word
you know it's not ideal
otherwise we might build have a method
that's more flexible and has some sort
of more complicated notion of time like
how long to wait until the next next
time set so we have here both our

[00:04]
sampling frequency problem and then the
problem saying noted before how I dunno
range we want and if we want to be
flexible about how many notes we play it
once so to solve these problems I'm
proposing two different kinds of
encodings and I'm calling these the
court bytes encoding and then note wise
encoding and I like to think about these
in sort of parallel to the language
models so chord wise is very similar to
like a word based language model and
know why it is much more the way you do
character by character prediction so for
chord wise is what I'm doing here and
literally I've only found some of them
here but literally for every 88 of the
piano keys I'm putting 0 or 1 for if a
note is being played at that high step
so at the very first moment you can say
they're just the TC simply so we have
the two ones you know you can imagine
this could exploit pretty quickly we
could have you know two to the 88
popsicle possible combinations
fortunately piano music is a lot more

[00:05]
predictable than that we're limited by
how many fingers we have and what sounds
good so I found that in across most of
classical music we had a vocab range
around 55,000 so 55,000 different
combinations of notes the other system
I'm proposing is this note Y system
where here I literally say first it's
going to be C then another C and we're
gonna weight the weight sort marks at
the end of this time weight force except
then you end that first C that's down in
the bottom you play G and then you wait
again so it's sort of it's very much
like a character system might be this is
the men's of being pretty nice it has a
much smaller vocab size because you only
hate
number of notes you have the ends and
the weights and it also has a really
nice feature that you can pretty easily
encode notes that last longer which I
also tried playing around with violin
modeling and there you really need to be

[00:06]
able to have notes that last for a long
time so I took the results of these and
I made a quiz which I invite people to
come across to the table later and try
it out but I have pairs of songs and one
song at the human concludes piece and
one is an AI composed piece and the task
is to guess which is which and
encouragingly enough people are really
bad at this it's you know I was getting
most people around twos threes ones do
you people got Poor's although often
people would email me and be like I'm a
professional musician so in general
people are finding this hard so they
take home from this is that these better
encodings can actually lead to some
really interesting music generation and
i'm just suggesting to encoding here i
think there's probably possibility for
even more interesting combinations I'm
suggesting you know maybe we can look at
ways of including some known music

[00:07]
theory things thirds scales things like
that I tinkered with this a little bit
but I think there's still a lot that can
be done another interesting possibility
is right now I'm training my model on
pretty much all composers at once and
then asking that to generate it would be
really fun to train that and then
fine-tune it on kind of neat quirky
combinations I'm suggesting like what if
you smashed Chopin and jazz together or
something like that I think there could
be some fun artistic possibilities and
lastly I think the big problem both for
this and then in the language model
generation world is how you kind of get
a longer-term structure so the pieces
that are was creating more often really
good for the first 30 seconds and even
like a minute sounded good and then we
started being you know you realize that
there's really no long when going on
here and so ideally you'd love to have
some sort of sense of the big picture
where you are and then
that's sort of immediate index notes
that'll sound good and in the interest

[00:08]
of time I skipped a lot of detail so
I'll open it up to questions now feel
free to hit any of these or whatever
you'd like thank you or you can just let
me up so the question is did I hit any
dead ends things that I tried but just
were not working at all um I would say
that I feel that way a little bit about
the chord wise system like I feel
intuitively that it should work and it
actually turns out to be very good at
memorizing theses so I can I can prompt
it with a little bit of Mozart and then
it'll continue to generate like 45
seconds or a minute of Mozart perfectly
but it has a really hard time moving
away from training set and getting into

[00:09]
kind of interesting new patterns and so
I feel like there should be a way to get
around that but I feel like it's a
little bit of a dead end right now so
that's part of why I moved over to know
Weiss go ahead
oh the question is how many minutes of
training data did I put into it
and I knew someone was gonna ask me it
is it's actually a very large amount I
don't know why in minutes but it's I so
I took data from there's a classical
archives where everyone has just
submitted MIDI recording so they're
pieces so it'll have like the entire set
of show penny to the entire set of
Beethoven sonatas but it's really a
pretty broad range of like all of the
famous classical music pieces so in the
piano said I wasn't finding I was
limited by data when I tried to do
violin and piano duo's then I was more

[00:10]
because there's a much smaller set for
that there's a super interesting
question it's have we done models like
this on birth songs or like whale songs
I imagine I do not know that answer so
it sounds like it could be really
fascinating but but I don't know but
Thank You Sadie one more shake on okay
yeah so the so one thing that I would
really love to see in these pieces but
that I don't see right now is any music
we have an idea of like one one and then

[00:11]
go so you you have a theme or like a
short idea and then you repeat the short
idea and then the third time you do it
it starts that way but then it goes off
into a longer idea and occasionally I
say here but not not regularly enough
that I could say like oh it's really
learned this and I kind of would expect
a good good music model to get that and
that's one of those longer-term
structure things but I'd love to be able
to get all right thank you I'm gonna
pass it up
[Applause]

</details>
