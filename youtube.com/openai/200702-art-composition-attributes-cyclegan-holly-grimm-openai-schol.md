---
title: "Art Composition Attributes + CycleGAN | Holly Grimm | OpenAI Scholars Demo Day 2018"
channel: openai
url: https://www.youtube.com/watch?v=KisG5I0DcpY
youtube_id: KisG5I0DcpY
published: 2020-07-02
duration: "7:03"
captions: en-orig
---

# Art Composition Attributes + CycleGAN | Holly Grimm | OpenAI Scholars Demo Day 2018

[![Art Composition Attributes + CycleGAN | Holly Grimm | OpenAI Scholars Demo Day 2018](https://img.youtube.com/vi/KisG5I0DcpY/hqdefault.jpg)](https://www.youtube.com/watch?v=KisG5I0DcpY)

<details>
<summary>자막: Art Composition Attributes + CycleGAN | Holly Grimm | OpenAI Scholars Demo Day 2018 (7:03)</summary>

[00:00]
hi my name is Holly Grimm and I'm an
artist and software developer from Santa
Fe New Mexico and this painting up here
on the upper left here is one of my
original paintings from the Santa Fe
National Forest and I used my tool set
that I'll be talking about to transform
it into these other images that you see
here artificial intelligence and
creativity how does creativity fit into
a GI one definition of computational
creativity is that it's a two phase flow
of generation and evaluation first novel
constructs are generated and then they
are evaluated for are based on
meaningfulness and usefulness and here's
a similar model in reinforcement
learning where actions are generated and
evaluated so for my creativity in art

[00:01]
here's a list of aesthetic principles
that I got from Dennis Dutton and in
particular I'm interested in applying
style for this project so here's a
related project that most of us know is
the image style transfer project from
2016 and it demonstrates form in the
form of a lion and composition for my
project instead of image for composition
I'm using eight art composition
attributes that I learned from my art
teacher and here and they'll be using I
was using the wiki art dataset traina
and so here are some examples of
paintings that that applied to each of
these sorry
to each of these attributes for instance
variety of texture here is a this these
are the low values along the top here it
has very little texture and the lower

[00:02]
lower road has high texture or high
shapes etc four primary color I use the
cyan and yellow magenta color wheel and
here are examples for each color in the
in the wheel and here are six images
with orange primary color showing color
harmony relationships so for instance
these are all the orange is the primary
color in these paintings but they have
various other colors that are also part
of the paintings based on these
different colors relationships so here's
four different major colors in this
painting here so here's a diagram of the
network I used I used to resonate 50
Network train free trains on image stats
and each residual block activation is

[00:03]
passed through a global app beverage
cooling layer and then merged into each
of the attributes if you recall from my
previous diagram the lion on the Left
what's the form but for my tests I use
the cycle game apple - orange data set
and so this is where the a real an apple
is generated and I mean an orange is
translated or a fake orange is generated
from the Apple and then reconstructed
back in addition to the classic cycle
gam AUSA's I added I passed this
translated Orange
my Aitken network along with some target
attribute values and and then I came up
with some losses based on that and so
here's some example results
here's color harmony after passing the
Apple in and passing in hi analogous

[00:04]
value it was able to create a analogous
color wheel basically and then here's
another example here for a complementary
color we're out of the leaf and the
background were changed to blue cyan and
I have another example as a variety of
color the left is was an image with a
lot of color here and it was translated
into a monochromatic red color on the
right shows the opposite case where
there were many it's kind of hard to see
on the slide but there were many colors
that were generated and even with the
relatively small dataset of 500 label
wiki labelled wiki art images I was able
to train on these eight art
compositional attributes via the cycle
again plus the a can network and get
some pretty interesting results so

[00:05]
possible next steps would include
applying activation mapping to
understand how the different
compensation 'el attributes are working
here's an example from learning
photography aesthetics from 2017 and it
would also be interesting to replace my
cycle again at work with other form
generation strategies like opening eyes
2018 project glow where they generated
these images of faces and bedrooms and
in another cool project from 2015 was
where an IRL robotic at rope robotic
Ayden's generated the actual physical
paintings here on the right using a
inverse reinforcement
you could find my blog posts for this
project on my website and the code is on
github and again here's another painting
of mine in the upper left-hand corner
with some of the generations that I got

[00:06]
from my network I'd like to thank open
AI and in particular of my mentor
Christie and Larissa and the rest of my
scholars thank you so much okay so many
questions
yeah so I I basically just did a merge
on those on the from the global average
bullying did emerge right into that and
that's actually I think learning from
photography aesthetics is a is where I
got that particular method of doing that
any other
and I'm always available over here later
for questions
[Applause]

</details>
