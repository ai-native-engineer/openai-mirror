---
title: "Coding with OpenAI o1"
channel: openai
url: https://www.youtube.com/watch?v=50W4YeQdnSg
youtube_id: 50W4YeQdnSg
published: 2024-09-12
duration: "2:46"
captions: en-orig
---

# Coding with OpenAI o1

[![Coding with OpenAI o1](https://img.youtube.com/vi/50W4YeQdnSg/hqdefault.jpg)](https://www.youtube.com/watch?v=50W4YeQdnSg)

<details>
<summary>자막: Coding with OpenAI o1 (2:46)</summary>

[00:00]
[Music]
all right so the example I'm going to
show is a writing a code for
visualization so I sometimes teach a
class on Transformers which is a
technology behind models like chipt and
when you give a sentence to Chach PT it
has to understand the relationship
between the words and so on so it's a
sequence of words and you just have to
model that and Transformers utilize
what's called a self attention to model
that so I always thought okay if I can
visualize a self attention mechanism and
with some interactive components to it
it will be really great I just don't
have the skills to do that so let's ask
our new model o1 preview to help me out
on that so I just typed in uh this
command uh and see how the model does so
unlike the previous models like GPT 40
it will think before outputting an
answer so it starts started thinking as
this thinking let me uh show you what
are some of these uh requirements I'm
giving a bunch of requirements to think

[00:01]
through so first one is like use an
example sentence the quick brown fox and
second one is like when hovering over a
token visualize the edges whose
thicknesses are proportional to the
attention score and that means just if
the two words are more relevant then
have a thicker edges and so on so the
one common failure modes of the existing
modles is that when you give a lot of
the instructions to follow it can miss
one of them just like humans can miss
one of them if you give too many of them
at once once so because this reasoning
model can think very slowly and
carefully it can go through each
requirement uh in depth and that reduces
the chance of missing um the instruction
so this output code let me copy paste
this into a terminal so I'm going to use
the D editor of 2024 so Vim HTML so I'm
just going to paste this thing into that

[00:02]
and just save it out uh and on the
browser I'll just try to open this up
and you can see that uh when I Hoover
over this thing it shows the arrows um
and then quick and brown and so on and
when I Hoover out of it it goes away so
that's a correctly rendered um version
of it now when I click on it it shows
the tension scores as just just as I
asked for and maybe there's a little bit
of rendering like it's overlapping but
other than that is actually much better
than what I could have done yeah so this
model did uh really nicely I think this
can be a really useful tool for me to
come up with a bunch of different
visualization tools for uh my new
teaching sessions

</details>
