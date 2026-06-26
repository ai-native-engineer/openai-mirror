<!-- source: https://developers.openai.com/api/reference/java/resources/moderations/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Moderations](/api/reference/java/resources/moderations)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create moderation

[ModerationCreateResponse](/api/reference/java/resources/moderations#(resource)%20moderations%20%3E%20(model)%20ModerationCreateResponse%20%3E%20(schema)) moderations().create(ModerationCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/moderations

Classifies if text and/or image inputs are potentially harmful. Learn
more in the [moderation guide](https://platform.openai.com/docs/guides/moderation).

##### ParametersExpand Collapse

ModerationCreateParams params

Input input

Input (or inputs) to classify. Can be a single string, an array of strings, or
an array of multi-modal input objects similar to other models.

String

List<String>

List<[ModerationMultiModalInput](/api/reference/java/resources/moderations#(resource)%20moderations%20%3E%20(model)%20moderation_multi_modal_input%20%3E%20(schema))>

One of the following:

class ModerationImageUrlInput:

An object describing an image to classify.

ImageUrl imageUrl

Contains either an image URL or a data URL for a base64 encoded image.

String url

Either a URL of the image or the base64 encoded image data.

formaturi

JsonValue; type "image\_url"constant"image\_url"constant

Always `image_url`.

class ModerationTextInput:

An object describing text to classify.

String text

A string of text to classify.

JsonValue; type "text"constant"text"constant

Always `text`.

Optional<[ModerationModel](/api/reference/java/resources/moderations#(resource)%20moderations%20%3E%20(model)%20moderation_model%20%3E%20(schema))> model

The content moderation model you would like to use. Learn more in
[the moderation guide](https://platform.openai.com/docs/guides/moderation), and learn about
available models [here](https://platform.openai.com/docs/models#moderation).

##### ReturnsExpand Collapse

class ModerationCreateResponse:

Represents if a given text input is potentially harmful.

String id

The unique identifier for the moderation request.

String model

The model used to generate the moderation results.

List<[Moderation](/api/reference/java/resources/moderations#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema))> results

A list of moderation objects.

Categories categories

A list of the categories, and whether they are flagged or not.

boolean harassment

Content that expresses, incites, or promotes harassing language towards any target.

boolean harassmentThreatening

Harassment content that also includes violence or serious harm towards any target.

boolean hate

Content that expresses, incites, or promotes hate based on race, gender, ethnicity, religion, nationality, sexual orientation, disability status, or caste. Hateful content aimed at non-protected groups (e.g., chess players) is harassment.

boolean hateThreatening

Hateful content that also includes violence or serious harm towards the targeted group based on race, gender, ethnicity, religion, nationality, sexual orientation, disability status, or caste.

Optional<Boolean> illicit

Content that includes instructions or advice that facilitate the planning or execution of wrongdoing, or that gives advice or instruction on how to commit illicit acts. For example, “how to shoplift” would fit this category.

Optional<Boolean> illicitViolent

Content that includes instructions or advice that facilitate the planning or execution of wrongdoing that also includes violence, or that gives advice or instruction on the procurement of any weapon.

boolean selfHarm

Content that promotes, encourages, or depicts acts of self-harm, such as suicide, cutting, and eating disorders.

boolean selfHarmInstructions

Content that encourages performing acts of self-harm, such as suicide, cutting, and eating disorders, or that gives instructions or advice on how to commit such acts.

boolean selfHarmIntent

Content where the speaker expresses that they are engaging or intend to engage in acts of self-harm, such as suicide, cutting, and eating disorders.

boolean sexual

Content meant to arouse sexual excitement, such as the description of sexual activity, or that promotes sexual services (excluding sex education and wellness).

boolean sexualMinors

Sexual content that includes an individual who is under 18 years old.

boolean violence

Content that depicts death, violence, or physical injury.

boolean violenceGraphic

Content that depicts death, violence, or physical injury in graphic detail.

CategoryAppliedInputTypes categoryAppliedInputTypes

A list of the categories along with the input type(s) that the score applies to.

List<Harassment> harassment

The applied input type(s) for the category ‘harassment’.

List<HarassmentThreatening> harassmentThreatening

The applied input type(s) for the category ‘harassment/threatening’.

List<Hate> hate

The applied input type(s) for the category ‘hate’.

List<HateThreatening> hateThreatening

The applied input type(s) for the category ‘hate/threatening’.

List<Illicit> illicit

The applied input type(s) for the category ‘illicit’.

List<IllicitViolent> illicitViolent

The applied input type(s) for the category ‘illicit/violent’.

List<SelfHarm> selfHarm

The applied input type(s) for the category ‘self-harm’.

One of the following:

TEXT("text")

IMAGE("image")

List<SelfHarmInstruction> selfHarmInstructions

The applied input type(s) for the category ‘self-harm/instructions’.

One of the following:

TEXT("text")

IMAGE("image")

List<SelfHarmIntent> selfHarmIntent

The applied input type(s) for the category ‘self-harm/intent’.

One of the following:

TEXT("text")

IMAGE("image")

List<Sexual> sexual

The applied input type(s) for the category ‘sexual’.

One of the following:

TEXT("text")

IMAGE("image")

List<SexualMinor> sexualMinors

The applied input type(s) for the category ‘sexual/minors’.

List<Violence> violence

The applied input type(s) for the category ‘violence’.

One of the following:

TEXT("text")

IMAGE("image")

List<ViolenceGraphic> violenceGraphic

The applied input type(s) for the category ‘violence/graphic’.

One of the following:

TEXT("text")

IMAGE("image")

CategoryScores categoryScores

A list of the categories along with their scores as predicted by model.

double harassment

The score for the category ‘harassment’.

double harassmentThreatening

The score for the category ‘harassment/threatening’.

double hate

The score for the category ‘hate’.

double hateThreatening

The score for the category ‘hate/threatening’.

double illicit

The score for the category ‘illicit’.

double illicitViolent

The score for the category ‘illicit/violent’.

double selfHarm

The score for the category ‘self-harm’.

double selfHarmInstructions

The score for the category ‘self-harm/instructions’.

double selfHarmIntent

The score for the category ‘self-harm/intent’.

double sexual

The score for the category ‘sexual’.

double sexualMinors

The score for the category ‘sexual/minors’.

double violence

The score for the category ‘violence’.

double violenceGraphic

The score for the category ‘violence/graphic’.

boolean flagged

Whether any of the below categories are flagged.

### Create moderation

Java

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.moderations.ModerationCreateParams;
import com.openai.models.moderations.ModerationCreateResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ModerationCreateParams params = ModerationCreateParams.builder()
            .input("I want to kill them.")
            .build();
        ModerationCreateResponse moderation = client.moderations().create(params);

200 example

  "id": "id",
  "model": "model",
  "results": [
      "categories": {
        "harassment": true,
        "harassment/threatening": true,
        "hate": true,
        "hate/threatening": true,
        "illicit": true,
        "illicit/violent": true,
        "self-harm": true,
        "self-harm/instructions": true,
        "self-harm/intent": true,
        "sexual": true,
        "sexual/minors": true,
        "violence": true,
        "violence/graphic": true
      "category_applied_input_types": {
        "harassment": [
          "text"
        ],
        "harassment/threatening": [
          "text"
        ],
        "hate": [
          "text"
        ],
        "hate/threatening": [
          "text"
        ],
        "illicit": [
          "text"
        ],
        "illicit/violent": [
          "text"
        ],
        "self-harm": [
          "text"
        ],
        "self-harm/instructions": [
          "text"
        ],
        "self-harm/intent": [
          "text"
        ],
        "sexual": [
          "text"
        ],
        "sexual/minors": [
          "text"
        ],
        "violence": [
          "text"
        ],
        "violence/graphic": [
          "text"
        ]
      "category_scores": {
        "harassment": 0,
        "harassment/threatening": 0,
        "hate": 0,
        "hate/threatening": 0,
        "illicit": 0,
        "illicit/violent": 0,
        "self-harm": 0,
        "self-harm/instructions": 0,
        "self-harm/intent": 0,
        "sexual": 0,
        "sexual/minors": 0,
        "violence": 0,
        "violence/graphic": 0
      "flagged": true
  ]

##### Returns Examples

200 example

  "id": "id",
  "model": "model",
  "results": [
      "categories": {
        "harassment": true,
        "harassment/threatening": true,
        "hate": true,
        "hate/threatening": true,
        "illicit": true,
        "illicit/violent": true,
        "self-harm": true,
        "self-harm/instructions": true,
        "self-harm/intent": true,
        "sexual": true,
        "sexual/minors": true,
        "violence": true,
        "violence/graphic": true
      "category_applied_input_types": {
        "harassment": [
          "text"
        ],
        "harassment/threatening": [
          "text"
        ],
        "hate": [
          "text"
        ],
        "hate/threatening": [
          "text"
        ],
        "illicit": [
          "text"
        ],
        "illicit/violent": [
          "text"
        ],
        "self-harm": [
          "text"
        ],
        "self-harm/instructions": [
          "text"
        ],
        "self-harm/intent": [
          "text"
        ],
        "sexual": [
          "text"
        ],
        "sexual/minors": [
          "text"
        ],
        "violence": [
          "text"
        ],
        "violence/graphic": [
          "text"
        ]
      "category_scores": {
        "harassment": 0,
        "harassment/threatening": 0,
        "hate": 0,
        "hate/threatening": 0,
        "illicit": 0,
        "illicit/violent": 0,
        "self-harm": 0,
        "self-harm/instructions": 0,
        "self-harm/intent": 0,
        "sexual": 0,
        "sexual/minors": 0,
        "violence": 0,
        "violence/graphic": 0
      "flagged": true
  ]
