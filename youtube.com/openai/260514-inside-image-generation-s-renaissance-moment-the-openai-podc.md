---
title: "Inside image generation’s Renaissance moment — the OpenAI Podcast Ep. 19"
channel: openai
url: https://www.youtube.com/watch?v=bH2nP-aCFjk
youtube_id: bH2nP-aCFjk
published: 2026-05-14
duration: "29:23"
captions: en
---

# Inside image generation’s Renaissance moment — the OpenAI Podcast Ep. 19

[![Inside image generation’s Renaissance moment — the OpenAI Podcast Ep. 19](https://img.youtube.com/vi/bH2nP-aCFjk/hqdefault.jpg)](https://www.youtube.com/watch?v=bH2nP-aCFjk)

<details>
<summary>자막: Inside image generation’s Renaissance moment — the OpenAI Podcast Ep. 19 (29:23)</summary>

[00:00]
Hello, I'm Andrew Mayne, and this is the
OpenAI Podcast.
On today's episode, we're talking about
Images 2.0 with researcher Kenji
Hata and product lead Adele Li.
They'll discuss why the new model
represents such a major leap forward, the
evaluations that mattered most during
development, and what people are
creating with it now that it's widely
available.
If DALL-E was the Stone Ages, ImageGen 2.0
is the Renaissance.
It's not only great artistically and
aesthetically,
but it also incorporates science, art,
architecture, all in one image.
We looked at it and we're like, all right,
this is better than ImageGen 1.
Adele, tell me a little bit about how you
became a product manager here.
So I joined OpenAI a little over two years
ago.
And before OpenAI, I was an investor my
entire career.
Oh, wow.
So I was in private equity and spent three
years at Redpoint
Ventures investing in AI and software
companies.
And when I first joined OpenAI, it was for
a completely different role.
I was thinking about how do we build out
our data and compute
infrastructure. And over time, made my way
over to the product side.

[00:01]
And for the last six months, have been
working on ImageGen.
It's interesting how you style yourself
going from one role, then finding
yourself into this space here, which is
kind of cool to think about the idea
that you have this sort of ability to be
useful in different ways.
Absolutely. And I think the role of a
product manager is just to do the job
that needs to be done, no matter what it
is.
And for ImageGen in particular, it's been
really awesome to flex a lot of
different muscles when it comes to
building products, working with
researchers like Kenji, but also thinking
about what is the gap in the
market today that we want to fill and what
is the opportunity that we want
to grasp here. It's not the same market
that it was a year ago when we
first released ImageGen 1.0.
Now it's a very different landscape.
There are multiple image generation makers
out there.
And ChatGPT is a very different company
and product itself too.
And so really thinking about the evolution
of ImageGen and its role within
ChatGPT has been really, really exciting
to me.
Kenji, how did you end up working on
images?

[00:02]
Actually, like when I first started at
OpenAI, I also started about two
years ago. I was working on like some
random audio project initially.
It was my first project. And then at the
time, I just found my way just
working on helping them work on ImageGen
1.0 prior to the launch.
And so gradually I moved more and more
onto the project and then I became
full time on it, basically.
What has the reception been like right now
for
the model?
In the last two weeks since we launched
the model, usage is up
more than 50%. More than 1.5 billion
images are generated every week on
ChatGPT. And we've seen viral trends
emerge across the world.
All the way from trends in Asia for color
analysis and stickers to US where
crayon and scribble are going viral.
but also a lot of people exploring
emergent use cases.
And I think it shows the dynamic range of
the model, but also how people are
able to visually grasp the advancement of
the model almost immediately.

[00:03]
I think the visual communication reaction
that we've seen from our users for
them to say, hey, this is the best,
highest fidelity, highest quality in a
static model that we've seen has been
really awesome.
This felt like a really big shift, almost
worthy of me not even being images
too, but almost like just a new paradigm
because just the capabilities are
through the roof. What made that possible?
When we started working on this project, I
think we sat down and we
discussed what is the step change of
capability and use cases that we wanted
to build towards.
And we believe that image generation has
the ability to do so much more than
what it does today. you could distill
every single output or visual content
that you see today into an image.
And so that was the mandate that we sought
out to improve.
And with this 2.0 model, we've improved on
various different dimensions.

[00:04]
One is text rendering. The ability for
text on a page is so much better
fidelity. The language and words actually
make sense in their actual words.
The second of all is multilingual.
So we've really focused on making this
model work in various different
languages. And we're already seeing that
people across the world in Asia and
Europe are really resonating with these
advancements.
The third is photorealism. I think we
really saw a lot of feedback from our
previous models that the output wasn't
very realistic or altered their face
or their bodies. And so one of our
mandates was how do we actually make the
image feel like more like yourself?
And so all the things that you think that
the model knows, it does because
it has imbued the knowledge of the world
into its conscience and is able to
visually communicate that back to you as a
user.
And so putting that all together, I think
we really get a state-of-the-art
image generation model that is the best
aesthetic model out there on the

[00:05]
market right now. That really represents a
new paradigm for image
generation, which is a huge part of, I
think, AI progress at large.
that we have an opportunity to work on
here.
We often listen back, listen to feedback
on social media too.
So we kind of just take all these things
and basically are just aware of it
and try to make sure that they're
mitigated or completely fixed in some
cases in the next iteration.
What kind of use cases are you seeing?
What are you seeing people do with this
now?
I think one that's particularly
close to like the research team as a
general is like infographics, text.
I think text in images is like so much
better nowadays.
So I think it just opens up a lot more
productive use cases.
And from the research side, we kind of
think image generation used to
always be about fun and maybe unproductive
things.
But now we're really seeing steps forward
into productivity and image
generation for any type of use case that
you can imagine it for.

[00:06]
So you mentioned text. I remember the
early models, no disrespect to
chimpanzees, but getting to dispel like
OpenAI even looked like a chimp did
it. And then now I'm looking at pages of
text and finely detailed stuff.
And I know that as models get smarter,
variable binding, the ability to put
things next to each other improves.
But this was just a big improvement.
Yeah. But I don't think it's completely
unexpected.
I think you see a lot of growth in
between.
Well, first you see between DALL-E 3 and
GPT Image 1.
If you ask for a grid of random objects,
you go from maybe
like 5 to 8 in DALL-E 3 to maybe around 16
in Images 1.
And then with 1.5, we went to about 25 to
36 consistently.
And I think now we could probably do over
100.
I think this is like a test that we might
do internally.
It's just we just ask GPT, give me a list
of 100 random objects.

[00:07]
And then we just send that to our image
generator and see how many are
correct. And usually, you know, it'll get
almost all 100 correct.
And that's, but you see the constant
growth over time.
So I don't think it's like completely
unexpected. It's just a steady pace.
That was a test I used to use for like the
really old models back with
like Ada, Babbage, and Curie, like list
100 science fiction books.
And then some of them would get, by the
time it got to like 22, we'd
just start repeating stuff. So we realize
the model reached the end of it.
So we've seen stuff too, like 360, 360
degree panoramas.
How did that happen?
Yeah, that really came from the emerging
capability of
the model, which is the ability to render
images in any aspect ratio.
We discovered that people were generating
really long, amazing panoramics,
skinny bookmarks as well. And one of the
cool capabilities of the model is
that not only were you able to generate
images in this panoramic aspect
ratio, but you could also render images in
the style of 360.

[00:08]
And we saw that it was really fun to
actually view these images in a 360
world itself. And so that was a really fun
feature that we ended up adding
into the product and it's available on
ChatGPT on web and mobile right now.
First thing I did was I made a version of
dogs playing poker.
Put that in there so you could sit there
like you're one of the dogs looking
around in there, which was not something I
expected, but it's fun.
Yeah. I mean, it's really awesome to see
how people are exploring new use
cases and fun things that they're creating
with the model, even far beyond
what we expected users to be using it for.
I think when we were designing the model,
we were really deliberate in
understanding what people really wanted to
see from image generation.
There was a lot of latent demand in image
generation.
People were mostly using it for personal
use cases, but we definitely saw a
lot of inklings of people wanting to push
the model in certain directions
that the model wasn't good at. So text
rendering was definitely one of those
dimensions that we really wanted to
improve on.
Multilingual is another. And I think world
understanding generally is so

[00:09]
much better in this model. And that
typically means that now people online
are sharing a bunch of examples of them
creating image done for all
different kinds of use cases that we
didn't even think existed out there.
So I think the model's understanding of
aesthetic beauty across
multiple different outputs, whether that
it's like a fun meme, an image for
a five-year-old versus a professional
consulting deck.
The expansion of opportunity and outputs
has been amazing to see in this
latest model. It's funny too how one of
the things that was trending
was taking popular images or photos of
people and then having the model make
like kind of janky looking Microsoft Paint
versions of that.
Yes.
And did you think that was something you
would see was that people are
going to use this incredibly capable tool
to then go make, you know, these
silly looking things?
Yeah, it's funny because it takes a lot of
intelligence to actually create something
that is imperfect.
That's what I tell people all the time.
Yeah.

[00:10]
And it's definitely very interesting in
the viral trends that we're seeing
online right now. One thing that I think
people are really striving for is
authenticity, imperfection, nostalgia.
We're seeing that in the Microsoft Paint
prompt, crayons, all different
kinds of generations that people are
creating.
And that really feels like the theme of
consumers is they want to interact
with AI in a very authentic, imperfect
way.
They want to show their imperfections and
use AI to help make them look
good, but also show a more fun and goofy
side of themselves.
And I think that's self-expression via AI
is something that we're really
excited about. And, you know, I think it's
really part of our mission as a
company to make it easier for people to
learn more and distribute that
intelligence, but also letting them
express a version of themselves that
maybe wasn't possible before.
Kenji, was there a moment with this model
where you're saying to yourself,
wow, I think this is ready to go?
You know, as it's training, we take a
checkpoint and then we just sample

[00:11]
from it, right? And just see, okay, how
good is this thing?
And I think we just sampled a model, an
image, and we looked at it and
we're like, all right, this is better than
ImageGen 1.
We were just like, okay. I remember
watching the iteration of one of the
early versions of DALL-E and how at first
it was sort of the wispy sort of
weird sort of the tendril sort of thing
and talking to one of the
researchers like, is that going to go
away?
It's like, I think two, probably two runs
away from that.
And then just like that, the ability to
predict that was amazing to me.
And all of a sudden everything got crisp
and clear. Yeah.
And then also like looking at, you know,
years ago I'd played with like, you
know, GANS and like doing those things.
You have to squint and say, I think it's a
pickup truck or something like
that. Yeah. So it's interesting what you
see is you say, okay, this just all
of a sudden got much better. Yeah.
I mean, it was just very obvious. You just
take the early checkpoint.
You just sample an image from it.
And then you just sample an image from,
you know, ImageGen 1.
And you just look at the two and you're
just, there's just.
Why do I like this garbage? I forgot what
the image was.

[00:12]
It might have just been like a picture of
like a woman on the seaside.
Like, you know, overlooking a seaside.
We just looked at it and we're like, all
right.
It was like no question. Yeah. That was
the big jump was the photorealism of
going from something that looked that was
more of a glossy, idealized
magazine cover to something that looked
like a really good photograph.
So help me understand, like besides just
more compute, how did this happen?
How did you get a model that's much better
and also that doesn't take an
hour to generate an image?
The times are still, I remember in the
DALL-E
days, like we would literally have to, you
know, tell us what you want.
And then an hour later, it'd be on
Instagram to now these things are in
ChatGPT and it's faster. How is it getting
both more intelligent and you're
maintaining the same speeds?
I think we learned a lot in each release,
like between 1 and 1.5, now 2.
And so we take each of the learnings that
we've made and we've, you know,
like, for example, speed, right?
You know, one of the things is like, oh,
can we make the model more token

[00:13]
efficient or something like that?
And we did a lot of work to make it
produce very good images with less
tokens. I think the post-training for this
model was very interesting in the
sense that we really had to think about
not only does the model understand
world knowledge and how things look in
science, concepts, math, etc.
in an image, but also what is the taste
that will resonate with users?
What makes the model or output beautiful?
How do you make it look realistic?
These are all questions that we had to
grapple with when we were
post-training this model. Because I think
that one of the things that was
really important for us was that this
model was the strongest aesthetic
model out there right now, which means
that it has more creativity in
various different outputs, no matter what
that output is, if it's a
professional output or a personal output.
And so that range of training and the
range of use case, I think, made

[00:14]
training this model a very interesting
problem.
Do you have any personal favorite
benchmark tests you like to do, things you
say, I want to see it make an image of
this?
I have an eval that I call the me, me, me
eval.
Okay. It's essentially 100 photos of
myself and my friends and my family.
And I put everyone in goofy positions.
I have about a card or a birthday for
every single person.
And I think it's a really great eval in
the sense that you only know the
people around your faces the best.
You also want to create funny things with
the model and do things that are
relevant. And so one thing for me as a
product manager that I'm testing is
not only is the raw capability of the
model really great, but also does
ChatGPT understand what I want in that
context?
You know, ChatGPT remembers, you know,
that I have a brother, that I have a
mom and dad and what they like to do.

[00:15]
And so does the model accurately know how
to insert pieces of
personalization in the moments that matter
in the images?
These are things that I'm testing for. How
about you?
Besides the grid one I mentioned earlier,
that's probably the one I've used
the most. For a while, I think Divya and I
were doing a lot about
photorealism. We're trying real hard to
push on that.
Just basically, I know Divya's favorite
one was like a woman holding a jug
of orange juice. I don't know if you've
seen this.
There's like so many images of a woman
holding a jug of orange juice.
Well, I actually feel like the researchers
had a more standard set of images
than they like to lead on. Yeah, and you
get like the standard.
Can it do somebody writing with their left
hand or watching on their right
hand and a clock showing this?
I think the big leap of the images, like
probably 1 or 1.5, was like a half full
glass of wine.
The wine glass folded the rim. Yeah,
folded the rim.
Yeah, exactly. And there were ways I was
able to prompt it to do it, but
it was really – had to get a really
descriptive, like, you know, red liquid

[00:16]
inside this. This one is so fun to prompt.
There was a thing people said, oh, can it
do, like, you know, can it do,
like, pixel accurate pixel image style
art?
And somebody was like, no, it can't.
And when I hear that, I'm like, okay,
let's try.
And I found out if I gave it, like, a 64
by 64 grid and I
said, go draw the art in there.
It did. It just was able to put art into
there.
And that was amazing to see those kinds of
results.
And that's the promptability of this is
insane.
How do you plan for that? Does it just
happen?
You're like, oh, wow, this is better
understanding this?
People come to ImageGen with very vague
prompts.
Yeah. Make it better. Make me look better.
You know, make me cuter. All these things
are really vague.
And I think it's really the job of the
model and the harness to distill that
into actually what users want.
And I think that's a personality of the
model that we've trained over time
that we've really harnessed the power for.
And honestly, I think it also yields a lot
of really surprising results that

[00:17]
people may not expect. And that surprise
is just part of the fun of using
ImageGen. I've seen like two kinds of
prompting sort of emerge.
And I remember back with DALL-E, I thought
like, oh, I'm a prompt engineer.
I'll be great at this. Like, I'll be
really good at this.
And I'd make a raccoon in space and be
like, feel proud.
And I'd see an artist, somebody who wasn't
a prompt engineer, somebody who
actually came from that world.
And I'd watch them use their language.
And they were doing amazing things. Yeah.
And that seems like that's still holding
true.
Definitely. I mean, we work with a group
of artists very closely when we
develop this model. And we're very
inspired by artists, designers,
marketers, all these different professions
that I think have a different way
of approaching their profession.
And one of the things that was very
important for us is we wanted to take
the inspiration as well as the best
practices for those professions and
distill that into the way that people
interact with the model.
And so that's something we've deliberately
tried to focus on.
One hack that I've seen work really well
is the ability to upload

[00:18]
inspiration or context into the model.
And the model has an incredible ability to
take the spirit of that context
and translate it into the output.
But it's interesting because I think that
a lot of people worry that, oh, I
just push in a button, I get something
beautiful.
And each model, that gets better.
It's easier, as you said, to not have to
put a lot of effort into it.
But when people do put effort into it,
they are getting even more amazing
results. And it seems like actually that
if you're artistically inclined,
you're getting even greater control
because now, like you said, it
understands more about what you're talking
about when you talk about depth
of field and these other things or
whatever you're trying to do.
And as you mentioned, it was exciting to
see with earlier models, artists
who said, oh, I gave it my originals and
it gave me these variations and I
know which one works.
And just seeing that as this real creative
amplifier.
Yeah, definitely. I think having creative
direction or taste or judgment and
bring that to the model is the best way to
push it further.
I think one thing about this model that
I'm really excited about is how it

[00:19]
expands the creative outlet for people.
I think the ability to create multiple
different styles or types or
variations has never been easier than with
this ImageGen model.
And I think it's also understanding of
different contexts, like the way that
it's able to shift what it's like to be
generating an architectural diagram
all the way to the aesthetics of a
children's book.
The ability for it to move so seamlessly
across these vectors has been
really awesome. The ability to do great
infographics and diagrams is very
powerful. What kind of feedback have you
been getting from people in
research and education?
We actually have an internal alpha channel
where we
test our models.
And in that, there's like a sub-channel
dedicated specifically towards
educators of any level, like elementary
school students all the way up to
graduate level. One of the coolest things
I saw was there was a biology

[00:20]
professor and he put like these graduate
level textbook rendering pages of
things I had no clue about. And he said it
was perfectly accurate.
I think the ability for this model to
distill very complex topics into
something that is really easy to
understand within an image is one of its
strongest capabilities.
And we've seen this with students, with
teachers who are using ImageGen to
learn different concepts, to also help
them create study guides, to help
also create personalized content.
I think personalized learning is a huge
trend that we're very passionate
about. And I think the ImageGen model
helps you as a teacher create
something that every kid can understand in
their own language and their own
preference. And that is something that
we're really excited about.
We're thinking about this in the context
of also how do we bring more of the
elements of ImageGen into ChatGPT at large
so that when people are trying to

[00:21]
learn concepts, we're teaching them with
ImageGen.
I remember when I was in school and kind
of prior to a lot of kind
of multimedia blowing up, posters were a
big thing, classroom posters
explaining stuff. This really reminded me
of how powerful an infographic can
be because it allows you to bring as much
attention as you want to it.
And you can spend the time looking at it
and seeing it, and you can put
a lot more detail into it. I think one
really awesome visual shift that I've
seen with ImageGen is that now in internal
presentations, over 50% of the
slides are created with ImageGen.
Wow. And that permeation of communication
via images is so powerful when
you're trying to explain your concepts or
illustrate what you mean.
And I think infographics and the text
rendering capability, as well as the
composition of the text on the page, is
incredibly powerful with this model.
The model's understanding of not only what
to say, but how to present it is
a superpower. And I'm really excited about
future explorations of this,

[00:22]
where we can think about how do we make
this even better?
How do we improve the composition, the
different kinds of outputs, and also
make it editable in the product?
These are directions that we're really
excited about.
How do you see the progression of this?
This is great, but typically anytime I
talk to somebody to open an eye about
what they're working on, they're like,
yeah, this is good, but.
I think we're still super early in
exploring all the different use cases
that people are really trying to push the
model with.
And so one of the things that we're really
excited about is what is that
next stage for ImageGen, which is to
create the creative agent.
Ultimately, the agent that can work
alongside you, be your creative
assistant, and really understand how you
work, what your preferences are,
what is the output that you want to get
to, and build the product and model
ecosystem that helps users kind of have a
personal interior designer,
personal architect, personal wedding
planner, et cetera, all in one image.

[00:23]
I'll tell you another thing that was kind
of amazing was like, all right,
books. And so every now and then I have a
book come out, I've got to
change my social media headers. And I just
went and I said, oh, find my book
cover and create an appropriate size
social media header that I can put on X
or Facebook or whatever. I'm like, well,
let's see.
First shot. First shot. Right aspect
ratio.
Everything. We basically did that from the
start or trained the models to be
good at that from the start. I remember I
worked on the initial de-risk of
basically it could do any aspect ratio
that you ask.
Yeah. Yeah, you can now really just easily
specify the outcome that you
want. Yeah. Like in the case of yourself,
you're like, I want promotional
material. I don't have an idea. I didn't
specify exactly what I wanted.
But the model was able to do the research
and then give it to you in
the style and aspect ratio that was
relevant to you.
And that's super powerful. We're already
seeing this.
you know you're an author I've talked to
real estate agents who are using

[00:24]
ImageGen to help them create listings for
their apartments or stage their
listings YouTube creators have talked to
me about using ImageGen for their
thumbnails and promotional content I've
talked to top artists who want to
use ImageGen to connect with their fans
and I think the ability for all
different kinds of professions to start to
use ImageGen to help them with
visual creation is super powerful
especially if you're working in a visual
and a creative industry, ImageGen is such
a hack in your professional
toolkit. I think it has to be a part of
everyone's everyday workflow in the
future. This does feel like the, I think
it feels like the first time where
anything I can reasonably come up with, it
does a pretty good job of it.
We think it's a new paradigm for image
generation altogether.
Like if, you know, we set this in the
launch video, if DALL-E was the stone
ages, ImageGen 2.0 is the Renaissance.
Yeah. And I think that is so true because
the model, It's not only great
artistically and aesthetically, but it
also incorporates science, art,

[00:25]
architecture, all in one image together.
And I think that composition and knowledge
that the model has just means
that the outputs are so much more
trustworthy, are more powerful, and enable
so many more use cases. I think that
ImageGen and Codex is also an amazing
intersection of the capabilities that
we're setting out to create with both
ImageGen as well as coding agents.
So many people are using ImageGen as a
first step to designing a new website
or creating a new app. And I think that
intersection of having a really
strong aesthetic model, which is image
generation, in combination with
strong coding abilities, means that now
you're able to zero shot really
amazing apps from scratch with both of
these tools.
Yeah, I asked it in Codex. I said, I took
my website.
I said, could you make me, I had the
ImageGen.
Could you create me some different
concepts for it?
And I did these contact sheets. I asked
for contact sheets to that.
Give me like four images there. And I
said, oh, the one on the upper right.

[00:26]
Can you go make that?
And I watched Codex go make that, which
was like, this
feels like magic. And then they've
implemented as part of pets.
And so like if you're using Codex and you
say, hey, I want to have like
I have like I love Raven. So I have like a
Raven.
I said, can you make a Raven? And then I
watched it pull up the ImageGen
tool and iterate and make the sprites for
it.
Yeah. Sprite sheets are going viral.
Yeah. Same with game design.
People are loving. using ImageGen to help
them create new worlds.
Any hints on how to do better sprite
sheets?
I mean, I've tried to make, you know, GIFs
internally.
And I think if I just use, like, the
thinking mode or Codex, and you
basically just ask it to generate one
initial sprite, it's really good.
And then you can just say, can you make
the rest?
The consistency across multi-images has
been amazing.
We've seen a lot of people try creating
10-page comic books with consistent
storylines, multi-page slides.
I think that consistency of characters and
aesthetics

[00:27]
is completely unique to this model.
That was an example too, where there were
a lot of workflows out there for
working with image models that were kind
of janky, but you had to figure out
how to do. And it's great now because I
can do stuff where I can create
characters and say, make a character sheet
with the different poses and
stuff and just go feed it back in and say,
okay, now doing this, now doing
that, now doing that. And that's just such
a – often, sometimes what we need
is obviously a smarter model, but context
length did so much for ChatGPT,
did so much for coding. And with an image
model, it's able to reliably
reference these references.
It's incredibly capable. Yeah, for sure.
And we're still trying to improve that as
well.
It's not perfect today. We're really
trying to develop this visual creation
layer for people because every single
person you have an aesthetic or
personal style or preference.

[00:28]
And we're really trying to imbue that into
the product that we're building
so that people can get to the output that
they're wanting easier and faster
with ImageGen. Any parting prompt tips for
people?
Well, one of the things I would suggest
people try is ImageGen thinking.
So if you navigate to the thinking or pro
models, we have a more powerful
version of ImageGen in that experience.
And in that model, you actually are able
to search the web, analyze files,
leverage tools under the hood, which then
yields a better quality and higher
composition photo.
And the suggestion that I have for
prompting that experience is be
open-ended. I think the model will go and
do the exploration itself to
understand and try to reason and find
information that matters.
And I also think giving it a sense of an
aesthetic is also super helpful.
Using and grounding that in a style has
been really fruitful for a great

[00:29]
result. Good one. Good one.
I think just being very particular about
the
style or like what you like in general.
Like for me, I like minimalist
infographics.
Sometimes I think the model can be a
little dense.
And so I just maybe I'm just a simplistic
kind of guy so I just like
very very clean a very clean look so I
like that.
Adele, Kenji, thank you very much.

</details>
