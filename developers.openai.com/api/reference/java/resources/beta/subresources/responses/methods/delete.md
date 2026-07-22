<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/responses/methods/delete/ -->

[API Reference](/api/reference/java)

[Beta](/api/reference/java/resources/beta)

[Responses](/api/reference/java/resources/beta/subresources/responses)

# Delete a model response

beta().responses().delete(ResponseDeleteParamsparams = ResponseDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/responses/{response\_id}

Deletes a model response with the given ID.

##### ParametersExpand Collapse

ResponseDeleteParams params

Optional<String> responseId

Optional<List<Beta>> betas

RESPONSES\_MULTI\_AGENT\_V1("responses\_multi\_agent=v1")

### Delete a model response

Java

package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.responses.ResponseDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        client.beta().responses().delete("resp_677efb5139a88190b512bc3fef8e535d");

  "id": "resp_6786a1bec27481909a17d673315b29f6",
  "object": "response",
  "deleted": true

  "id": "resp_6786a1bec27481909a17d673315b29f6",
  "object": "response",
  "deleted": true
