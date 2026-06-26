<!-- source: https://openai.com/index/multimodal-neurons/ -->

March 4, 2021

[Milestone](/research/index/milestone/)

# Multimodal neurons in artificial neural networks

[Read paper(opens in a new window)](https://distill.pub/2021/multimodal-neurons/)[(opens in a new window)](https://github.com/openai/CLIP-featurevis)

![Multimodal Neurons](https://images.ctfassets.net/kftzwdyauwt9/e16f419f-09bf-4266-7ca3cdd2ae33/0a11dd23053f257828e7c68a815cd632/multimodal-neurons.png?w=3840&q=90&fm=webp)

We’ve discovered neurons in CLIP that respond to the same concept whether presented literally, symbolically, or conceptually. This may explain CLIP’s accuracy in classifying surprising visual renditions of concepts, and is also an important step toward understanding the associations and biases that CLIP and similar models learn.

Fifteen years ago, Quiroga et al.[1](#citation-bottom-1) discovered that the human brain possesses multimodal neurons. These neurons respond to clusters of abstract concepts centered around a common high-level theme, rather than any specific visual feature. The most famous of these was the “Halle Berry” neuron, a neuron featured in both [Scientific American⁠(opens in a new window)](https://www.scientificamerican.com/article/one-face-one-neuron) and [The New York Times⁠(opens in a new window)](https://www.nytimes.com/2005/07/05/science/a-neuron-with-halle-berrys-name-on-it.html), that responds to photographs, sketches, and the text “Halle Berry” (but not other names).

Two months ago, OpenAI announced [CLIP⁠](/index/clip/), a general-purpose vision system that matches the performance of a ResNet-50,[2](#citation-bottom-2) but outperforms existing vision systems on some of the most challenging datasets. Each of these challenge datasets, *ObjectNet*, *ImageNet Rendition*, and *ImageNet Sketch*, stress tests the model’s robustness to not recognizing not just simple distortions or changes in lighting or pose, but also to complete abstraction and reconstruction—sketches, cartoons, and even statues of the objects.

Now, we’re releasing our discovery of the presence of multimodal neurons in CLIP. One such neuron, for example, is a “Spider-Man” neuron (bearing a remarkable resemblance to the “Halle Berry” neuron) that responds to an image of a spider, an image of the text “spider,” and the comic book character “Spider-Man” either in costume or illustrated.

Our discovery of multimodal neurons in CLIP gives us a clue as to what may be a common mechanism of both synthetic and natural vision systems—abstraction. We discover that the highest layers of CLIP organize images as a loose semantic collection of ideas, providing a simple explanation for both the model’s versatility and the representation’s compactness.

Loading...

Using the tools of interpretability, we give an unprecedented look into the rich visual concepts that exist within the weights of CLIP. Within CLIP, we discover high-level concepts that span a large subset of the human visual lexicon—geographical regions, facial expressions, religious iconography, famous people and more. By probing what each neuron affects downstream, we can get a glimpse into how CLIP performs its classification.

## Multimodal neurons in CLIP

Our [paper⁠(opens in a new window)](https://distill.pub/2021/multimodal-neurons/) builds on nearly a decade of research into interpreting convolutional networks,[3](#citation-bottom-3), [4](#citation-bottom-4), [5](#citation-bottom-5), [6](#citation-bottom-6), [7](#citation-bottom-7), [8](#citation-bottom-8), [9](#citation-bottom-9), [10](#citation-bottom-10), [11](#citation-bottom-11), [12](#citation-bottom-12) beginning with the observation that many of these classical techniques are directly applicable to CLIP. We employ two tools to understand the activations of the model: *feature visualization*,[6](#citation-bottom-6), [5](#citation-bottom-5), [12](#citation-bottom-12) which maximizes the neuron’s firing by doing gradient-based optimization on the input, and *dataset examples*,[4](#citation-bottom-4) which looks at the distribution of maximal activating images for a neuron from a dataset.

Using these simple techniques, we’ve found the majority of the neurons in CLIP RN50x4 (a ResNet-50 scaled up 4x using the EfficientNet scaling rule) to be readily interpretable. Indeed, these neurons appear to be extreme examples of “multi-faceted neurons,” [11](#citation-bottom-11) neurons that respond to multiple distinct cases, only at a higher level of abstraction.

Loading...

Indeed, we were surprised to find many of these categories appear to mirror neurons in the medial temporal lobe documented in epilepsy patients with intracranial depth electrodes. These include neurons that respond to emotions,[17](#citation-bottom-17) animals,[18](#citation-bottom-18) and famous people.[1](#citation-bottom-1)

But our investigation into CLIP reveals many more such strange and wonderful abstractions, including neurons that appear to count [[17⁠(opens in a new window)](https://microscope.openai.com/models/contrastive_4x/image_block_4_5_Add_6_0/17), [202⁠(opens in a new window)](https://microscope.openai.com/models/contrastive_4x/image_block_4_5_Add_6_0/202), [310⁠(opens in a new window)](https://microscope.openai.com/models/contrastive_4x/image_block_4_5_Add_6_0/310)], neurons responding to art styles [[75⁠(opens in a new window)](https://microscope.openai.com/models/contrastive_4x/image_block_4_5_Add_6_0/75), [587⁠(opens in a new window)](https://microscope.openai.com/models/contrastive_4x/image_block_4_5_Add_6_0/587), [122⁠(opens in a new window)](https://microscope.openai.com/models/contrastive_4x/image_block_4_5_Add_6_0/122)], even images with evidence of digital alteration [[1640⁠(opens in a new window)](https://microscope.openai.com/models/contrastive_4x/image_block_4_5_Add_6_0/1640)].

## Absent concepts

While this analysis shows a great breadth of concepts, we note that a simple analysis on a neuron level cannot represent a complete documentation of the model’s behavior. The authors of CLIP have demonstrated, for example, that the model is capable of very precise geolocation,[19](#citation-bottom-19) (Appendix E.4, Figure 20) with a granularity that extends down to the level of a city and even a neighborhood. In fact, we offer an anecdote: we have noticed, by running our own personal photos through CLIP, that CLIP can often recognize if a photo was taken in San Francisco, and sometimes even the neighborhood (e.g., “Twin Peaks”).

Despite our best efforts, however, we have not found a “San Francisco” neuron, nor did it seem from attribution that San Francisco decomposes nicely into meaningful unit concepts like “California” and “city.” We believe this information to be encoded within the activations of the model somewhere, but in a more exotic way, either as a direction or as some other more complex manifold. We believe this to be a fruitful direction for further research.

## How multimodal neurons compose

These multimodal neurons can give us insight into understanding how CLIP performs classification. With a sparse linear probe,[19](#citation-bottom-19) we can easily inspect CLIP’s weights to see which concepts combine to achieve a final classification for ImageNet classification:

Loading...

For text classification, a key observation is that these concepts are contained within neurons in a way that, similar to the word2vec objective,[20](#citation-bottom-20) is *almost linear*. The concepts, therefore, form a simple algebra that behaves similarly to a linear probe. By linearizing the attention, we too can inspect any sentence, much like a linear probe, as shown below:

Loading...

## Fallacies of abstraction

The degree of abstraction in CLIP surfaces a new vector of attack that we believe has not manifested in previous systems. Like many deep networks, the representations at the highest layers of the model are completely dominated by such high-level abstractions. What distinguishes CLIP, however, is a matter of degree—CLIP’s multimodal neurons generalize across the literal and the iconic, which may be a double-edged sword.

Through a series of carefully-constructed experiments, we demonstrate that we can exploit this reductive behavior to fool the model into making absurd classifications. We have observed that the excitations of the neurons in CLIP are often controllable by its response to *images of text*, providing a simple vector of attacking the model.

The finance neuron [[1330⁠(opens in a new window)](https://microscope.openai.com/models/contrastive_4x/image_block_4_5_Add_6_0/1330)], for example, responds to images of piggy banks, but also responds to the string “$$$”. By forcing the finance neuron to fire, we can fool our model into classifying a dog as a piggy bank.

Loading...

## Attacks in the wild

We refer to these attacks as *typographic attacks*. We believe attacks such as those described above are far from simply an academic concern. By exploiting the model’s ability to read text robustly, we find that even *photographs of hand-written text* can often fool the model. Like the Adversarial Patch,[21](#citation-bottom-21) this attack works in the wild; but unlike such attacks, it requires no more technology than pen and paper.

Loading...

We also believe that these attacks may also take a more subtle, less conspicuous form. An image, given to CLIP, is abstracted in many subtle and sophisticated ways, and these abstractions may over-abstract common patterns—oversimplifying and, by virtue of that, overgeneralizing.

## Bias and overgeneralization

Our model, despite being trained on a curated subset of the internet, still inherits its many unchecked biases and associations. Many associations we have discovered appear to be benign, but yet we have discovered several cases where CLIP holds associations that could result in representational harm, such as denigration of certain individuals or groups.

We have observed, for example, a “Middle East” neuron [[1895]⁠(opens in a new window)](https://microscope.openai.com/models/contrastive_v2/image_block_4_2_Add_6_0/1895) with an association with terrorism; and an “immigration” neuron [[395]⁠(opens in a new window)](https://microscope.openai.com/models/contrastive_v2/image_block_4_2_Add_6_0/395) that responds to Latin America. We have even found a neuron that fires for both dark-skinned people and gorillas [[1257⁠(opens in a new window)](https://microscope.openai.com/models/contrastive_4x/image_block_4_5_Add_6_0/1257)], mirroring earlier photo tagging incidents in other models we consider unacceptable.[22](#citation-bottom-22)

These associations present obvious challenges to applications of such powerful visual systems.[A](#citation-bottom-A) Whether fine-tuned or used zero-shot, it is likely that these biases and associations will remain in the system, with their effects manifesting in both visible and nearly invisible ways during deployment. Many biased behaviors may be difficult to anticipate a priori, making their measurement and correction difficult. We believe that these tools of interpretability may aid practitioners the ability to preempt potential problems, by discovering some of these associations and ambigiuities ahead of time.

Our own understanding of CLIP is still evolving, and we are still determining if and how we would release large versions of CLIP. We hope that further community exploration of the released versions as well as the tools we are announcing today will help advance general understanding of multimodal systems, as well as inform our own decision-making.

## Conclusion

Alongside the publication of “Multimodal Neurons in Artificial Neural Networks,” we are also releasing some of the tools we have ourselves used to understand CLIP—the OpenAI [Microscope⁠(opens in a new window)](https://microscope.openai.com/) catalog has been updated with feature visualizations, dataset examples, and text feature visualizations for every neuron in CLIP RN50x4. We are also releasing the weights of CLIP [RN50x4⁠(opens in a new window)](https://github.com/openai/CLIP) and [RN101⁠(opens in a new window)](https://github.com/openai/CLIP) to further accommodate such research. We believe these investigations of CLIP only scratch the surface in understanding CLIP’s behavior, and we invite the research community to join in improving our understanding of CLIP and models like it.

* [Visit OpenAI Microscope(opens in a new window)](https://microscope.openai.com)

* [CLIP](/research/index/?tags=technology-clip)
* [Generative Models](/research/index/?tags=generative-models)
* [Transformers](/research/index/?tags=transformers)
* [Language](/research/index/?tags=language)
* [Ethics & Safety](/research/index/?tags=ethics-safety)

## Footnotes

1. A

   Note that the released CLIP models are intended strictly for research purposes. See the associated [model card⁠(opens in a new window)](https://github.com/openai/CLIP/blob/main/model-card.md).

## References

1. 1

   Quiroga, R. Q., Reddy, L., Kreiman, G., Koch, C., & Fried, I. (2005). [Invariant visual representation by single neurons in the human brain⁠(opens in a new window)](https://www.nature.com/articles/nature03687). *Nature, 435*(7045), 1102-1107.
2. 2

   He, K., Zhang, X., Ren, S., & Sun, J. (2016). [Deep residual learning for image recognition⁠(opens in a new window)](https://openaccess.thecvf.com/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf). In *Proceedings of the IEEE conference on computer vision and pattern recognition* (pp. 770-778).
3. 3

   Erhan, D., Bengio, Y., Courville, A., & Vincent, P. (2009). [Visualizing higher-layer features of a deep network⁠(opens in a new window)](https://www.researchgate.net/profile/Aaron_Courville/publication/265022827_Visualizing_Higher-Layer_Features_of_a_Deep_Network/links/53ff82b00cf24c81027da530.pdf). *University of Montreal, 1341*(3), 1.
4. 4

   Szegedy, C., Zaremba, W., Sutskever, I., Bruna, J., Erhan, D., Goodfellow, I., & Fergus, R. (2013). [Intriguing properties of neural networks⁠(opens in a new window)](https://arxiv.org/abs/1312.6199). *arXiv preprint arXiv:1312.6199*.
5. 5

   Mahendran, A., & Vedaldi, A. (2014). [Understanding Deep Image Representations by Inverting Them⁠(opens in a new window)](https://arxiv.org/abs/1412.0035). *arXiv preprint arXiv:1412.0035*.
6. 6

   Nguyen, A., Yosinski, J., & Clune, J. (2015). [Deep neural networks are easily fooled: High confidence predictions for unrecognizable images⁠(opens in a new window)](https://www.cv-foundation.org/openaccess/content_cvpr_2015/html/Nguyen_Deep_Neural_Networks_2015_CVPR_paper.html). In *Proceedings of the IEEE conference on computer vision and pattern recognition* (pp. 427-436).
7. 7

   Øygard, A. (2015). [Visualizing GoogLeNet Classes⁠(opens in a new window)](https://www.auduno.com/2015/07/29/visualizing-googlenet-classes/). *Accessed in*.
8. 8

   Mordvintsev, A., Olah, C., & Tyka, M. (2015). [Inceptionism: Going deeper into neural networks⁠(opens in a new window)](https://ai.googleblog.com/2015/06/inceptionism-going-deeper-into-neural.html).
9. 9

   Nguyen, A., Dosovitskiy, A., Yosinski, J., Brox, T., & Clune, J. (2016). [Synthesizing the preferred inputs for neurons in neural networks via deep generator networks⁠(opens in a new window)](https://arxiv.org/abs/1605.09304). *arXiv preprint arXiv:1605.09304*.
10. 10

    Nguyen, A., Clune, J., Bengio, Y., Dosovitskiy, A., & Yosinski, J. (2017). [Plug & play generative networks: Conditional iterative generation of images in latent space⁠(opens in a new window)](http://openaccess.thecvf.com/content_cvpr_2017/html/Nguyen_Plug__Play_CVPR_2017_paper.html). In *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition* (pp. 4467-4477).
11. 11

    Nguyen, A., Yosinski, J., & Clune, J. (2016). [Multifaceted feature visualization: Uncovering the different types of features learned by each neuron in deep neural networks⁠(opens in a new window)](https://arxiv.org/abs/1602.03616). *arXiv preprint arXiv:1602.03616*.
12. 12

    Olah, C., Mordvintsev, A., & Schubert, L. (2017). [Feature visualization⁠(opens in a new window)](https://distill.pub/2017/feature-visualization). *Distill*, 2(11), e7.
13. 13

    Goh, G., et al. (2021). [Multimodal Neurons in Artificial Neural Networks⁠(opens in a new window)](https://distill.pub/2021/multimodal-neurons/#imagenet-challenge). *Distill*.
14. 14

    Miller, G. A. (1995). [WordNet: a lexical database for English⁠(opens in a new window)](https://dl.acm.org/doi/abs/10.1145/219717.219748). *Communications of the ACM*, 38(11), 39-41.
15. 15

    Crawford, K. & Paglen, T. (2019). [Excavating AI: the politics of images in machine learning training sets⁠(opens in a new window)](https://excavating.ai/). *Excavating AI*.
16. 16

    Hanna, A., Denton, E., Amironesei, R,, Smart A., Nicole, H. [Lines of Sight⁠(opens in a new window)](https://logicmag.io/commons/lines-of-sight/). *Logic Magazine*.
17. 17

    Fried, I., MacDonald, K. A., & Wilson, C. L. (1997). [Single neuron activity in human hippocampus and amygdala during recognition of faces and objects⁠(opens in a new window)](https://www.sciencedirect.com/science/article/pii/S0896627300803153). *Neuron, 18*(5), 753-765.
18. 18

    Kreiman, G., Koch, C., & Fried, I. (2000). [Category-specific visual responses of single neurons in the human medial temporal lobe⁠(opens in a new window)](https://www.nature.com/articles/nn0900_946). *Nature neuroscience, 3*(9), 946-953.
19. 19

    Radford, A., Jozefowicz, R., & Sutskever, I. (2017). [Learning to generate reviews and discovering sentiment⁠(opens in a new window)](https://arxiv.org/abs/1704.01444). *arXiv preprint arXiv:1704.01444*.
20. 20

    Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). [Efficient estimation of word representations in vector space⁠(opens in a new window)](https://arxiv.org/abs/1301.3781). *arXiv preprint arXiv:1301.3781*.
21. 21

    Brown, T. B., Mané, D., Roy, A., Abadi, M., & Gilmer, J. (2017). [Adversarial patch⁠(opens in a new window)](https://arxiv.org/abs/1712.09665). *arXiv preprint arXiv:1712.09665*.
22. 22

    Crawford, K. & Paglen, T. (2019). [Excavating AI: the politics of images in machine learning training sets⁠(opens in a new window)](https://excavating.ai/). *Excavating AI*.

## Authors

Gabriel Goh, Chelsea Voss, Daniela Amodei, Shan Carter, Michael Petrov, Justin Jay Wang, Nick Cammarata, Chris Olah

## Acknowledgments

Sandhini Agarwal, Greg Brockman, Miles Brundage, Jeff Clune, Steve Dowling, Jonathan Gordon, Gretchen Krueger, Faiz Mandviwalla, Vedant Misra, Reiichiro Nakano, Ashley Pilipiszyn, Alec Radford, Aditya Ramesh, Pranav Shyam, Ilya Sutskever, Martin Wattenberg & Hannah Wong

## Related articles

![Democratic Inputs To AI Grant Program Update](https://images.ctfassets.net/kftzwdyauwt9/f50ce1d2-4f61-4ed2-e560c624d631/6f4dd4542898a35d0a91b137f85c9834/Democratic_inputs_to_AI_grant_program_lessons_learned_and_implementation_plans.jpg?w=3840&q=90&fm=webp)

[Democratic inputs to AI grant program: lessons learned and implementation plans

SafetyJan 16, 2024](/index/democratic-inputs-to-ai-grant-program-update/)

![Practices For Governing Agentic AI Systems](https://images.ctfassets.net/kftzwdyauwt9/dfdeca52-d054-4ce9-18d684209ff9/f3a2e6e71ebefb70fca386ff7bbb9d92/practices-for-governing-agentic-ai-systems.jpg?w=3840&q=90&fm=webp)

[Practices for Governing Agentic AI Systems

PublicationDec 14, 2023](/index/practices-for-governing-agentic-ai-systems/)

![Confidence-Building Measures for Artificial Intelligence Workshop proceedings](https://images.ctfassets.net/kftzwdyauwt9/Z9HqTzpgkOEFSdz1i0Mkl/4a794853a9d3412851d52a0e18d407f3/Confidence-Building_Measures_for_Artificial_Intelligence__Workshop_proceedings.png?w=3840&q=90&fm=webp)

[Confidence-Building Measures for Artificial Intelligence: Workshop proceedings

ConclusionAug 1, 2023](/index/confidence-building-measures-for-artificial-intelligence/)
