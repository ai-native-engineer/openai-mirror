<!-- source: https://openai.com/index/learning-complex-goals-with-iterated-amplification/ -->

October 22, 2018

[Publication](/research/index/publication/)

# Learning complex goals with iterated amplification

[Read paper(opens in a new window)](https://arxiv.org/abs/1810.08575)

![Learning Complex Goals With Iterated Amplification](https://images.ctfassets.net/kftzwdyauwt9/30581d01-7e0e-4a73-00bd5afa2a81/ca6842af37fe957e7f0b40fd76810f71/image-43.webp?w=3840&q=90&fm=webp)

We’re proposing an AI safety technique called iterated amplification that lets us specify complicated behaviors and goals that are beyond human scale, by demonstrating how to decompose a task into simpler sub-tasks, rather than by providing labeled data or a reward function. Although this idea is in its very early stages and we have only completed experiments on simple toy algorithmic domains, we’ve decided to present it in its preliminary state because we think it could prove to be a scalable approach to AI safety.

If we want to train an ML system to perform a task, we need a training signal—a way to evaluate how well it is doing in order to help it learn. For example, labels in supervised learning or rewards in reinforcement learning are training signals. The formalism of ML usually assumes a training signal is already present and focuses on learning from it, but in reality the training signal has to come from somewhere. If we don’t have a training signal we can’t learn the task, and if we have the wrong training signal, we can get unintended and [sometimes⁠(opens in a new window)](https://arxiv.org/abs/1803.03453) [dangerous⁠](/index/faulty-reward-functions/) [behavior⁠(opens in a new window)](https://arxiv.org/abs/1705.08417). Thus, it would be valuable for both learning new tasks, and for AI safety, to improve our ability to generate training signals.

How do we currently generate training signals? Sometimes, the goal we want can be evaluated algorithmically, like counting up the score in a game of Go or checking whether a set of numbers has been successfully sorted (left panels of figure below). Most real-world tasks don’t lend themselves to an algorithmic training signal, but often we can instead obtain a training signal by having a human either [perform⁠(opens in a new window)](https://arxiv.org/abs/1603.00448) [the⁠(opens in a new window)](https://ai.stanford.edu/~ang/papers/icml04-apprentice.pdf) [task⁠(opens in a new window)](https://arxiv.org/abs/1710.04615) (for example, labeling a training set or demonstrating an RL task), or [judge⁠(opens in a new window)](https://dl.acm.org/citation.cfm?id=1597738%5D) [an⁠(opens in a new window)](https://arxiv.org/abs/1208.0984) [AI’s⁠(opens in a new window)](https://arxiv.org/abs/1701.06049) [performance⁠](/index/learning-from-human-preferences/) on the task (middle panels of figure below). However, many tasks are so complicated that a human can’t judge or perform them—examples might be designing a complicated transit system or managing every detail of the security of a large network of computers (right panels of figure below).

![Example problems which require different kinds of training signal](https://images.ctfassets.net/kftzwdyauwt9/ba811d0e-7f6d-4359-acda813bff28/428ac1a234f0a39f29d7ee29f1b67d06/table1a2x.png?w=3840&q=90&fm=webp)

Iterated amplification is a method for generating a training signal for the latter types of tasks, under certain assumptions. Namely, although a human can’t perform or judge the whole task directly, we assume that a human can, given a piece of the task, identify clear smaller components of which it’s made up. For example, in the networked computer example, a human could break down “defend a collection of servers and routers” into “consider attacks on the servers”, “consider attacks on the routers”, and “consider how the previous two attacks might interact”. Additionally, we assume a human can do very small instances of the task, for example “identify if a specific line in a log file is suspicious”. If these two things hold true, then we can build up a training signal for big tasks from human training signals for small tasks, using the human to coordinate their assembly.

In our implementation of amplification, we start by sampling small subtasks and training the AI system to do them by soliciting demonstrations from humans (who can do these small tasks). We then begin sampling slightly larger tasks, solving them by asking humans to break them up into small pieces, which AI systems trained from the previous step can now solve. We use the solutions to these slightly harder tasks, which were obtained with human help, as a training signal to train AI systems to solve these second-level tasks directly (without human help). We then continue to further composite tasks, iteratively building up a training signal as we go. If the process works, the end result is a totally automated system that can solve highly composite tasks despite starting with no direct training signal for those tasks. This process is somewhat similar to [expert iteration⁠(opens in a new window)](https://arxiv.org/pdf/1705.08439.pdf) (the method used in [AlphaGo Zero⁠(opens in a new window)](https://www.nature.com/articles/nature24270)), except that expert iteration reinforces an existing training signal, while iterated amplification builds up a training signal from scratch. It also has features in common with [several⁠(opens in a new window)](https://arxiv.org/pdf/1807.04640.pdf) [recent⁠(opens in a new window)](https://people.eecs.berkeley.edu/~dawnsong/papers/iclr_2017_recursion.pdf) [learning algorithms⁠(opens in a new window)](https://arxiv.org/abs/1611.02401) that use problem decomposition on-the-fly to solve a problem at test time, but differs in that it operates in settings where there is no prior training signal.

## Experiments

As with our previous work on [AI safety via debate⁠](/index/debate/), working directly on tasks beyond human scale is too hard for a prototype project. Also, using an actual human as training signal introduces complications, so we haven’t done this yet (though we plan to do it in the future). For our first experiments, we instead try to amplify an algorithmic training signal, to show that iterated amplification can work in this simple setting. We also limit our attention to supervised learning (unlike our previous work on [human training signals in RL⁠](/index/learning-from-human-preferences/)). We’ve tried the method on five toy algorithmic tasks. These tasks have direct algorithmic solutions which we pretend we don’t know (for example, find the shortest path between two points on a graph). The problems can also be solved by piecing together small one-step deductions (for example, combining two paths to form a longer path), but it would take exponentially much effort to piece everything together manually. We use iterated amplification to learn the direct algorithm using only the pieces as training signal, thus simulating the situation where a human knows how to combine subpieces of a solution but can’t provide a direct training signal.

On each of these five tasks (permutation powering, sequential assignments, wildcard search, shortest path, and union find), we are able to perform competitively with just directly learning the task via supervised learning, despite being handicapped by not having a direct training signal (the goal here is to match supervised learning with less information, not to surpass it).

![Amplification Diagram](https://images.ctfassets.net/kftzwdyauwt9/dc48f376-e2f9-41d3-82243b6512d8/2ba57edc5704b7fbb424ce67e91ada14/amplification-diagram.svg?w=3840&q=90)

Iterated amplification has comparable performance to supervised learning without ever seeing the ground truth labels

Amplification has features in common with our previous work on [AI safety via debate⁠](/index/debate/). Like debate, it seeks to train tasks that are beyond human ability to directly perform or judge, through an iterative process that allows humans to provide indirect supervision - however the specific approach is different. It also builds on our work on [human feedback⁠](/index/learning-from-human-preferences/), by implementing a reward prediction system, and later versions of it are likely to include feedback from actual humans. So far we’ve explored all of these methods in a preliminary way, and are now working on scaling them up to address more interesting and realistic problems.

If you’re interested in helping us extend tools like iterated amplification to build safe, powerful AI, then consider [joining OpenAI⁠](/careers/).

* [Ethics & Safety](/research/index/?tags=ethics-safety)

## Authors

Paul Christiano, Dario Amodei

## Related articles

![Disrupting malicious > media](https://images.ctfassets.net/kftzwdyauwt9/5080983d-9c4d-4479-17e421d7380a/0b42f77c2478bc5bc7bde3fddfc68462/45.png?w=3840&q=90&fm=webp)

[Disrupting malicious uses of AI by state-affiliated threat actors

SecurityFeb 14, 2024](/index/disrupting-malicious-uses-of-ai-by-state-affiliated-threat-actors/)

![](https://images.ctfassets.net/kftzwdyauwt9/ec66425e-99ca-4314-d04b087f8727/de7341b6a5281c2a220b93a737ce19b0/building-an-early-warning-system-for-llm-aided-biological-threat-creation.jpg?w=3840&q=90&fm=webp)

[Building an early warning system for LLM-aided biological threat creation

PublicationJan 31, 2024](/index/building-an-early-warning-system-for-llm-aided-biological-threat-creation/)

![Democratic Inputs To AI Grant Program Update](https://images.ctfassets.net/kftzwdyauwt9/f50ce1d2-4f61-4ed2-e560c624d631/6f4dd4542898a35d0a91b137f85c9834/Democratic_inputs_to_AI_grant_program_lessons_learned_and_implementation_plans.jpg?w=3840&q=90&fm=webp)

[Democratic inputs to AI grant program: lessons learned and implementation plans

SafetyJan 16, 2024](/index/democratic-inputs-to-ai-grant-program-update/)
