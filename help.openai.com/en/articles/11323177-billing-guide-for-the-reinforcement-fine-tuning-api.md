<!-- source: https://help.openai.com/en/articles/11323177-billing-guide-for-the-reinforcement-fine-tuning-api -->

# Billing guide for the Reinforcement Fine Tuning API

How billing works for the RFT API

Updated: 2 days ago

# How billing works for RFT

Reinforcement Fine‑Tuning (RFT) allows you to optimize the performance of OpenAI’s reasoning models using reinforcement learning. Unlike our supervised or preference fine‑tuning offerings, which are billed by the number of tokens in the training dataset, RFT is billed based on the time your training run spends performing the core machine learning work.

This guide explains what counts as billable training time, how we handle pauses and cancellations, and how your configuration choices can affect cost.

## Pricing

* **Compute**: $100 per hour of wall-clock time spent in the core training loop for `o4-mini-2025-04-16`. Charges are prorated to the second and rounded to two decimal places on the invoice (e.g., 2.55 hours).
* **Model grader usage**: If you use an OpenAI model to "grade" outputs during training, the tokens consumed by those grading calls are billed separately at our standard API rates after training completes.

We only charge for training work that actually updates your model (what we call "captured forward progress").

## What we bill for

We bill for the time your training worker spends actively training your model, specifically:

