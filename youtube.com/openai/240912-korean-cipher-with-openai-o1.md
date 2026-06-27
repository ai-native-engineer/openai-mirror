---
title: "Korean Cipher with OpenAI o1"
channel: openai
url: https://www.youtube.com/watch?v=eZDmDn6Iq9Y
youtube_id: eZDmDn6Iq9Y
published: 2024-09-12
duration: "3:14"
captions: en-orig
---

# Korean Cipher with OpenAI o1

[![Korean Cipher with OpenAI o1](https://img.youtube.com/vi/eZDmDn6Iq9Y/hqdefault.jpg)](https://www.youtube.com/watch?v=eZDmDn6Iq9Y)

<details>
<summary>자막: Korean Cipher with OpenAI o1 (3:14)</summary>

[00:00]
so the example I'm I'm going to try out
is a almost a code cracking of a badly
corrupted Korean sentence so here I
pasted in the The Prompt and I'm asking
the model to translate this badly
corrupted Korean sentence to uh English
and as you can see this is not a invalid
Korean uh sentence so let's start with
the existing model GPT 40 and see how it
does the model is just not able to
understand this text which is a valid
response because this is not a valid
language so what's happening here U so
Korean is an interesting language in
that when we form a character we can
combine vowels and consonants sometimes
put the consonant at the bottom and so
on one way to corrupt this character is
to add in some extra unnecessary
consonants to it and that combination is
so unnatural to native speakers so they
can just when they see it uh just
automatically undo that change and

[00:01]
understand the text so this is character
level corruption we can do that at the
phrase level we can also do that at the
sound level and so on people have come
up with various methods like this and I
found that really interesting so I
adopted a few of them to create this
example so if you understand Korean this
part that I'm highlighting now you can
read it off as
a and so on I'm not going to read off
the whole thing but this is the idea
Koreans can read it but the models find
it so difficult to understand so now
let's go on to our new model uh o1
preview and see if reasoning can help
solve this problem so I typed in the
same thing unlike GPT 40 this Model
start thinking uh thinking through this
problem before outputting the answer so
it's decoding the garble text so that's
actually the U the right approach
because this is I gave a a translation
task but the under L task is actually

[00:02]
decoding this problem so it started off
the right path and then I'm examining
this text deciphering the text
deciphering is actually the right Verve
to use here enhancing the translation
and then actually it starts unpacking
some part of it so here
boom and so on this is already an
decrypted part of this and then once the
model figures it out that part
everything else is just easy enough so
it does the other sentence too and so
let's close this thought so it thought
for 15 seconds the final translation the
model output is no translator on Earth
can do this but Koreans can easily
recognize it there is a method of
encrypting hungo by inputting various
transformations of vowels and consonants
it creates a way to make it look
different on the surface it can even
confuse AI models I think this is a
perfect translation of the sentence so
this illustrate how general purpose
reasoning models like o1 preview can
help seemingly

[00:03]
unrelated questions like this which is
almost like a code cracking so um I hope
this illustrate how reasoning can be a
powerful tool for for solving your
problems

</details>
