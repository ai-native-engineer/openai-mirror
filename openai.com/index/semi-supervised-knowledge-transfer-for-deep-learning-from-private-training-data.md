<!-- source: https://openai.com/index/semi-supervised-knowledge-transfer-for-deep-learning-from-private-training-data/ -->

October 18, 2016

[Publication](/research/index/publication/)

# Semi-supervised knowledge transfer for deep learning from private training data

[Read paper(opens in a new window)](https://arxiv.org/abs/1610.05755)

![Semi Supervised Knowledge Transfer For Deep Learning From Private Training Data](https://images.ctfassets.net/kftzwdyauwt9/d11b8795-7bf4-41ff-dc33663470c3/fae7f11e7e5d05fbdf67c2d8ae381948/semi-supervised-knowledge-transfer-for-deep-learning-from-private-training-data.png?w=3840&q=90&fm=webp)

## Abstract

Some machine learning applications involve training data that is sensitive, such as the medical histories of patients in a clinical trial. A model may inadvertently and implicitly store some of its training data; careful analysis of the model may therefore reveal sensitive information.

To address this problem, we demonstrate a generally applicable approach to providing strong privacy guarantees for training data: Private Aggregation of Teacher Ensembles (PATE). The approach combines, in a black-box fashion, multiple models trained with disjoint datasets, such as records from different subsets of users. Because they rely directly on sensitive data, these models are not published, but instead used as "teachers" for a "student" model. The student learns to predict an output chosen by noisy voting among all of the teachers, and cannot directly access an individual teacher or the underlying data or parameters. The student's privacy properties can be understood both intuitively (since no single teacher and thus no single dataset dictates the student's training) and formally, in terms of differential privacy. These properties hold even if an adversary can not only query the student but also inspect its internal workings.

Compared with previous work, the approach imposes only weak assumptions on how teachers are trained: it applies to any model, including non-convex models like DNNs. We achieve state-of-the-art privacy/utility trade-offs on MNIST and SVHN thanks to an improved privacy analysis and semi-supervised learning.

* [Ethics & Safety](/research/index/?tags=ethics-safety)

## Authors

Nicolas Papernot, Martín Abadi, Úlfar Erlingsson, Ian Goodfellow, Kunal Talwar

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