* Generating samples from your model during the fine-tuning process (known as “rollouts”)
* Evaluating those outputs with one or more graders that you have defined on the job ([learn more about graders](https://platform.openai.com/docs/guides/graders))
* Computing and applying weight updates based on the grades (backpropagation).
* Running any validation (evaluation) steps you have configured.

Most graders are “free” to run, which means we don’t charge extra for their use outside of the amount of time that they contribute to the core training loop. The exception to this is for model graders, where we also tally the tokens those graders consume during the above activities. These tokens appear as a separate line item on your invoice. Tokens consumed by model graders are billed at normal inference rates ([OpenAI pricing](https://openai.com/api/pricing/)).

## What we do NOT bill for

We do not charge for time spent:

* Validating or inspecting your dataset before training starts.
* Safety checks on your dataset.
* Waiting in a queue for compute resources.
* Downloading model weights or datasets.
* Preparing (rendering) your dataset into our training format.
* Post‑training safety evaluations of your fine‑tuned model.

If training work is lost due to an error on our side (for example, if a worker crashes and has to roll back to a previous checkpoint), you are not charged for the lost compute time or grader tokens. More details on this in the next section.

## Captured forward progress and billing events

Training consists of many small updates to your model. We track how many of these updates complete successfully. Charges are based on the compute time and grader tokens associated with these successful updates.

We issue a charge when one of the following "billing events" occurs:

* Training completes successfully.
* You pause training.
* You cancel training.
* Training fails.

Each charge covers the incremental work done since the last charge. For example:

* If you pause a run, we save a checkpoint and charge you for the compute time and grader tokens used since the last charge.
* When you resume, training continues from the checkpoint. The next charge (on completion, another pause, cancellation, or failure) will cover only the additional work done after the resume.
* If you cancel a run, we charge you for the work done up to the cancellation.
* If training fails and work since the last charge is lost, you are not billed for the lost portion.

This "captured forward progress" approach ensures you only pay for work that is retained in your model or that you intentionally abandon.

## Viewing job progress

RFT jobs have a field called `usage_metrics` which documents the total usage of the job up until the current step. This includes the time spent training, and all tokens used across all model graders on the job. This field can be inspected via the API (`GET /v1/fine_tuning/jobs/{job_id}`) or via the [fine-tuning dashboard](https://platform.openai.com/finetune).

## Factors that influence training time

Because billing is time‑based, your configuration choices directly affect cost. Key factors include:

* **Problem difficulty:** if your dataset consists of difficult problems, the model will likely spend more time reasoning over each problem which increases the amount of time it takes to produce each sample.
* **Compute intensity**: The `compute_multiplier` hyperparameter controls how much computation you do per training step. Higher values encourage the model to reason more verbosely over each datapoint, which causes each step to run more slowly.
* **Validation settings**:

  + A larger validation set increases the time spent evaluating.
  + Increasing `eval_samples` (the number of model outputs graded per validation example) increases validation time.
  + Running validation more frequently (lower `eval_interval`) increases the proportion of time spent on validation.
* **Grader performance**:

  + Larger or more capable model graders take longer to return a grade than smaller ones. For example, grading with a reasoning model may take 10x longer than grading with a non-reasoning model.
  + Complex Python grading functions take longer to run than simple ones.

These settings let you trade off cost, speed, and model quality. For example, frequent validation can catch issues earlier but increases cost. Grading with a more advanced model can drastically improve grading accuracy, but will slow down each grading step and make jobs more expensive.

## Managing cost

To control your spend:

* Start with shorter runs to understand how your configuration affects time.
* Use a reasonable number of validation examples and `eval_samples`. Avoid validating more often than you need.
* Choose the smallest grader model that meets your quality requirements.
* Keep custom Python graders efficient.
* Adjust `compute_multiplier` to balance convergence speed and cost.
* Monitor your run in the dashboard or via the API. You can pause or cancel at any time.

## Examples

## Successful training run

| Training Time | Billed Time | Status | Description |
| --- | --- | --- | --- |
| 00:00 | 00:00 | – | User creates RFT job via API |
| 00:10 | 00:00 | VALIDATING\_FILES | 10 minutes spent validating dataset |
| 00:30 | 00:00 | VALIDATING\_FILES | 20 minutes running dataset safety checks |
| 01:00 | 00:00 | QUEUED | 30 minutes waiting for an available worker |
| 01:30 | 00:00 | RUNNING | 30 minutes setting up training (downloading weights, preprocessing, etc.) |
| 05:30 | 04:00 | RUNNING | 4 hours spent training |
| 06:00 | 04:00 | RUNNING | 30 minutes running safety evaluations of resulting model |
| 06:00 | 04:00 | SUCCEEDED | Training finishes |

In this case, the total wall‑clock time is 6 hours, but only 4 hours are billable. The cost would be 4 hours × $100/hour = **$400**.

## Failed job example

In this example, the run trains for 2 hours, writes a checkpoint, trains for 1 more hour, but then fails. Only the 2 hours of training up to the checkpoint are billable.

| Training Time | Billed Time | Status | Description |
| --- | --- | --- | --- |
| 00:00 | 00:00 | – | User creates RFT job via API |
| 00:10 | 00:00 | VALIDATING\_FILES | 10 minutes spent validating dataset |
| 00:30 | 00:00 | VALIDATING\_FILES | 20 minutes running dataset safety checks |
| 01:00 | 00:00 | QUEUED | 30 minutes waiting for an available worker |
| 01:30 | 00:00 | RUNNING | 30 minutes setting up training (downloading weights, preprocessing, etc.) |
| 03:30 | 02:00 | RUNNING | 2 hours spent training |
| 03:30 | 02:00 | RUNNING | Checkpoint created at step 5 |
| 04:30 | 02:00 | RUNNING | Training fails due to internal error at step 8 (after 1 more hour) |
| 04:30 | 02:00 | RUNNING | 30 minutes evaluating and validating the checkpoint |
| 04:30 | 02:00 | SUCCEEDED | Job finishes (with latest checkpoint) |

Even though 3 hours were spent training in total, only 2 hours are "captured" in a usable checkpoint and are billed. The hour of training work lost due to the failure is not your responsibility. The cost would be 2 hours × $100/hour = **$200**.

# Frequently asked questions

## When am I charged?

We bill when your run completes, is paused, is cancelled, or fails. Each bill covers work done since the previous bill.

## Do I pay if a run fails?

If a run fails due to our error and any recent training work is lost, you are not charged for the lost portion. If you cancel a run, you are charged for work up to the cancellation.

## How are grader model tokens billed?

We count the tokens used by any model graders you configure. After training finishes, we bill those tokens at our standard per‑token rates.

## Can I pause and resume a run?

Yes. When you pause, we save a checkpoint and charge for work done so far. When you resume, you will only be charged for additional work done after resuming.  
  
If you have other questions about Reinforcement Fine‑Tuning billing, [contact our support team](https://help.openai.com/).
