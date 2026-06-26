<!-- source: https://openai.com/index/musenet/ -->

April 25, 2019

[Milestone](/research/index/milestone/)

# MuseNet

![Musenet](https://images.ctfassets.net/kftzwdyauwt9/cd5a2134-380b-4ecb-f3dc692f0471/2176f5a9461083ef3238168101d3dc42/Frame_6.png?w=3840&q=90&fm=webp)

Illustration: Ben Barry

We’ve created MuseNet, a deep neural network that can generate 4-minute musical compositions with 10 different instruments, and can combine styles from country to Mozart to the Beatles. MuseNet was not explicitly programmed with our understanding of music, but instead discovered patterns of harmony, rhythm, and style by learning to predict the next token in hundreds of thousands of MIDI files. MuseNet uses the same general-purpose unsupervised technology as [GPT‑2⁠](/index/better-language-models/), a large-scale [transformer⁠(opens in a new window)](https://arxiv.org/abs/1706.03762) model trained to predict the next token in a sequence, whether audio or text.

## Samples

Loading...

Since MuseNet knows many different styles, we can blend generations in novel ways.[A](#citation-bottom-A) Here the model is given the first 6 notes of a Chopin Nocturne, but is asked to generate a piece in a pop style with piano, drums, bass, and guitar. The model manages to blend the two styles convincingly, with the full band joining in at around the 30 second mark:

Loading...

We’re excited to see how musicians and non-musicians alike will use MuseNet to create new compositions![1](#citation-bottom-1)

In *simple mode* (shown by default), you’ll hear random uncurated samples that we’ve pre-generated. Choose a composer or style, an optional start of a famous piece, and start generating. This lets you explore the variety of musical styles the model can create. In *advanced mode* you can interact with the model directly. The completions will take longer, but you’ll be creating an entirely new piece.

Loading...

Some of MuseNet’s limitations include:

* The instruments you ask for are strong suggestions, not requirements. MuseNet generates each note by calculating the probabilities across all possible notes and instruments. The model shifts to make your instrument choices more likely, but there’s always a chance it will choose something else.
* MuseNet has a more difficult time with odd pairings of styles and instruments (such as Chopin with bass and drums). Generations will be more natural if you pick instruments closest to the composer or band’s usual style.

## Composer and instrumentation tokens

We created composer and instrumentation tokens to give more control over the kinds of samples MuseNet generates. During training time, these composer and instrumentation tokens were prepended to each sample, so the model would learn to use this information in making note predictions. At generation time, we can then condition the model to create samples in a chosen style by starting with a prompt such as a Rachmaninoff piano start:

Loading...

Or prompted with the band Journey, with piano, bass, guitar, and drums:

Loading...

We can visualize the embeddings from MuseNet to gain insight into what the model has learned. Here we use [t-SNE⁠(opens in a new window)](https://lvdmaaten.github.io/tsne/) to create a 2-D map of the cosine similarity of various musical composer and style embeddings.

Loading...

## Long-term structure

MuseNet uses the recompute and optimized kernels of [Sparse Transformer⁠](/index/sparse-transformer/) to train a 72-layer network with 24 attention heads—with full attention over a context of 4096 tokens. This long context may be one reason why it is able to remember long-term structure in a piece, like in the following sample imitating Chopin:

Loading...

It can also create musical melodic structures, as in this sample imitating Mozart:

Loading...

Music generation is a useful domain for testing the Sparse Transformer as it sits on a middle ground between text and images. It has the fluid token structure of text (in images you can look back N tokens and find the row above, whereas in music there’s not a fixed number for looking back to the previous measure). Yet we can easily hear whether the model is capturing long term structure on the order of hundreds to thousands of tokens. It’s much more obvious if a music model messes up structure by changing the rhythm, in a way that it’s less clear if a text model goes on a brief tangent.

## Dataset

We collected training data for MuseNet from many different sources. [ClassicalArchives⁠(opens in a new window)](https://www.classicalarchives.com/) and [BitMidi⁠(opens in a new window)](https://bitmidi.com/) donated their large collections of MIDI files for this project, and we also found several collections online, including jazz, pop, African, Indian, and Arabic styles. Additionally, we used the [MAESTRO dataset⁠(opens in a new window)](https://arxiv.org/abs/1810.12247).

The transformer is trained on sequential data: given a set of notes, we ask it to predict the upcoming note. We experimented with several different ways to encode the MIDI files into tokens suitable for this task. First, a chordwise approach that considered every combination of notes sounding at one time as an individual “chord”, and assigned a token to each chord. Second, we tried condensing the musical patterns by only focusing on the starts of notes, and tried further compressing that using a byte pair encoding scheme.

We also tried two different methods of marking the passage of time: either tokens that were scaled according to the piece’s tempo (so that the tokens represented a musical beat or fraction of a beat), or tokens that marked absolute time in seconds. We landed on an encoding that combines expressivity with conciseness: combining the pitch, volume, and instrument information into a single token.

#### Plain Text

```` ```
1

bach piano_strings start tempo90 piano:v72:G1 piano:v72:G2 piano:v72:B4 piano:v72:D4 violin:v80:G4 piano:v72:G4 piano:v72:B5 piano:v72:D5 wait:12 piano:v0:B5 wait:5 piano:v72:D5 wait:12 piano:v0:D5 wait:4 piano:v0:G1 piano:v0:G2 piano:v0:B4 piano:v0:D4 violin:v0:G4 piano:v0:G4 wait:1 piano:v72:G5 wait:12 piano:v0:G5 wait:5 piano:v72:D5 wait:12 piano:v0:D5 wait:5 piano:v72:B5 wait:12
``` ````

Sample encoding which combines pitch, volume, and instrument.

During training, we:

1. Transpose the notes by raising and lowering the pitches (later in training, we reduce the amount of transposition so that generations stay within the individual instrument ranges).
2. Augment the volumes, turning up or turning down the overall volumes of the various samples.
3. Augment timing (when using the absolute time in seconds encoding), effectively slightly slowing or speeding up the pieces.
4. Use [mixup⁠(opens in a new window)](https://arxiv.org/abs/1710.09412) on the token embedding space

We also create an inner critic: the model is asked during training time to predict whether a given sample is truly from the dataset or if it is one of the model’s own past generations. This score is used to select samples at generation time.

## Embeddings

We added several different kinds of embeddings to give the model more structural context. In addition to the standard positional embeddings, we added a learned embedding that tracks the passage of time in a given sample. This way, all of the notes that sound at the same time are given the same timing embedding. We then add an embedding for each note in a chord (this mimics relative attention, since it will be easier for the model to learn that note 4 needs to look back at note 3, or else at note 4 of the previous chord). Finally, we add two structural embeddings which tell the model where a given musical sample is within the larger musical piece. One embedding divides the larger piece into 128 parts, while the second encoding is a countdown from 127 to 0 as the model approaches the (end) token.

We’re excited to hear what people create! If you create a piece you like, you can upload it to a free service like [Instaudio⁠(opens in a new window)](https://instaud.io/) and then tweet us the link (the MuseNet demo has a tweet button to help with this).

If you’re interested in learning more about OpenAI’s music work, consider [applying⁠](/careers/) to join our team. Please feel free to [email us⁠](mailto:musenet@openai.com) with suggestions for the MuseNet demo. We’d also love to hear from you if you’re interested in composing with MuseNet in more depth, or if you have MIDI files you’d like to add to the training set.

Loading...

* [GPT](/research/index/?tags=gpt)
* [Generative Models](/research/index/?tags=generative-models)
* [Learning Paradigms](/research/index/?tags=learning-paradigms)
* [Transformers](/research/index/?tags=transformers)

## Footnotes

1. A

   If you’re interested in other projects for creating AI generated music using transformers, we recommend checking out [Magenta’s piano generation work⁠(opens in a new window)](https://magenta.tensorflow.org/music-transformer).

## References

1. For use of outputs created by MuseNet, please cite this blog post as

Payne, Christine. "MuseNet." *OpenAI*, 25 Apr. 2019, openai.com/blog/musenet

Please note: We do not own the music output, but kindly ask that you not charge for it. While unlikely, we make no guarantee that the music is free from external copyright claims.

## Related articles

![Whisper](https://images.ctfassets.net/kftzwdyauwt9/13c810cb-0592-442d-190ab7378bef/a7cb2299d034abe93023f662f8d32263/Speech_Rec_16_9.png?w=3840&q=90&fm=webp)

[Introducing Whisper

ReleaseSep 21, 2022](/index/whisper/)

![Hierarchical Text Conditional Image Generation With Clip Latents](https://images.ctfassets.net/kftzwdyauwt9/7c44eedc-3563-4438-c613706c52b1/fcfc38b26fd4878a3c6b4ca8d1d73b17/hierarchical-text-conditional-image-generation-with-clip-latents.jpg?w=3840&q=90&fm=webp)

[Hierarchical text-conditional image generation with CLIP latents

PublicationApr 13, 2022](/index/hierarchical-text-conditional-image-generation-with-clip-latents/)

![Solving Some Formal Math Olympiad Problems](https://images.ctfassets.net/kftzwdyauwt9/107bb1e1-daad-40bf-85975dfa741c/57d987d185a7a46828ea203bb0132867/image-12_copy.png?w=3840&q=90&fm=webp)

[Solving (some) formal math olympiad problems

MilestoneFeb 2, 2022](/index/formal-math/)
