<!-- source: https://deploymentsafety.openai.com/gpt-5-sensitive-conversations/ -->

When we launched GPT-5, we [noted](https://openai.com/index/gpt-5-system-card/) in the
system card that we were working to establish better benchmarks and to
continue to strengthen model safety in areas related to mental and
emotional distress. On October 3, we deployed an [update](https://help.openai.com/en/articles/9624314-model-release-notes)
that reflected those efforts, improving ChatGPT’s default model to
better recognize and support people in moments of distress. In this
effort, we worked with more than 170 mental health experts to help
ChatGPT more reliably recognize signs of distress, respond with care,
and guide people toward real-world support–reducing responses that fall
short of our desired behavior by 65-80%.

We are publishing a related [blog
post](https://openai.com/index/strengthening-chatgpt-responses-in-sensitive-conversations/) that gives more information about this work, and this addendum
to the GPT-5 system card to share baseline safety evaluations. These
evaluations compare the [August
15 version](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#h_6b1adafe01) of ChatGPT’s default model, also known as GPT-5 Instant,
to the updated one launched October 3.

We evaluate completions using LLM-based grading models. The primary
metric is not\_unsafe, checking that the model did not produce output
that is disallowed under the relevant OpenAI policy.

With this launch, we created the following new evaluation sets:

* Emotional Reliance not\_unsafe - tests that the model does not produce
  disallowed content under our policies related to unhealthy emotional
  dependence or attachment to ChatGPT
* Mental Health not\_unsafe - tests that the model does not produce
  disallowed content under our policies in situations where there are
  signs that a user may be experiencing isolated delusions, psychosis, or
  mania

Our new evaluations for emotional reliance and mental health, like
the existing evaluations in this Production Benchmarks set, were
deliberately intended to be challenging. They were built around cases in
which our existing models were not yet giving ideal responses, and this
is reflected in the initial scores below. Error rates are not
representative of average production traffic.

Note these are new evaluations and may evolve over time.

### Table 1: Disallowed Content Evaluations - Production Benchmarks (higher is better)

Table 1. Disallowed Content Evaluations - Production Benchmarks (higher is better)

| **Category** | **gpt-5-aug-15** | **gpt-5-oct-3** |
| non-violent hate | 0.800 | 0.853 |
| personal-data | 0.876 | 0.908 |
| harassment/threatening | 0.653 | 0.706 |
| sexual/exploitative | 0.785 | 0.910 |
| sexual/minors | 0.906 | 0.959 |
| extremism | 0.933 | 0.925 |
| hate/threatening | 0.780 | 0.791 |
| illicit/nonviolent | 0.720 | 0.800 |
| illicit/violent | 0.782 | 0.834 |
| emotional reliance | 0.507\* | 0.976 |
| mental health | 0.273\* | 0.926 |
| self-harm/intent | 0.874 | 0.933 |
| self-harm/instructions | 0.805 | 0.890 |

\*These are new evaluations that were not available when the August 15
model launched. We have run them retrospectively for these launches.

We further evaluate the robustness of the models to jailbreaks:
adversarial prompts that purposely try to circumvent model refusals for
content it’s not supposed to produce. We evaluate using the following
approach:

* StrongReject [[1](/gpt-5-sensitive-conversations/references#ref-souly2024strongreject "Alexandra Souly, Qingyuan Lu, Dillon Bowen, Tu Trinh, Elvis Hsieh, Sana Pandey, et al. A strongreject for empty jailbreaks. arXiv preprint arXiv:2402.10260 .")]: inserts a known jailbreak
  into an example from the above safety refusal eval. We then run it
  through the same policy graders we use for disallowed content checks. We
  test jailbreak techniques on base prompts across several harm
  categories, and evaluate for not\_unsafe according to relevant
  policy.

### Table 2: Jailbreak evaluations

Table 2. Jailbreak evaluations

| **Category** | **metric** | **gpt-5-aug-15** | **gpt-5-oct-3** |
| --- | --- | --- | --- |
| illicit/non‑violent‐crime prompts | not\_unsafe | 0.926 | 0.957 |
| violence prompts | not\_unsafe | 0.942 | 0.968 |
| abuse / disinformation / hate prompts | not\_unsafe | 0.967 | 0.981 |
| sexual‑content prompts | not\_unsafe | 0.954 | 0.969 |

We ran the image input evaluations introduced with ChatGPT agent,
that evaluate for not\_unsafe model output, given disallowed combined
text and image input.

### Table 3: Image input evaluations (higher is better)

We evaluate hallucinations via SimpleQA, a diverse dataset of
four-thousand fact-seeking questions with short answers and measures
model accuracy for attempted answers.

We consider two metrics: accuracy (did the model answer the question
correctly) and hallucination rate (checking how often the model
hallucinated). Further details on hallucinations in GPT-5, including our
work on newer evaluations and progress in our reasoning models, can be
found in the original [GPT-5 system
card](https://cdn.openai.com/gpt-5-system-card.pdf).

### Table 4: Hallucination evaluation

Table 4. Hallucination evaluation

| **Dataset** | **Metric** | **gpt-5-aug-15** | **gpt-5-oct-3** |
| --- | --- | --- | --- |
| SimpleQA | accuracy (higher is better) | 0.46 | .44 |
|  | hallucination rate (lower is better) | 0.49 | .52 |

   Alexandra Souly, Qingyuan
   Lu, Dillon Bowen, Tu Trinh, Elvis Hsieh, Sana Pandey, et al. A
   strongreject for empty jailbreaks. *arXiv preprint
   arXiv:2402.10260*.
