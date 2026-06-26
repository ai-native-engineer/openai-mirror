<!-- source: https://openai.com/index/sparse-transformer/ -->

April 23, 2019

[Publication](/research/index/publication/)

# Generative modeling with sparse transformers

[Read paper(opens in a new window)](https://arxiv.org/abs/1904.10509)[(opens in a new window)](https://github.com/openai/sparse_attention)

![Sparse Transformer](https://images.ctfassets.net/kftzwdyauwt9/103412f3-2a59-4835-0b613995759a/e6a3d3ff1b73219391d36ea1648a6305/sparse-transformer.jpg?w=3840&q=90&fm=webp)

We’ve developed the Sparse Transformer, a deep neural network which sets new records at predicting what comes next in a sequence—whether text, images, or sound. It uses an algorithmic improvement of the *attention* mechanism to extract patterns from sequences 30x longer than possible previously.

One existing challenge in AI research is modeling long-range, subtle interdependencies in complex data like images, videos, or sounds. The Sparse Transformer incorporates an O(NN) O(N \sqrt{N}) O(NN​) reformulation of the O(N2) O(N^2) O(N2) [Transformer⁠(opens in a new window)](https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html) self-attention mechanism, along with several other improvements, to apply it directly to these rich data types. Previously, models used on these data were specifically crafted for one domain or difficult to scale to sequences more than a few thousand elements long. In contrast, our model can model sequences with tens of thousands of elements using hundreds of layers, achieving state-of-the-art performance across multiple domains. At OpenAI, we’re using it to help us build AI systems that possess a greater ability to understand the world.

## Deep attention

In Transformers, every output element is connected to every input element, and the weightings between them are dynamically calculated based upon the circumstances, a process called *attention*. While it is believed that this allows Transformers to be more flexible than models with fixed connectivity patterns, in practice it requires the creation of an N×N N\times N N×N *attention matrix* for every layer and attention head, which can consume large amounts of memory when applied to data types with many elements, like images or raw audio.

|  |  |  |
| --- | --- | --- |
| **Data type** | **Stored** | **Recomputed** |
| 1024 text tokens (several paragraphs) | 1.0 GB | 16 MB |
| 32x32x3 pixels (CIFAR-10 image) | 9.6 GB | 151 MB |
| 64x64x3 pixels (Imagenet 64 image) | 154 GB | 2.4 GB |
| 24,000 samples (~2 seconds of 12 kHz audio) | 590 GB | 9.2GB |

Attention memory usage for a deep Transformer (64 layers and 4 heads) when matrices are stored in memory or recomputed during the backward pass. For reference, standard GPUs used for deep learning typically have memory of 12-32 GB.

One way to reduce this is by recomputing the attention matrix from *checkpoints* during backpropagation, a well-established technique in deep learning for reducing memory usage at the cost of more computation. When done for the attention matrix in Transformers, it means the largest memory cost becomes independent of the number of layers, letting us train networks with substantially greater depth than possible previously. In practice, we found that Transformers with depth up to 128 layers outperformed shallower networks on benchmark tasks like CIFAR-10.

To train these models with increased depth, we made several adjustments to the ordering of operations in the transformer and modified the initialization scheme. Full details can be seen in our paper.

## Sparse attention

Even computing a single attention matrix, however, can become impractical for very large inputs. We instead use sparse attention patterns, where each output position only computes weightings from a subset of input positions. When the subset is small relative to the full set of inputs (say, N \sqrt{N} N​​ elements instead of  N N  N elements), the resulting attention computation becomes tractable even for very long sequences, with an algorithmic complexity of O(NN) O(N \sqrt{N}) O(NN​) instead of O(N2) O(N^2) O(N2).

To assess the feasibility of the approach, we first visualized the learned attention patterns for deep Transformers on images, finding that many showed interpretable and structured sparsity patterns. Each of the below images shows which input pixels (highlighted in white) are attended to by a given attention head in order to predict the next value in the image. When the input portions are focused on small subsets and show a high degree of regularity, the layer is amenable to sparsification. A sampling of them are displayed here for a 128-layer model on CIFAR-10 images:

Loading...

Loading...

While many layers displayed sparse structure, some layers clearly display dynamic attention that stretch over the entirety of the image. In order to preserve the ability of our network to learn such patterns, we implemented a two-dimensional factorization of the attention matrix, where the network can attend to all positions through two steps of sparse attention.

Loading...

The first version, *strided* attention, is roughly equivalent to each position attending to its row and its column, and is similar to the attention pattern learned by the network above. (Note that the column attention can be equivalently formulated as attending to the row of the transposed matrix). The second version, *fixed* attention, attends to a fixed column and the elements after the latest column element, a pattern we found useful for when the data didn’t fit into a two-dimensional structure (like text). For more details, we refer readers to our paper.

## Experimental results

Sparse Transformers set new state-of-the-art scores for density estimation of CIFAR-10, Enwik8, and Imagenet 64.

|  |  |
| --- | --- |
| **CIFAR10** | **Bits per dim** |
| PixelCNN++ (Salimans et al, 2017) | 2.92 |
| Image Transformer (Parmar et. al, 2018) | 2.90 |
| PixelSNAIL (Chen et al., 2017) | 2.85 |
| Sparse Transformer 59M (256W, 128L, 2H) | 2.80 |

|  |  |
| --- | --- |
| **Enwik8** | **Bits per byte** |
| Deeper Self-Attention (Al-Rfou et al, 2018) | 1.06 |
| Transformer-XL 88M (Dai et al., 2018) | 1.03 |
| Transformer-XL 277M (Dai et al., 2018) | 0.99 |
| Sparse Transformer 95M (512W, 30L, 8H) | 0.99 |

|  |  |
| --- | --- |
| **ImageNet 64x64** | **Bits per dim** |
| Gated PixelCNN (van den Oord et al, 2016) | 3.57 |
| Parallel Multiscale (Reed et al, 2017) | 3.7 |
| SPN 150M (Menick & Kalchbrenner, 2018) | 3.52 |
| Sparse Transformer 152M (512W, 48L, 16H) | 3.44 |

Density modeling performance in bits per byte (or dim) on a variety of benchmark datasets. M denotes millions of parameters used in the network, W the width of the network, L the number of layers, and H the number of heads.

We also found that sparse attention achieved lower loss than full attention, in addition to being significantly faster (see our paper for comparisons). This may point to a useful inductive bias from our sparsity patterns, or an underlying optimization issue with dense attention.

## Generating images

Transformers that use sparse attention seem to have a notion of global structure, which can be qualitatively evaluated by looking at image completions. Here we visualize a model trained on 64×64 64\times 64 64×64 ImageNet:

![Half-images used to train a sparse attention transformer to complete images](https://images.ctfassets.net/kftzwdyauwt9/80f4bb40-ddc0-4df3-7af675a97ea4/4a753784c553181e7b1c0512650c72c0/cond-prompt-1.png?w=3840&q=90&fm=webp)

![Grid of images completed using a sparse attention transformer](https://images.ctfassets.net/kftzwdyauwt9/3a1e062c-3ee7-46be-2a11da35cd55/5c31c543850bbe051d3d894538f175bd/cond-grid-1.png?w=3840&q=90&fm=webp)

![Row of photographs used as samples to train a sparse attention transformer to complete images](https://images.ctfassets.net/kftzwdyauwt9/d715dd6a-b842-4b75-cc18c26f88a8/101f859270ec19f4d5f7d2137f1d9c4f/cond-gt-1.png?w=3840&q=90&fm=webp)

We also generated fully unconditional samples with an unadjusted softmax temperature of 1.0. These models are trained using the maximum likelihood objective, which is well-known to cover all modes of the data (including potentially nonexistent ones) instead of increasing fidelity of a smaller portion of the data. Sampling from these models with unadjusted temperature lets us see the full distribution of images that the model believes exists in the world. As a result, some samples can appear strange.

![Sample images used to train a sparse attention transformer model](https://images.ctfassets.net/kftzwdyauwt9/1291eb88-0c0f-466f-c12c0dd34e9b/f50abb38668b59a37e1a72881f88362b/uncond-samples.png?w=3840&q=90&fm=webp)

Model samples

![Imagenet True Data](https://images.ctfassets.net/kftzwdyauwt9/598e1375-02a4-4266-2f7182ba6009/28df1c0ed4f0303115c4b9e26d8fb4fb/imagenet_true_data.png?w=3840&q=90&fm=webp)

Real data

## Generating raw audio waveforms

Sparse Transformers can also be adapted to generate raw audio instead of images by simply changing the position embeddings. As deep learning expands to novel data types, we believe the ease of specifying inductive biases with this class of networks will be a useful tool.

This model was trained on raw classical music clips and uses sparse attention to generate sequences of length 65,000. This corresponds to ~5 seconds of raw audio, and we have concatenated several samples together in each of the clips below.

Loading...

## Code release

Normally, implementing sparse attention would involve slicing query and key matrices in blocks, so to ease experimentation we implemented a set of [block-sparse kernels⁠](/index/block-sparse-gpu-kernels/) which efficiently perform these operations on the the GPU. We open-source these kernels and provide example sparse attention functions in [this repository⁠(opens in a new window)](https://github.com/openai/sparse_attention).

## Future work and limitations

* The sparse attention patterns we introduced are only preliminary steps in the direction of efficient modeling of long sequences. We think exploring different patterns and combinations of sparsity is useful, and that learning sparse patterns is a particularly promising avenue of research for the next generation of neural network architectures.
* Even with the improvements we described above, autoregressive sequence generation still seems impractical for very high resolution images or video. The optimized attention operations we have introduced, however, may be useful primitives to combine with other approaches to modeling high dimensional data, like multi-scale approaches.

If you are interested in advancing AI capabilities and helping further our mission of ensuring they benefit humanity, [we’re hiring⁠](/careers/)!

* [Transformers](/research/index/?tags=transformers)
* [Generative Models](/research/index/?tags=generative-models)
* [Learning Paradigms](/research/index/?tags=learning-paradigms)

## Authors

Rewon Child, Scott Gray

## Acknowledgments

Thanks to Ashish Vaswani for helpful discussions, and Johannes Otterbach, Mark Chen, Prafulla Dhariwal, David Luan, and Lukasz Kaiser for comments on the manuscript.

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
