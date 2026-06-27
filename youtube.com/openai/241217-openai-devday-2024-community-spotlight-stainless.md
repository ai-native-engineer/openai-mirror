---
title: "OpenAI DevDay 2024 | Community Spotlight | Stainless"
channel: openai
url: https://www.youtube.com/watch?v=aFedOROUXMQ
youtube_id: aFedOROUXMQ
published: 2024-12-17
duration: "5:23"
captions: en-orig
---

# OpenAI DevDay 2024 | Community Spotlight | Stainless

[![OpenAI DevDay 2024 | Community Spotlight | Stainless](https://img.youtube.com/vi/aFedOROUXMQ/hqdefault.jpg)](https://www.youtube.com/watch?v=aFedOROUXMQ)

<details>
<summary>자막: OpenAI DevDay 2024 | Community Spotlight | Stainless (5:23)</summary>

[00:00]
so Robert um I'm gonna uh put you on the
hot seat like right away so like okay I
can get this for free right like there
are how many tools out there that are
open source that uh already can take an
open API specification and generate
client libraries for me like why do I
pay you guys six figures like to
generate our SD for us like what's this
about yeah um if anyone in this room
might remember an old version of the
openi node s actually was generated
using one of these open source tools
called open API generator um and that
was missing one core feature that the
open API really needs is
streaming so we Bak that into our Cen
for you and other customers uh and then
we also have built stuff on top of the
generated sdks using one of our features
which is custom code and you can make
any arbitary change to the sdks that you
want um just like it was any normal repo

[00:01]
yeah which is pretty slick so uh have
has anybody used like structured outputs
through the sdks uh so far couple couple
folks so uh that's that's a good example
of like custom code like we have like
Zod and pantic helpers that are a part
of the SDK uh that uh is very specific
to how the open AI open API uh excuse me
open AI using those words in the same
sentence is pretty brutal uh but it's
very specific to how our technology
Works um and like how does that like how
does that come together like how do you
apply that the custom code to the SDK
like when you're doing a release like
yeah it's we do some G magic behind the
scenes uh so we have multiple branches
one branch is just this is the Cen
output and then another branch is has
all the stuff on top of it and then we
do some get cherry picking um yeah it's
like you it's like applying a patch at
the end of the day yeah basic like you
just like the custom code it comes in as
a patch and then uh what's really nice
as the uh like you just get a pull
request to your repo that has just like
all the relevant changes like new types

[00:02]
and stuff like that so it's pretty sick
um all right so uh I I've been working
on developer tools for a little while
now um and I actually told Robert that
the first like API client I wrote was in
nodejs 0.8 and like his eyes widened in
Terror like you couldn't believe people
were writing software like back in those
days um but back in my day Robert uh we
had to uh you know write SDK s that set
on top of rest apis from scratch um and
when we did that like we thought aot
about like what the right level of
abstraction was like do you create like
a very thin layer over the top of the
HTTP request response cycle or do you
like completely abstract it behind like
some kind of big object model like what
what do you think like the right place
is to land like what how do you think
about making that decision yeah I think
it really depends on the kind of Sate
you're providing so if you're Vell zi
package or Lang chain you can come up
with your own really nice abstractions
for certain use cases um but if you're
providing a first party SDK like open I

[00:03]
python for
example you really need to be able to
support everything that the API does um
and if you create a really thin wrapper
over the HTTP API then you'll support
everything and then all of your
customers and users can just look at
your API docs and then really quickly
map how the API Works into how the SDK
works and if you create your own
abstractions then they would have to
learn how the API works and then how to
use the SDK yeah so uh so like using the
to like paper over rough parts of the
API is generally considered considered
harmful like because you'll create some
confusion around what's actually there
or not yeah exactly like why is this one
thing called two different things um
yeah totally so like what what are like
the helpful things to abstract away like
what what do you think is useful to
create some abstractions in like with an
HTP interface yeah one of the big ones
is pagination um because obviously you
can't fit all the data in one single HTP
response and then so it has to be split
up into multiple things

[00:04]
um and then an SK is a great use case
for that um along with auto retries you
know if you can't connect for some
reason and then that's just an inent
error then your application can continue
working without any issues if you were
just making a real HTP request without
any retries yeah and like what what is
the important like detail of the HTP API
that you do have to surface like what
can't you abstract
away um one thing is like headers like
you need to be able to say
um uh users will need to be able to
access the RO response in some cases
they might want to log all the headers
they got or how long it took to just get
the response or they might not want to
parse the the response into your Ridge
Chason object
um so generally like the the fact that
that that an HTTP request is happening
is essential like you're going to need
that data um
eventually um so one other thing so like
automatically generating code uh for

[00:05]
sdks like has the has the possible
Pitfall of like generating bad code and
that's like why like the open source
solutions that we were using before like
ultimately we didn't go with those um
because like the generated output was
not up to snu and like especially like
languages like python there's this like
sense that python code should be
pythonic like it should look look and
feel a certain way like how do you like
think

</details>
