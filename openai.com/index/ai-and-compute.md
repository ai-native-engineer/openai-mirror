<!-- source: https://openai.com/index/ai-and-compute/ -->

May 16, 2018

[Conclusion](/research/index/conclusion/)

# AI and compute

![AI And Compute](https://images.ctfassets.net/kftzwdyauwt9/ee8676d8-8614-4151-2a721fde65e5/8bf8e46e00c8869512f8b1e2d846c764/image-49.webp?w=3840&q=90&fm=webp)

We’re releasing an analysis showing that since 2012, the amount of compute used in the largest AI training runs has been increasing exponentially with a 3.4-month doubling time (by comparison, Moore’s Law had a 2-year doubling period). Since 2012, this metric has grown by more than 300,000x (a 2-year doubling period would yield only a 7x increase). Improvements in compute have been a key component of AI progress, so as long as this trend continues, it’s worth preparing for the implications of systems far outside today’s capabilities.

#### AlexNet to AlphaGo Zero: 300,000x increase in compute

Loading...

* [Download charts(opens in a new window)](https://cdn.openai.com/ai-and-compute/charts.zip)

## Overview

Three factors drive the advance of AI: algorithmic innovation, data (which can be either supervised data or interactive environments), and the amount of compute available for training. Algorithmic innovation and data are difficult to track, but compute is unusually quantifiable, providing an opportunity to measure one input to AI progress. Of course, the use of massive compute sometimes just exposes the shortcomings of our current algorithms. But at least within many current domains, more compute seems to lead [predictably to better performance⁠(opens in a new window)](https://arxiv.org/abs/1712.00409), and is often complementary to algorithmic advances.

For this analysis, we believe the relevant number is not the speed of a single GPU, nor the capacity of the biggest datacenter, but the amount of compute that is used to train a single model—this is the number most likely to correlate to how powerful our best models are. Compute per model differs greatly from total bulk compute because [limits on parallelism⁠(opens in a new window)](http://learningsys.org/nips17/assets/slides/dean-nips17.pdf) (both hardware and algorithmic) have constrained how big a model can be or how much it can be usefully trained. Of course, important breakthroughs are still made with [modest amounts⁠](/index/ai-and-compute/#appendixrecentnovelresultsthatusedmodestamountsofcompute) of compute—this analysis just covers compute capability.

The trend represents an increase by roughly a factor of 10 each year. It’s been partly driven by custom hardware that allows more operations to be performed per second for a given price (GPUs and TPUs), but it’s been primarily propelled by researchers repeatedly finding ways to use more chips in parallel and being willing to pay the economic cost of doing so.

## Eras

Looking at the graph we can roughly see four distinct eras:

* Before 2012: It was uncommon to use GPUs for ML, making any of the results in the graph difficult to achieve.
* 2012 to 2014: Infrastructure to train on many GPUs was uncommon, so most results used 1-8 GPUs rated at 1-2 TFLOPS for a total of 0.001-0.1 pfs-days.
* 2014 to 2016: Large-scale results used 10-100 GPUs rated at 5-10 TFLOPS, resulting in 0.1-10 pfs-days. Diminishing returns on data parallelism meant that larger training runs had limited value.
* 2016 to 2017: Approaches that allow greater algorithmic parallelism such as [huge batch sizes⁠(opens in a new window)](https://arxiv.org/abs/1711.04325), [architecture search⁠(opens in a new window)](https://arxiv.org/abs/1611.01578), and [expert iteration⁠(opens in a new window)](https://arxiv.org/pdf/1705.08439.pdf), along with specialized hardware such as TPU’s and faster interconnects, have greatly increased these limits, at least for some applications.

AlphaGoZero/AlphaZero is the most visible public example of massive algorithmic parallelism, but many other applications at this scale are now algorithmically possible, and may already be happening in a production context.

## Looking forward

We see multiple reasons to believe that the trend in the graph could continue. Many [hardware startups⁠(opens in a new window)](https://www.nytimes.com/2018/01/14/technology/artificial-intelligence-chip-start-ups.html) are developing AI-specific chips, some of which claim they will achieve a substantial increase in FLOPS/Watt (which is correlated to FLOPS/$) over the next 1–2 years. There may also be gains from simply reconfiguring hardware to do the same number of operations for [less economic cost⁠(opens in a new window)](http://www.fast.ai/2018/04/30/dawnbench-fastai/). On the parallelism side, many of the recent algorithmic innovations described above could in principle be combined multiplicatively—for example, architecture search and massively parallel SGD.

On the other hand, cost will eventually limit the parallelism side of the trend and physics will limit the chip efficiency side. We believe the largest training runs today employ hardware that cost in the single digit millions of dollars to purchase (although the amortized cost is much lower). But the majority of neural net compute today is still spent on inference (deployment), not training, meaning companies can repurpose or afford to purchase much larger fleets of chips for training. Therefore, if sufficient economic incentive exists, we could see even more massively parallel training runs, and thus the continuation of this trend for several more years. The world’s total hardware budget is [1 trillion dollars⁠(opens in a new window)](https://www.statista.com/statistics/422802/hardware-spending-forecast-worldwide/) a year, so absolute limits remain far away. Overall, given the data above, the precedent for exponential trends in computing, work on ML specific hardware, and the economic incentives at play, we think it’d be a mistake to be confident this trend won’t continue in the short term.

Past trends are not sufficient to predict how long the trend will continue into the future, or what will happen while it continues. But even the reasonable potential for rapid increases in capabilities means it is critical to start addressing both [safety⁠](/index/concrete-ai-safety-problems/) and [malicious use of AI⁠](/index/preparing-for-malicious-uses-of-ai/) today. Foresight is essential to [responsible policymaking⁠(opens in a new window)](https://oversight.house.gov/wp-content/uploads/2018/04/Clark-OpenAI-Statement-AI-III-4-18.pdf) and responsible technological development, and we must get out ahead of these trends rather than belatedly reacting to them.

*If you’d like to help make sure that* [*AI progress benefits all of humanity*⁠](/charter/)*,* [*join us*⁠](/careers/) *at OpenAI. Our research and engineering roles range from* [*machine learning researchers*⁠(opens in a new window)](https://jobs.lever.co/openai/588c1d80-4632-4d5c-a535-9f2c8c80c501) *to* [*policy researchers*⁠(opens in a new window)](https://jobs.lever.co/openai/638c06a8-4058-4c3d-9aef-6ee0528fb3bf) *to* [*infrastructure engineers*⁠(opens in a new window)](https://jobs.lever.co/openai/f163bf64-278e-417b-ad2e-5e508a29eb71)*.*

Loading...

## Addendum: Compute used in older headline results

We’ve updated our [analysis⁠](/index/ai-and-compute/#modern) with data that span 1959 to 2012. Looking at the data as a whole, we clearly see two distinct eras of training AI systems in terms of compute-usage: (a) a first era, from 1959 to 2012, which is defined by results that roughly track Moore’s law, and (b) the modern era, from 2012 to now, of results using computational power that substantially outpaces macro trends. The history of investment in AI broadly is usually told as a story of booms and busts, but we don’t see that reflected in the historical trend of compute used by learning systems. It seems that AI winters and periods of excitement had a small effect on compute used to train models[B](#citation-bottom-B) over the last half-century.

#### Two distinct eras of compute usage in training AI systems

Loading...

* [Download charts(opens in a new window)](https://cdn.openai.com/ai-and-compute/charts.zip)

Starting from the [perceptron⁠(opens in a new window)](https://www.nytimes.com/1958/07/13/archives/electronic-brain-teaches-itself.html) in 1959, we see a ~2-year doubling time for the compute used in these historical results—with a 3.4-month doubling time starting in ~2012. It’s difficult to draw a strong conclusion from this data alone, but we believe that this trend is probably due to a combination of the limits on the amount of compute that was possible to use for those results and the willingness to spend on scaling up experiments. [C](#citation-bottom-C)

We followed the same methodology outlined in the original post for this updated analysis. When possible, we programmatically counted the number of FLOPs in the results by implementing the models directly. Since computer architectures varied historically and many papers omitted details of their computational setup, these older data points are more uncertain (our original analysis of post-2012 data aimed to be within a factor of 2–3, but for these pre-2012 data points we aim for an order of magnitude estimate). We’ve also created graphs that provide additional views on the data: one graph lays out compute usage in fundamentals, speech, language, vision, and games over time and another visualizes the error-bar estimates around each data point.

We’re very uncertain about the future of compute usage in AI systems, but it’s difficult to be confident that the recent trend of rapid increase in compute usage will stop, and we see many reasons that the trend could [continue⁠](/index/ai-and-compute/#lookingforward). Based on this analysis, we think policymakers should consider increasing funding[D](#citation-bottom-D) for academic research into AI, as it’s clear that some types of AI research are becoming more computationally intensive and therefore expensive.

* [Compute Scaling](/research/index/?tags=compute-scaling)

## Footnotes

1. A

   A petaflop/s-day (pfs-day) consists of performing 1015 neural net operations per second for one day, or a total of about 1020 operations. The compute-time product serves as a mental convenience, similar to kW-hr for energy. We don’t measure peak theoretical FLOPS of the hardware but instead try to estimate the number of actual operations performed. We count adds and multiplies as separate operations, we count any add or multiply as a single operation regardless of numerical precision (making “FLOP” a slight misnomer), and we ignore [ensemble models⁠(opens in a new window)](http://web.engr.oregonstate.edu/~tgd/publications/mcs-ensembles.pdf). Example calculations that went into this graph are provided in this [appendix⁠](#appendix-methods). Doubling time for line of best fit shown is 3.4 months.
2. B

   Just as in the original analysis, we focus on the costs to train models. This doesn’t include AI systems like expert systems, which attracted substantial investment in the first era.
3. C

   For one vivid account of the history of computing in AI in this period, see the “False Start” section in Hans Moravec’s [article⁠(opens in a new window)](https://jetpress.org/volume1/moravec.htm).
4. D

   We’ve already advocated for additional funding for academia in our [testimony in Congress⁠(opens in a new window)](https://science.house.gov/imo/media/doc/Clark%20Testimony.pdf) this year, and for the creation of dedicated compute clusters to help academia and industry collaboratively benchmark and assess the safety of AI systems in response to a [request for information from NIST⁠(opens in a new window)](https://www.nist.gov/sites/default/files/documents/2019/06/10/nist-ai-rfi-openai-001.pdf)

## Original post

Dario Amodei, Danny Hernandez

## Addendum

Girish Sastry, Jack Clark, Greg Brockman, Ilya Sutskever

## Acknowledgments

The authors thank Katja Grace, Geoffrey Irving, Jack Clark, Thomas Anthony, and Michael Page for assistance with this post.

## Related articles

![Techniques For Training Large Neural Networks](https://images.ctfassets.net/kftzwdyauwt9/62793de4-0f01-42fc-539325d9af36/bc1ac82499fc1dc43f59accdd31d0195/image-9.webp?w=3840&q=90&fm=webp)

[Techniques for training large neural networks

PublicationJun 9, 2022](/index/techniques-for-training-large-neural-networks/)

![Introducing Triton Open Source Gpu Programming For Neural Networks](https://images.ctfassets.net/kftzwdyauwt9/cdce1ebd-19a2-4848-a08ec8c44e18/55b924fc6628318148b7c5c4902551e7/image-18.webp?w=3840&q=90&fm=webp)

[Introducing Triton: Open-source GPU programming for neural networks

ReleaseJul 28, 2021](/index/triton/)

![Scaling Kubernetes To 7 500 Nodes](https://images.ctfassets.net/kftzwdyauwt9/84745f0a-d786-4066-99f031ec2cb2/be1d8d7357f9f5bc35970e058f42c8d0/image-25.webp?w=3840&q=90&fm=webp)

[Scaling Kubernetes to 7,500 nodes

ConclusionJan 25, 2021](/index/scaling-kubernetes-to-7500-nodes/)
