<!-- source: https://help.openai.com/en/articles/9197833-batch-api-faq -->

# Batch API FAQ

Batch API endpoint for asynchronous batch processing

Updated: 10 days ago

## How does the Batch API work?

The Batch API endpoint, as documented [here](https://platform.openai.com/docs/api-reference/batch), allows users to submit requests for asynchronous batch processing. We will process these requests within 24 hours. The details of each request will be read from a pre-uploaded file, and the responses will be written to an output file. You can query the batch object for status updates and results.

## What is the pricing for the Batch API?

Each model will be offered at **50% cost discount** vs. the synchronous APIs. Here's more [information](https://platform.openai.com/docs/pricing) regarding our API pricing.

## What models can I batch?

The Batch API is widely available across most of our models, but not all. Please refer to the [model reference docs](https://platform.openai.com/docs/models) to ensure the model you're using supports the Batch API.

## What happens if the API doesn’t complete my request within the promised time?

We aim to get all requests within 24 hours. If a batch expires (i.e. it could not be completed within the SLA time window), then remaining work is cancelled and any already completed work is returned. Developers will be charged for any completed work.

## What’s the limit of how many requests I can batch?

Embeddings APIs have a limit of 1 million enqueued requests at a time.  
  
For all other APIs, there is no limit on the number of requests you can batch; however, each usage tier has an associated batch rate limit. Your batch rate limit includes the maximum number of input tokens you have enqueued at one time. You can find your rate limits [here](https://platform.openai.com/account/rate-limits).

## Can I change the time it takes to hear back from the Batch API?

Our current specified time window is 24 hours. We currently cannot change this time period.

## Is streaming supported on the Batch API?

No, streaming is not supported on the Batch API. Batch requests return results through output files rather than streamed responses.

## Are images supported on the Batch API?

Yes, images are supported on the Batch API.

## I got an error message “The URL provided for this request does not prefix-match the batch endpoint”. What should I do?

If you get this error, this means your URL is incorrectly formatted for the Batch API endpoint. Please refer to our documentation here to make sure you’re calling the endpoint correctly.

## Does usage of the Batch API count against my other rate limits?

Batch API rate limits are completely separate from existing limits.

## What happens if a batch is cancelled?

If a batch is manually cancelled then whatever results have already been completed are returned. Developers will be charged for any completed work.

## What happens if a batch expires?

If a batch expires (i.e. it could not be completed within the SLA time window), then remaining work is cancelled and any already completed work is returned. Developers will be charged for any completed work.

## What statuses can I expect on batch jobs?

The batch job can have any of the following statuses: Validating, Failed, In Progress, Finalizing, Completed, Expired, Cancelling, and Cancelled. If you are checking API status values programmatically, use the lowercase literals: validating, failed, in\_progress, finalizing, completed, expired, cancelling, and cancelled.

* **Validating:** Validation of the uploaded file is in progress before the batch can begin.
* **Failed:** The file has failed the validation process.
* **In Progress:** The file was successfully validated and the batch process is underway.
* **Finalizing:** The batch job has completed and the results are being prepared.
* **Completed:** The batch job is complete and the results are ready.
* **Expired:** The batch could not be completed within the SLA time window.
* **Cancelling:** Cancellation of the batch job has been initiated.
* **Cancelled:** The batch job was canceled.

## How can I check which batch jobs I've already created?

You can get a list of all your batch jobs using the API call specified [here](https://platform.openai.com/docs/api-reference/batch/list).

## Is zero data retention supported on this endpoint?

If you have zero data retention enabled for your org, please note that zero data retention does not apply to the Batch API. ZDR orgs can create batch jobs, but batch input files, outputs, errors, and intermediate artifacts are retained according to the configured Batch, File Service, and Sediment retention policies.
