<!-- source: https://developers.openai.com/api/reference/java/resources/decisions/methods/create/ -->

[Skip to content](#_top)

For the complete documentation index, see [llms.txt](/llms.txt). Markdown versions of documentation pages are available by appending
`.md` to the page URL.

Copy Markdown

# Create a decision

[Decision](/api/reference/java/resources/decisions#(resource)%20decisions%20%3E%20(model)%20decision%20%3E%20(schema)) decisions().create(DecisionCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST

/decisions

Use this endpoint to quickly answer classification or scoring questions about some input. You can ask multiple questions in one request.

##### ParametersExpand Collapse

DecisionCreateParams params

Input input

The input to evaluate for every question. Provide a text string or an ordered array of messages, function calls and outputs, or custom tool calls and outputs. Each tool output must identify a matching call by call ID.

String model

The model to use. Only `gpt-6-luna` is supported.

minLength0

maxLength1048576

List<Question> questions

Ask 1–400 questions about the input. Each question can be a predicate, choice, or score. Answers come back in the same order.

minItems1

maxItems400

Optional<String> promptCacheKey

Partition prompt cache reuse by caller-provided key.

minLength0

maxLength64

Optional<PromptCacheOptions> promptCacheOptions

Options for prompt caching. Supported for `gpt-5.6` and later models. By default, OpenAI automatically chooses one implicit cache breakpoint. You can add explicit breakpoints to content blocks with `prompt_cache_breakpoint`. Each request can write up to four breakpoints. For cache matching, OpenAI considers up to the latest 80 breakpoints in the conversation, without a content-block lookback limit. Set `mode` to `explicit` to disable the implicit breakpoint. The `ttl` defaults to `30m`, which is currently the only supported value. See the [prompt caching guide](/api/docs/guides/prompt-caching) for current details.

Optional<String> safetyIdentifier

Opaque caller-provided end-user identifier, scoped by the verified org. Match Responses’ limit; this is never the authenticated user identity.

minLength0

maxLength128

##### ReturnsExpand Collapse

class Decision:

List<Answer> answers

Answers in question order. Any question can return a refusal instead of an answer; other questions can still receive answers. A refusal has `type: "refusal"` and the question’s `name`, or `null` if it was unnamed.

minItems0

maxItems2000

String model

The model used.

minLength0

Usage usage

Token usage for the request.

### Create a decision

SDK languageJava

package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.decisions.Decision;
import com.openai.models.decisions.DecisionCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        DecisionCreateParams params = DecisionCreateParams.builder()
            .input("string")
            .model("model")
            .addPredicateQuestion("string")
            .build();
        Decision decision = client.decisions().create(params);

Response example

  "model": "gpt-6-luna",
  "answers": [
    {"type": "predicate", "name": "damaged", "probability": 0.95}
  "usage": {
    "input_tokens": 42,
    "input_tokens_details": {"cached_tokens": 0, "cache_write_tokens": 0},
    "output_tokens": 0,
    "output_tokens_details": {"reasoning_tokens": 0},
    "total_tokens": 42

##### Returns Examples

Response example

  "model": "gpt-6-luna",
  "answers": [
    {"type": "predicate", "name": "damaged", "probability": 0.95}
  "usage": {
    "input_tokens": 42,
    "input_tokens_details": {"cached_tokens": 0, "cache_write_tokens": 0},
    "output_tokens": 0,
    "output_tokens_details": {"reasoning_tokens": 0},
    "total_tokens": 42
