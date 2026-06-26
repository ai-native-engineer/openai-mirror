<!-- source: https://openai.com/index/nonlinear-computation-in-deep-linear-networks/ -->

September 29, 2017

[Conclusion](/research/index/conclusion/)

# Nonlinear computation in deep linear networks

![Nonlinear Computation In Deep Linear Networks](https://images.ctfassets.net/kftzwdyauwt9/d72e3623-cc94-46b3-d27c0c03592d/96cdff076f5580f9b954e310dc908ea2/image-63.webp?w=3840&q=90&fm=webp)

We’ve shown that deep linear networks—as implemented using floating-point arithmetic—are not actually linear and can perform nonlinear computation. We used [evolution strategies⁠](/index/nonlinear-computation-in-linear-networks/#ES) to find parameters in linear networks that exploit this trait, letting us solve non-trivial problems.

Neural networks consist of stacks of a linear layer followed by a nonlinearity like tanh or rectified linear unit. Without the nonlinearity, consecutive linear layers would be in theory mathematically equivalent to a single linear layer. So it’s a surprise that floating point arithmetic is nonlinear enough to yield trainable deep networks.

## Background

Numbers used by computers aren’t perfect mathematical objects, but approximate representations using finite numbers of bits. Floating point numbers are commonly used by computers to represent mathematical objects. Each floating point number is represented by a combination of a fraction and an exponent. In the IEEE’s float32 standard, 23 bits are used for the fraction and 8 for the exponent, and one for the sign.

![Single-precision floating-point format](https://images.ctfassets.net/kftzwdyauwt9/51b46f4b-7d8e-48a0-1a8f685c15fe/c24733ff3e972fca5b2dcd755c924392/image2.png?w=3840&q=90&fm=webp)

Image Credit: [Wikipedia⁠(opens in a new window)](https://en.wikipedia.org/wiki/Single-precision_floating-point_format)

As a consequence of these conventions and the binary format used, the smallest normal non-zero number (in binary) is *1.0..0 x 2^-126*, which we refer to as *min* going forward. However, the next representable number is *1.0..01 x 2^-126*, which we can write as *min + 0.0..01 x 2^-126*. It is evident that the gap between the 2nd number is by a factor of 2^20 smaller than gap between 0 and min. In float32, when numbers are smaller than the smallest representable number they get mapped to zero. Due to this ‘underflow’, around zero all computation involving floating point numbers becomes nonlinear.

An exception to these restrictions is [denormal numbers⁠(opens in a new window)](https://en.wikipedia.org/wiki/Denormal_number), which can be disabled on some computing hardware. While the GPU and cuBLAS have denormals enabled by default, TensorFlow builds all its primitives with denormals off (with the `ftz=true` flag set). This means that any non-matrix multiply operation written in TensorFlow has an implicit non-linearity following it (provided the scale of computation is near 1e-38).

So, while in general the difference between any “mathematical” number and their normal float representation is small, around zero there is a large gap and the approximation error can be very significant.

![Image1](https://images.ctfassets.net/kftzwdyauwt9/86221d5b-7469-4ee6-8d1e713769d5/668439144daf11b05a7f7ad84b799310/image1.png?w=3840&q=90&fm=webp)

This can lead to some odd effects where the familiar rules of mathematics stop applying. For instance, (a+b)×c (a + b) \times c (a+b)×c becomes unequal to a ×c+b× c \times c + b \times c ×c+b× c

For example if you set  a=0.4×min a = 0.4 \times min  a=0.4×min, b=0.5×min b = 0.5 \times min b=0.5×min, and c=1/ min c = 1 / min c=1/ min.

Then: (a+b)×c=(0.4×min+0.5×min)×1/min=(0+0)×1/min=0 (a+b) \times c = (0.4 \times min + 0.5 \times min) \times 1 / min = (0 + 0) \times 1 / min = 0 (a+b)×c=(0.4×min+0.5×min)×1/min=(0+0)×1/min=0.However: (a×c)+(b×c)=0.4×min/min+0.5×min×1/min= 0.9 (a \times c) + (b \times c) = 0.4 \times min / min + 0.5 \times min \times 1 / min = 0.9 (a×c)+(b×c)=0.4×min/min+0.5×min×1/min= 0.9.

In another example, we can set a=2.5×min a = 2.5 \times min a=2.5×min, b=−1.6×min b = -1.6 \times min b=−1.6×min, and  c=1× min c = 1 \times min  c=1× min.

Then:  (a+b)+c=(0)+1×min=min (a+b) + c = (0) + 1 \times min = min  (a+b)+c=(0)+1×min=min.However: (b+c)+a=(0×min)+2.5×min=2.5× min (b+c) + a = (0 \times min) + 2.5 \times min = 2.5 \times min (b+c)+a=(0×min)+2.5×min=2.5× min.

At this smallest scale the fundamental addition operation has become nonlinear!

## Exploiting Nonlinearities with Evolution Strategies

We wanted to know if this inherent nonlinearity could be exploited as a computational nonlinearity, as this would let deep linear networks perform nonlinear computations. The challenge is that modern differentiation libraries are blind to these nonlinearities at the smallest scale. As such, it would be difficult or impossible to train a neural network to exploit them via backpropagation.

We can use [evolution strategies (ES)⁠(opens in a new window)](https://blog.openai.com/evolution-strategies/) to estimate gradients without having to rely on symbolic differentiation. Using ES we can indeed exploit the near-zero behavior of float32 as a computational nonlinearity. When trained on MNIST a deep linear network trained via backpropagation achieves a training accuracy of 94% and a testing accuracy of 92%. In contrast, the same linear network can achieve >99% training and 96.7% test accuracy when trained with ES and ensuring that the activations are sufficiently small to be in the nonlinear range of float32. This increase in training performance is due to ES exploiting the nonlinearities in the float32 representation. These powerful nonlinearities allow any layer to generate novel features which are nonlinear combinations of lower level features. Here is the network structure:

#### Python

```` ```
1

x = tf.placeholder(dtype=tf.float32, shape=[batch_size,784])

2

y = tf.placeholder(dtype=tf.float32, shape=[batch_size,10])

3

4

w1 = tf.Variable(np.random.normal(scale=np.sqrt(2./784),size=[784,512]).astype(np.float32))

5

b1 = tf.Variable(np.zeros(512,dtype=np.float32))

6

w2 = tf.Variable(np.random.normal(scale=np.sqrt(2./512),size=[512,512]).astype(np.float32))

7

b2 = tf.Variable(np.zeros(512,dtype=np.float32))

8

w3 = tf.Variable(np.random.normal(scale=np.sqrt(2./512),size=[512,10]).astype(np.float32))

9

b3 = tf.Variable(np.zeros(10,dtype=np.float32))

10

11

params = [w1,b1,w2,b2,w3,b3]

12

nr_params = sum([np.prod(p.get_shape().as_list()) for p in params])

13

scaling = 2**125

14

15

def get_logits(par):

16

h1 = tf.nn.bias_add(tf.matmul(x , par[0]), par[1]) / scaling

17

h2 = tf.nn.bias_add(tf.matmul(h1, par[2]) , par[3] / scaling)

18

o =   tf.nn.bias_add(tf.matmul(h2, par[4]), par[5]/ scaling)*scaling

19

return o
``` ````

Beyond MNIST, we think other interesting experiments could be extending this work to recurrent neural networks, or to exploit nonlinear computation to improve complex machine learning tasks like language modeling and translation. We’re excited to explore this capability with our fellow researchers.

* [Software & Engineering](/research/index/?tags=software-engineering)

## Author

Jakob Foerster

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
