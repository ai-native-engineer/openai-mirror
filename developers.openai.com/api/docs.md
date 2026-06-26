<!-- source: https://developers.openai.com/api/docs/ -->

# API Platform

## Developer quickstart

Make your first API request in minutes. Learn the basics of the OpenAI platform.

[Get started](/api/docs/quickstart)[Create API key](https://platform.openai.com/api-keys)

javascript

curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-5.5",
    "input": "Write a short bedtime story about a unicorn."
  }'

import OpenAI from "openai";
const client = new OpenAI();

const response = await client.responses.create({
  model: "gpt-5.5",
  input: "Write a short bedtime story about a unicorn.",

console.log(response.output_text);

from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-5.5",
    input="Write a short bedtime story about a unicorn."

print(response.output_text)

using OpenAI.Responses;

string apiKey = Environment.GetEnvironmentVariable("OPENAI_API_KEY")!;
var client = new OpenAIResponseClient(model: "gpt-5.5", apiKey: apiKey);

OpenAIResponse response = client.CreateResponse(
    "Write a short bedtime story about a unicorn."
);

Console.WriteLine(response.GetOutputText());

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.responses.Response;
import com.openai.models.responses.ResponseCreateParams;

public class Main {
    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ResponseCreateParams params = ResponseCreateParams.builder()
                .model("gpt-5.5")
                .input("Write a short bedtime story about a unicorn.")
                .build();

        Response response = client.responses().create(params);
        System.out.println(response.outputText());

package main

import (
	"context"
	"fmt"

	"github.com/openai/openai-go/v3"
	"github.com/openai/openai-go/v3/responses"

func main() {
	client := openai.NewClient()

	response, err := client.Responses.New(context.Background(), openai.ResponseNewParams{
		Model: "gpt-5.5",
		Input: responses.ResponseNewParamsInputUnion{
			OfString: openai.String("Write a short bedtime story about a unicorn."),
	})
	if err != nil {
		panic(err)

	fmt.Println(response.OutputText())

require "openai"

openai = OpenAI::Client.new

response = openai.responses.create(
  model: "gpt-5.5",
  input: "Write a short bedtime story about a unicorn."

puts(response.output_text)

openai responses create \
  --model gpt-5.5 \
  --input "Write a short bedtime story about a unicorn." \
  --raw-output \
  --transform 'output.#(type=="message").content.0.text'

Build with the OpenAI API in Codex

The OpenAI Developers plugin enables Codex to connect to the OpenAI Platform, follow OpenAI API setup guidance, and create project API keys when your app needs one.

[Install the plugin](/learn/developers-codex-plugin)

## Build paths

[### Responses API

Make direct model requests for text, structured output, tools, and multimodal workflows.

Start with Responses](/api/docs/guides/text)[### Agents SDK

Build code-first agents that orchestrate tools, handoffs, approvals, tracing, and container-based execution.

Start with the Agents SDK](/api/docs/guides/agents/quickstart)

## Models

Start with GPT-5.5 for complex reasoning and coding, or choose GPT-5.4 mini and GPT-5.4 nano for lower-latency, lower-cost workloads.

[View all](/api/docs/models)

[GPT-5.5

New

A new class of intelligence for coding and professional work.](/api/docs/models/gpt-5.5)[GPT-5.4

A more affordable model for coding and professional work.](/api/docs/models/gpt-5.4)[GPT-5.4 mini

Our strongest mini model yet for coding, computer use, and subagents](/api/docs/models/gpt-5.4-mini)

## Start building

[Read and generate text

Use the API to prompt a model and generate text](/api/docs/guides/text)[Use a model's vision capabilities

Allow models to see and analyze images in your application](/api/docs/guides/images-vision)[Generate images as output

Create images with GPT Image 2](/api/docs/guides/image-generation)[Build apps with audio

Analyze, transcribe, and generate audio with API endpoints](/api/docs/guides/audio)[Build agentic applications

Use the API to build agents that use tools and computers](/api/docs/guides/agents)[Achieve complex tasks with reasoning

Use reasoning models to carry out complex tasks](/api/docs/guides/reasoning)[Get structured data from models

Use Structured Outputs to get model responses that adhere to a JSON schema](/api/docs/guides/structured-outputs)[Tailor to your use case

Adjust our models to perform specifically for your use case with fine-tuning, evals, and distillation](/api/docs/guides/model-optimization)

[Help center

Frequently asked account and billing questions](https://help.openai.com)[Developer forum

Discuss topics with other developers](https://community.openai.com/)[Cookbook

Open-source collection of examples and guides](/cookbook)[Status

Check the status of OpenAI services](https://status.openai.com)
