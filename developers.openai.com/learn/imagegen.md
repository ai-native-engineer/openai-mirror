<!-- source: https://developers.openai.com/learn/imagegen/ -->

## Search developer resources

# Image generation

[![Sora, ImageGen, and Codex: The Next Wave of Creative Production](https://cdn.openai.com/devhub/resources/video-1.png)

#### Sora, ImageGen, and Codex: The Next Wave of Creative Production

Panel discussion on combining Sora, ImageGen, and Codex for media creation.

video](https://www.youtube.com/watch?v=70ush8Vknx8)[![4o image generation intro](https://cdn.openai.com/devhub/resources/video-2.png)

<!-- yt-inline:70ush8Vknx8 -->
[![Sora, ImageGen, and Codex: The Next Wave of Creative Production](https://img.youtube.com/vi/70ush8Vknx8/hqdefault.jpg)](https://www.youtube.com/watch?v=70ush8Vknx8)

<details>
<summary>자막: Sora, ImageGen, and Codex: The Next Wave of Creative Production (22:35)</summary>

[00:00]
Great to have you here.
Hi everyone. I'm Chad Nelson. I'm a
creative director here at OpenAI.
Stop. Stop. Stop. We'll keep it casual,
but no, this is going to be a fun talk.
Uh so in my career I've made a lot of
content, films, video games, television
shows and in all my experiences there's
been one common kind of through line
which is how am I going to make it? How
am I going to make this stuff ultimately
like what are my creative workflows that
I need? What are the tools I'm going to
use? And so what happens you start a
project
and you basically look at the tool
landscape that's out there and you say
okay what are the tools I can use?
Hopefully, they're not too generalized
or or worse, too complicated for my
project's needs. And it also doesn't
help that in kind of the landscape
today, these AI tools, I mean, literally

[00:01]
new tools are coming out every single
month.
But kind of made us ask a question. What
if you could actually develop a tool
that was perfect for your individual
project, your creative workflow, and not
have it take months to develop? So
that's something we've been thinking
about here at OpenAI and we found a
project that actually helped us test
this theory. Now a few months ago or I
should say actually it was two weeks ago
uh Native Foreign and Vertigo Films out
of the UK announced a feature film
called Critters. It's an animated film
and their team in London they basically
wanted to power or partner their artists
if you will with our latest open AI
models. And what was interesting about
this, they came to us and said, 'Well,
we want everything to make sure that
it's humanled. Like, we want our artists
to be driving the AI tools itself and
not have them kind of work the other way
around, if you will. So, their goals
were simple.
Let's start with storyboarding. Now,

[00:02]
storyboarding is this pro process where
you sketch out each scene of the film to
ultimately visualize the entire movie.
And when we sat down with their team in
the beginning, they said, "Well, this
process can typically take about a
year." Uh and and the one of the issues
with that is it takes so long that you
really only have a few chances or
iterations to kind of get it right. And
so we thought about that and we said hm
that'd be interesting. What if we could
design a tool for this very specific to
storyboarding?
So we took chat GPT5 and codeex and we
said okay let's design a tool that was
very very focused on storyboarding which
would allow you go from sketches to
something that's more of a highfidelity
render and then potentially even to
final frame and we internally dubbed
this project storyboard and to
demonstrate how it works I'd like to
introduce to you my colleague Olivia
[Applause]
Hi everyone. My name is Olivia Morgan

[00:03]
and I'm a solutions engineer here at
OpenAI.
Now, I want to use Critters as kind of
the backdrop to show you this storyboard
application that we built. And what I
hope you all take away from this today
is not just that we're able to use
codecs to accelerate the build of a
truly custom tool, but that by
thoughtfully exposing the parameters in
our image APIs and our video APIs, um
you could really unlock a lot of
creative freedom.
So I'm going to show you a demo of
storyboard and I'm going to use the
persona of a storyboard artist, but you
can imagine any creative field, right?
somebody in design, somebody in
marketing trying to generate an initial
concept.
So when I land on the storyboard page,
you see this concept of projects. Now to
start a new project, I'm going to go to
the upper right hand corner and we'll
call this project today dev day. And for
the sake of the demo, I'm going to

[00:04]
duplicate from an existing project. Now,
all this is going to do is duplicate my
project setup. And I'll explain more
about the project setup in a little bit.
Uh but that's essentially what's given
me this population of characters,
locations, and props. But you can kind
of see the framework that we're starting
with. On the lefth hand side, we bring
in sk um some sketches and some prompts.
Then we have a list of controls. Um now
these are images that are fed into our
edit endpoint on GPT image one. Um and
helps us control uh the fidelity of
those final outputs.
Now you'll notice here that I can
generate in two different presets. So I
have kind of a turbo preset in the
project setup. We have this set to
generate in black and white sketches.
And then we have a high fidelity preset.
And so the this gives us really our
final renderings if you will. So let's
walk you through an example.
So in the upper leftand corner I'm going
to upload some frames and we'll go to

[00:05]
our swimming critter, our volcano
critter, and our waving critter.
And you'll see when those hit the
storyboard, they're here on the lefth
hand side. Now, I have this critter
swimming with a yellow fish here. And we
need to add a prompt to describe the
sketch. So, I'm going to jump into my
notepad. And I'm just going to grab some
of these prompts that I have.
And we'll describe this one as a white
furry critter swimming underwater as
she's surrounded by bubbles floating up
around her. A yellow and white fish with
scales approaches.
Now I want to select the controls,
right? I want that fidelity in my final
output of what I want my critter to look
like. So here I have a list of
characters. I'm going to select uh this
critter actually for our character. But
if I had a rendering where I wanted to
use Grandpa Critter, I could select him,
too. And then we move on to locations.
So this critter is underwater. Um and
this is just an an image we took with an
iPhone. So, we'll select that underwater

[00:06]
location, but we could also play with a
desert or a forest location or bring
more locations in in our project setup.
Um, then we have this concept of props.
So, if I wanted this critter to be
wearing sunglasses, I'll show you this
in a a later generation. We could bring
that in, too. Now, let's kick off these
generations,
and I'll move on to these last two
images. So, here we've got some critters
in front of a volcano. And I'll grab
that prompt
to describe this sketch. We've got two
furry critters looking at a distant
volcano uh on the other side of a lake.
There are berry bushes on the sides, and
this is going to be early morning light.
So, again, I'm going to use that initial
critter. For the location, I don't need
to bring in an asset. We described it in
our prompt, and we'll kick off those
generations as well. And then for this
last guy, I'm actually going to show you
an example of bringing in a prompt, a
prop.
And we'll describe this sketch as

[00:07]
a white furry critter waving hello
wearing sunglasses. So you'll see in the
image he's not, but we'll bring in that
prop for it. So here's our first
critter, and we'll bring in those props,
uh, those crystal sunglasses as a prop.
So this will be what he's wearing in the
final generation.
All right. Now, before we look at these
generations, I want to take you through
the project setup.
Um, so this is what was duplicated when
I initially spun up the project. And
when we were working with the creative
team in London, they mentioned that this
part of the image generation was really
important, the ability to set an overall
style in their storyboard. So, you'll
notice up here at the top, we have that
style guide where we can kind of set the
aesthetic description that's applied to
every generation. In our case, we want
the sketch uh to uh we want to turn the
sketch of a storyboard frame into a
detailed scene. And we want to maintain
the position and the composition of the
initial sketch.
Now, for the turbo generation prompt, uh
we just want a storyboard style black
and white marker and ink rendering, no

[00:08]
color. And then for that highfidelity
generation prompt, this is a full color
highly realistic movie scene, 35mm
photography.
Now, speaking of controls or assets, um,
down here at the bottom is where we can
manage our locations, our characters,
and our props.
Now, for each image that we bring in, we
can add a description. Um, for the
characters, we actually added the
ability for GPT5 to generate the
description for us. We were kind of
playing around with these controls. So,
I'll show you an example. We'll bring in
our yellow critter. And you'll notice uh
very quickly it's fed into GPT5 and we
get a short description, a small fluffy
bright yellow critter with a round
chubby body covered in software.
Now again, these are all fed into the
prompt for that final image generation.
So both the text and those images. Um
and this is important because that GPT
image one model that we have has a um

[00:09]
high input fidelity parameter that you
can turn on and you'll kind of see how
this comes to play here in a second.
Now, the last thing I want to touch on
is this history tab. Um, when working
with the creative team in London, they
mentioned that having this concept of a
history tab was important. They wanted
to be able to see the initial sketch,
the generated images, whether or not we
were referencing certain characters,
props or locations, and then which
prompt went with the image that was
generated. And we gave them on the
righthand corner the ability to export
this all in a CSV so that they have full
auditability on all of these storyboards
that they're creating.
Now, let's go back to the storyboard
frame and see what was generated. So,
you'll remember we had that initial
sketch of the the critter underwater.
And we've got our our black and white
frames now. Um, so we have four
different presets because when you're
working with these image models, you
know, there's a little bit of creative
freedom that is to be had with these
models. And so, it just gives the artist
the ability to choose the best rendering

[00:10]
that fits the vision. Um, I can confirm
for download here in the uh bottom right
hand corner. And um, I want to get some
participation from the audience. I'm
going to look at these last four and you
cheer for me which one you like the
best. Do we like this generation? We
like this generation or this generation.
>> First one. Okay.
Okay. So, we got our our confirmed
generations. I'll go through these last
two just very quickly. Um, we now have
also our critters in front of the
volcano. So, if I can get a shout out
which one we like best, I'll confirm
that one for download.
>> I heard two.
Um, and then here at the bottom, we've
got an example of those generations with
the glasses. So, we're still waiting for
the black and white sketch, but we got
the full color generations. I kind of
like either two or four, so we're going
to go with number two. But why this is
important is when you're working with uh
you know storyboarding or you're

[00:11]
generating initial sketches a lot of
times in production you're not just
working with one image you have hundreds
of images and so the ability to do this
in bulk stage it for download and then
move it into your other creative tools
is a really powerful concept.
And when we were working with the
creative uh team in London, what we
found really fascinating is that um they
started utilizing this storyboard
concept for many different aspects
including things like environmental
design. So you'll see here uh the sketch
of an initial environment and and
storyboard's final rendering of it. uh
but also things like character design
where we're throwing an initial sketch
of the character into storyboard and
we're using storyboard to render out all
of the final details. Um now this really
opened our eyes to what a tool like this
uh could be used for in uh you know
larger enterprise applications. So
imagine you are an athleisure brand and
you're preparing for a seasonal launch
or you're an automotive company and

[00:12]
you're building a new campaign.
Um and so that's really where storyboard
comes in. turns these initial concepts
into stunning production style shots so
you can move fast and kind of stay
confident that your first sketch to
final frame is exactly how you want it.
And with the new uh Sora 2 API, we are
really excited because what this means
now for our storyboard tool is we can go
from initial sketch to a beautiful image
now to full motion. Um, and I am so
excited for you all to get your hands on
this. I think what you'll find in Sora 2
is that the motion understanding, the
physics, the ability to guide the
details through prompts and images um is
is truly truly impressive. And so you
can actually then go from visuals or
images like this
to uh full motion and sound like this.
Hey there, shiny friend. You like to

[00:13]
dance, huh? You're beautiful.
[Applause]
So, that's a little teaser of our Sora 2
API. Um, I'm so excited for you all to
get your hands on it. I'm certainly
excited to continue to build this into
storyboard. Um, and speaking of
building, next I want to bring up my
colleague Allison to actually walk you
through how we built Storyboard. But
before I bring her up here, um, Chad,
are you still around?
Um, what? I'm sorry.
>> I wanted to bring you back up here. Um,
do you think you could sketch something
that we could actually throw into
storyboard so we can actually show them
how we've been working?
>> Uh, I think you might have given me a
challenge here. I need to get the iPad.
>> Okay.
>> Hold on a second. I'll be right back.
Okay.
>> But, uh, what do you want me to draw?
>> So, I'm thinking we have the swimming
critter. We got the volcanoes. What
about the cave scene? Could you do like
a critter in a cave?
>> I got it. Let me get the iPad. Oh, I
found it. Wow. Oh, look at that. Look at

[00:14]
that. Okay. Hopefully this cord's long
enough.
>> Um, how many have like like two, three,
cuz I'm not I'm just I'm a creative
director, not a storyboard artist, but
I'll I'll try.
>> We'll give you a you got a few minutes.
Um, so while he sketches, I want to
bring up my colleague Allison to walk
you through how we built storyboard.
[Applause]
>> Thanks, Olivia. Hi, everyone. I'm
Allison August, a solutions engineering
leader at OpenAI. Now, while Chad is
going to be furiously drawing over
there, I'm going to take a few minutes
to explain how we built Storyboard in 48
hours and how it's accelerated the
design process for Critters.
So, our team has worked with many
different creatives across the industry,
from some of the largest media companies
to small teams who really need to move
fast. And what we heard was clear. They
want more control over the creative
process with AI. Now, with a lot of

[00:15]
tools today, you send a text prompt for
an image and you get an output that can
vary actually quite far from what you
want.
But creatives have a vision of how a
shot should play out in their head. They
want to be able to visualize the scene
and the style to get an output that
matches their concept rather than go
straight to final generation. And in
fact, Chad, that's your drawing there on
the right, right? It's looking pretty
good. judgment free zone.
>> It looks great, Chad. Um, so with
Storyboard, our goal was really to
create a workflow that allows creatives
to follow a process that gives them this
level of control and fidelity to bring
their light their shots to life with AI.
So, at an internal company hackathon
back in August, I worked with Olivia and
three other solutions engineers to try
to solve this problem. We had crossed
paths with the critters team a few days
before and thought we could work with
them as a thought partner to ideulate
towards a solution during this hackathon
and we built a working prototype in just
two days.

[00:16]
So to build this MVP quickly we relied
on codec cli and cursor powered by GPT5.
We built the app in Nex.js JS with
superbase as the back end which manages
project state images and authentication
and everything is deployed on Verscell.
Now on Verscell we run functions that
coordinate GPT5 image gen and now the
new SOR 2 API and for every request we
generate four image variations with GPT
image one giving creatives the option to
select the image that most closely
matches their vision. Now, as Olivia
mentioned a little earlier, GPT5 is also
embedded throughout the application to
improve our generated results from
refining an artist sketch description to
automatically generating rich character
text that drives more detailed image
outputs.
So, let's take a peek at one of our
original concepts for Storyboard. So, we
started with an interface where you
could upload one sketch at a time, add a

[00:17]
prompt, and select a character, or in
this case, a very cute little critter.
It was pretty basic. There was no
project setup, no generation history,
and you couldn't even upload sketches in
bulk.
Now, as we worked, we realized that the
concept of a project where you can bulk
upload sketches from a scene and render
different types of outputs based on a
project level configuration would be so
much more helpful for creatives. So,
here's a mockup of what we actually sent
over to the Critters team and looks a
lot more similar to what you saw Olivia
demo a little bit earlier.
So when we sent this over, the Critters
team started testing the app immediately
and they had a lot of really valuable
feedback from basic asks like adding
file name visibility to more complex
requests like adding the options to
control inputs for props and locations.
Now, initially Olivia and I hadn't
planned to make any changes after our
hackathon, but when we saw the requests
and how valuable some of these changes
could be for the team, we decided to
test Codex, our coding agent, and the

[00:18]
newest GPT5 codeex model.
So, we would send tasks to Codeex in
between meetings. We really easily
reviewed and merged PRs into production,
which Codex even allowed us to do from
our phones. Right, Olivia?
>> Yep. Now, right now you're seeing a
screenshot of my actual codeex workspace
and some of the various tasks that we
shipped. We started with some quick wins
like adding small elements to the UI,
but soon found that it actually excelled
with more complex tasks like compiling
our generation prompt based on assets
uploaded at both the project and the
sketch level.
Now, in my experience, once we built the
foundation for the application and
designed what we thought about the base
UI, Codex was really incredible at
adding the additional features and
actually troubleshooting what we needed
in record time. And every day, we
completed nearly 10 feature requests
from the Critters team, and they were
simply blown away at how quickly we ship
those improvements.
All right, Chad, this is my last slide,
so I hope you're wrapping it up over
there.
>> I'm Yes, I think we'll be ready.

[00:19]
>> I'm sure it will be great.
So to summarize on my piece here, we
partnered really closely with the
Critters team and stayed in a tight
feedback loop, which meant that with
help from Codeex, we were able to
prototype faster than we ever have
before and incorporate feedback on a
daily basis. Typically, this kind of
loop can truly take anywhere from one to
two weeks. But with Codeex, we brought
our ideation time truly down to a day.
Now, the final storyboard tool helps the
Critters team visualize thousands of
sketches across different scenes in a
matter of days. A process that normally
would have taken months. All right,
Chad, pencil's down. Can we take a look
at what you drew?
>> Yeah. So, okay.
It's this little sketch here.
>> Beautiful.
>> Uh,
you said a ca entering a cave. I gave it
a little torch, like a little, you know,
it's a dark cave.
>> So, yeah. I I'm very curious to see what
it did with it.
>> All right, so I've got the generations.

[00:20]
They just came in just in time. Um,
we've got Chad's sketch. Uh, I gave it a
little description, the front view of a
furry critter who's entering a dark
cave. We selected, you know, our critter
character as that asset that we wanted
to feed into our prop uh into our
prompt. And then we've got our black and
white generations of the adventurous
critter and our final images here that
we can stage to move into.
>> I love the torch. The torch works really
well. This is amazing. I actually really
love the fact that I can just take a
sketch like in barely what two minutes
and get it um visualized this way. And I
think that's what's been so amazing
about seeing how their team in London is
working with the tools. Uh, now we
mentioned Sor 2 and I think we wanted to
show I mean obviously I love the fish
but I think Sor 2 made that audio. The
Critters team in London put together a
little demonstration. Now they've had
access to the tool about a I don't know
a few days u when we announced it last

[00:21]
week. So let's take a look at something
they put together to show us an example
of what it can do there. Give it a quick
comb. PERFECT.
>> PICTURES UP. CAMERA STAND BY and you
sorted. Good. Camera's rolling and ready
on the big land.
>> Have the antenna tidy. Thank you.
>> All right, EVERYONE. SET
>> ROLLING ACTION.
>> HI THERE. Uh um what's my line again?
Blast it.
>> I love it. I love it.
>> I think Sora too. I mean the visual
quality is amazing. I love the sound. I
mean all the voices and all the ambient
and the music. It's amazing. But I think
what's so exciting about this time is
that we're seeing this period where
artists and developers can now work more
closely than ever before. And we've seen
what happens when you take artists and
couple them with AI. I mean that
produces, you know, amazing work. But
now how they're producing that work can
be truly transformed with these custom
tools. So I think Critters has become an
ex exceptional example of this. Uh I

[00:22]
can't wait to see what they build next
with the tools. Uh but when I look out
in this room, I see a whole room full of
developers. I mean, what excites us is
what you all will build. What creative
tools might you bring to the industry
and to artists to let them explore their
imaginations? So, with that, I'll say on
behalf of uh Olivia and Allison uh and
myself, thank you so much for coming.
Have a wonderful dev day. Thanks again.
Thank you.

</details>


#### 4o image generation intro

Video introduction to 4o model image generation capabilities.

video](https://www.youtube.com/watch?v=2f3K43FHRKo)[![Image generation guide](https://cdn.openai.com/devhub/resources/guide-1.png)

<!-- yt-inline:2f3K43FHRKo -->
[![4o Image Generation in ChatGPT and Sora](https://img.youtube.com/vi/2f3K43FHRKo/hqdefault.jpg)](https://www.youtube.com/watch?v=2f3K43FHRKo)

<details>
<summary>자막: 4o Image Generation in ChatGPT and Sora (16:07)</summary>

[00:00]
Good morning everybody. Today we have
one of the most fun cool things we have
ever launched. People have been waiting
this waiting for this for a long time.
Uh we know we've made you wait but we
think it's really worth it and we think
you're going to love it. We are
launching native images in Chad GBT.
Image generation has been around for a
while. In fact, one of the first things
that we ever were known for was the
original dolly. But image generation has
been largely a novelty. uh you've been
able to make some cool art with it and
people have done amazing things but it
has not had the power to be really
useful in a wide variety of ways. The
thing that we're going to launch today
um is native image generation in our 40
model and it's such a huge step forward
that the best way to uh the best way to
explain it to you is just to show it
which we'll do very soon. Um but this is
this is really something that we have
been excited about bringing to the world
for a long time. We think that if we can
uh offer image generation like this,
creatives, educators, small business
owners, students, way more will be able
to use this and do all kinds of new

[00:01]
things with AI that they couldn't
before. And um really the best thing to
do is just to show it to you. So I'd
like to introduce Gabe who is the lead
researcher uh and really the primary
driver of this product. And we will I'll
hand it over. Hey, so I'm Gabe uh lead
researcher. Hey, I'm Proful. I'm the
head of multimodal research. So, okay,
I'm going to jump right in with uh with
a demo. And uh the reason I'm starting
off with a demo is because I'm also
using these demos as my speaker notes.
So, uh it's a bit handy. Now, um two
years ago when we first started this
project, uh we were interested in sort
of like uh maybe a scientific question
about what native support for image
generation would look like in a model as
powerful as GBD4. We didn't know the
answer to that question. But a year
later when the model was done training,
we saw really exciting signs of life.
So, you know, we featured this in a
forum blog post if some of you will
remember. And um, you know, we saw that

[00:02]
the model could render paragraphs of
text, for example, you could combine
images in really very interesting and
novel ways. And I think we spent a lot
of time just playing with this model and
I felt that sense of like joy and
excitement. You know, I haven't felt for
a very long time, maybe even since GPD2.
I haven't either. This was one of those
really wow moments. It was a wow moment,
but that model was still a bit rough
around the edges. So, you know, it's um
you know, it it it it you know,
sometimes made typos. It you know, it
was it it was kind of unreliable, I
would say. And um so over the last year,
I've been refining this model to make it
more accessible and more uh user
friendly to the average person. And so,
um okay, the image is generating as you
can see. And um
um let me see. So it seems to have
gotten all the text. I don't see any
typos, which is good. Okay, it's still
amazing to me to see uh and you know,

[00:03]
image generation with perfect text. It
shouldn't be that impressive, but
somehow we've been waiting for this for
so long, and every time it happens, it's
like, wow, that's so cool. Yeah. and and
the number of things that like this
image had to get right in the
instructions like the you know what you
want focused on not like the that it
should be a point of view image and
where we are and then sort of to get you
know having the text like like that's
just uh this is still amazing to me.
Yeah. And point of view images are
actually really hard to do and this kind
of looks like what we see right now. It
looks like you were just taking it.
Yeah. All right. Well, I am going to
begin my demo by taking a selfie of all
of us. So
give me a nice expression.
Yeah. Okay. And I'm going to ask chat
GPT to make it into an anime frame.
So in this case, it's not just getting
the context of my text prompt, but it's
also getting this image. And it can use
both of these to produce a really nice
image for us. And this is possible
because we train for as an omniodel. So
you know, it's a model of not just
language, but images, audio, all

[00:04]
modalities in and out. It understands
them. It can generate them and it can
you know seamlessly work across these
things and we have spent a lot of effort
to you know make useful products like
first advanced voice mode where audio
just works seamlessly and now this where
images just work seamlessly across the
board. It is so cool that we're finally
getting towards this truly integrated
multimodal model that just does
everything. Yeah. And in this case, you
know, it gives the user a lot more
control because, you know, I might want
a specific style or I might want to use
a specific previous image I have or, you
know, a design palette or something. And
they can provide all of this context to
chat GPT. You can just use all of this
and, you know, produce the thing you
want. It becomes more controllable. Oh,
okay. All right. We can, you know,
you're already seeing the sky behind us,
the plants. By the way, this goes live
today in Chachi PT and Sora. Um, I think
we're already started. So, if you also
want to make an anime version of
yourself, you can you can now do that.
Yeah, I think it's already out to all
pro and uh plus should be done pretty
soon. Amazing. Nice. It'll be available

[00:05]
to free users, too.
I I see I have my little beard there. I
see your expressions and my perfect the
hand sign. And my hand sign, too. Yeah.
Nice. What should we do next with this?
Can we make a meme out of it? Oo, make
it into a meme. That's on game speaker
notes. What do you want to um you know
one of the like common memes inside of
OpenAI is feel the AGI. I have no idea
what AI will think about that but let's
try it. I do feel the AGI.
Yeah. And in this case, right, that
animating is so good. Yeah. Um and in
this case, you know, the model is seeing
all of the past context as well. And you
know, it uses all of its knowledge of,
you know, language and beams and
everything to give us a new rendition.
And this multi-turn nature makes it even
more useful to people, right? Like I can
ask for any edit I want. If it gets it
wrong, I can just be like, "Hey, you
know, fix that thing." I think that, you
know, is taking us into a direction of
making these more like tools, not toys

[00:06]
for people. And I think I'm really
excited by that. Speaking of memes, how
much like how much do you think for
knows about like common internet memes
in general? Like if we had picked I I
think it knows a lot. And in fact, when
we first put this out to, you know,
people inside Open Air, most of what we
got was memes from people. Maybe Gabe
can tell you more about that. Yeah, I
mean you know uh memes were like one of
the number one use cases for this model
in our internal version and yeah I was
just thinking about you know memes and
why this use case you know kind of
struck a chord with the company and I
what I realized is that you know as in
the last nine months as I've been
working on this model uh I've been doing
this kind of like meditative exercise
where I sort of like uh look at all the
images around me and I realized I'm just
surrounded by you know hundreds of
images maybe a day and you know all
these images you know Not necessarily
the most aesthetic or beautiful images,
but they were all created with intent.
They were all, you know, like memes.
They were all created to, you know, to
persuade, to inform, to educate. These
are the workhorse images that, you know,

[00:07]
comprise our everyday life. And what I'm
very excited is that I'll be able to be
giving this power to create workhouse
images to everyone in the world in Chbt.
Speaking of this power, um we are giving
a much higher degree of creative
expression and creative freedom than we
normally do. Um and so what we'd like is
for the model to not be offensive if you
don't want it to be, but if you want it
to be within reason, really let people
create what they need and what they want
to what they want. And uh I, you know,
we may not get the line there perfectly
on day one, but we think given what Gabe
just said, we want to lean pretty far
into creative freedom and let people get
maximum utility out of this model. and
uh you know we're excited to see what
people will do with it. Yeah, me too.
Let's look at the meme we got.
That's great.
Um okay, so thank you guys very much and
we're going to welcome a few other
research and product people to show some
more stuff unless either of you have
anything else. No, thanks. Thank you.

[00:08]
Okay. So, in addition to building uh you
know all the great research that went
into this, we really wanted to work hard
to make it a great product experience as
well. Um and so if my colleagues want to
introduce themselves, maybe starting
with Alan, we will then show you a few
more things. Hi, I'm Alan and I'm a
research scientist at OpenAI. Hi, my
name is Bench. I'm an engineer on ch.
Hi, my name is Lou. I'm a research
scientist at OpenAI.
So, uh, as our models get more capable,
uh, their knowledge of the world is
deepening. Uh, but so far, they've
really only been able to express
themselves in either text or code. And I
think what's really exciting about this
release is that now these models can
actually visualize what they know and
externalize it in a visual way. So, the
prompt that I'm going to try is make a
collable page of manga describing the
theory of relativity. And just for fun,
we'll ask it to add some humor. How well
do you find that the model understands
like visual humor versus just funny
text? I think that given that this

[00:09]
prompt is like so vague, it'll be
interesting to see, you know, what kind
of wild cardy stuff uh the model comes
up with. Um this is really just like it
leveraging the world knowledge that it
has, writing maybe an extended version
of the prompt and then giving us a nice
image. uh but you know if you have a
much more detailed sense of the kind of
story that you want to convey in this
kind of thing like a manga or an image
or in general you can definitely do
that. This model is very good at
following instructions and in the blog
post that we just put out there's a lot
of nice examples of uh of how you can do
exactly that. Um by the way images are
much slower than previous uh our
previous image generation thing but like
unbelievably better. We think it's super
super worth the wait. Uh we also will be
able to make it faster over time. Um but
you know it's just it's like quite the
uh the ratio of quality to time we think
is is already great. Yeah. Um and it
looks like it's given us not only some
English but a different language here.
But yeah, I think in general um we're

[00:10]
hoping that this model's ability to not
only generate images but also blend in
precise text in the right ways uh makes
it not only a tool for imagination but
also for for learning and for
communication. It did add some humor.
Yeah. Yeah. I like the layout. Yeah,
definitely quite colorful on the
software. That's beautiful.
Thanks, Alan. So, Alan just showed us
how much this model can shine in
professional and educational
environments. But what I love the most
about this model is how accessible it is
to everyone. For someone like me who
don't have professional artistic skills,
but still enjoys expressing my
creativity. To show you what I meant,
I've prepared something special. Let's
kick it off. Um, so I was inspired by
this trading card in my hand that I got
from our Sora launch and I thought we it
will be really cool if we can design a
new one in the same style for photo
image generation. So I took a photo of
it in the morning. This is what it looks
like. But instead of having the giant
cat king here, I would like to have my

[00:11]
dog Sani to be the main character. And
this is a photo of my dog. He's cute.
Um, and I've also included a couple
details that I would like to see on the
card, including the name of the model,
the year, and some ability where like I
could highlight and also the weight and
height for Sanji. And let's see what the
model comes up with. Why is the giant
cat king Visora? I have no idea, but I
feel the the trading card Dora was
designed by some professional designer.
So, it would be amazing if we can
actually use our model to generate that.
Yeah, I think our model has come a long
way in terms of just very precise text
rendering. So, it'll be super cool to
see how well it does with this detailed
instruction. Can I see the original
card? Yes.
Oh, it's very nice.
It looks like it's already reviewed. We
should do these for every launch. These
are cool. Yeah.
I guess now we can make them with a

[00:12]
machine. Yeah, we should definitely do
that.
Yeah. And yeah, Sanji is snowboarding,
which is something I've never seen him
doing in real life, but it'll be cool.
The text is also very crisp. Yes. Yes.
And got it got all the stats correct.
That's amazing. Um, thank you for
letting me share this little creative
moment with you. And now I'm excited to
pass it on to Lou to show you more
innovative ways of using our product.
Yeah, sure. I'm very happy to share that
with everyone today. So, we've seen the
generation from Alan and Monta. So today
I'm going to do something very special
here. So I'm going to make a memorable
coin based on the generations from these
two and also another two pictures that
is in our background. So I'm going to
first copy the pictures from
Alan and also the pictures from
Mchao and the rest of the two are the
background we show here in the demo.
So I would like to also use a special

[00:13]
hex code here. So as you can see this
special hex code is a spring color
because for and this launch both
launched in spring. So I would like to
it to be a unique color for us and also
I would like to include the text for
image gen and today's date on this
memorial cone so we can make a souvenir
for us for today. So you can see this
model is trained in non auto reggressive
way. So it is able to understand both
text and multiple images in context and
seamlessly render it in a very
harmonious way in a coin. So it's able
to can you imagine how this coin will
look like based on this not easily from
that but I'm excited to see. Yeah. Yeah.
Me too. Me too. That's what I'm thinking
of also. So we are seeing here. So we
have the fur image gen and we have the
bear that is the artistic bear there.
the radio there and also Alan's
manga and I was still amazing Sanji.

[00:14]
That's so cool. Cool. That's very cool.
I want one of those. Yes, I agree. So
now I'm I'm going to make it a
transparency background because we
really wanted this coin to be printed
out so we can have this coin physically
for us. So as you can see the model not
only can understand context in one turn
it is also understanding the context
across multiple terms in context. So
from today we can just chat to chat GBT
in a more visual way and uh this is just
a very simple example. I make a
transparency background. You can also
talk to the model. For example, imagine
how will this coin look like on the back
side or we can make a unique color for
Alan and Munchchow and me to have a
different unique color for each one. And
other than making the background
transparent, how good will it be at
keeping the actual coin itself
consistent between the two? Yeah, it's
very good at keeping the editing

[00:15]
consistent. So that is also to see you
can use CHP from today to do image
editing and image refinement in Chad and
using a very chatty
language. Cool. Here so we see the coin
here and it's in transparent background
now and it's keeping the consistency
between the previous generation. That's
awesome. Yeah, it's very cool.
Well, we're so excited to get this out
to the world. Uh, it goes live today in
Chacht and Sora. It will come to the API
soon. We we really think this is a huge
step forward in what AI models are
capable of doing visually and we cannot
wait to see what you all will create.
Thank you very much. And again,
congrats. Cheers. Thank you. Thank you.
[Music]

</details>


#### Image generation guide

Guide to generating images using OpenAI models.

guide](https://platform.openai.com/docs/guides/image-generation)
