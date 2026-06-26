<!-- source: https://developers.openai.com/api/reference/go/resources/moderations/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Moderations](/api/reference/go/resources/moderations)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create moderation

client.Moderations.New(ctx, body) (\*[ModerationNewResponse](/api/reference/go/resources/moderations#(resource)%20moderations%20%3E%20(model)%20ModerationNewResponse%20%3E%20(schema)), error)

POST/moderations

Classifies if text and/or image inputs are potentially harmful. Learn
more in the [moderation guide](https://platform.openai.com/docs/guides/moderation).

##### ParametersExpand Collapse

body ModerationNewParams

Input param.Field[[ModerationNewParamsInputUnion](/api/reference/go/resources/moderations/methods/create#(resource)%20moderations%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20input%20%3E%20(schema))]

Input (or inputs) to classify. Can be a single string, an array of strings, or
an array of multi-modal input objects similar to other models.

string

type ModerationNewParamsInputArray []string

An array of strings to classify for moderation.

type ModerationNewParamsInputModerationMultiModalArray [][ModerationMultiModalInputUnion](/api/reference/go/resources/moderations#(resource)%20moderations%20%3E%20(model)%20moderation_multi_modal_input%20%3E%20(schema))

An array of multi-modal inputs to the moderation model.

One of the following:

type ModerationImageURLInput struct{…}

An object describing an image to classify.

ImageURL ModerationImageURLInputImageURL

Contains either an image URL or a data URL for a base64 encoded image.

URL string

Either a URL of the image or the base64 encoded image data.

formaturi

Type ImageURL

Always `image_url`.

type ModerationTextInput struct{…}

An object describing text to classify.

Text string

A string of text to classify.

Type Text

Always `text`.

Model param.Field[[ModerationModel](/api/reference/go/resources/moderations#(resource)%20moderations%20%3E%20(model)%20moderation_model%20%3E%20(schema))]Optional

The content moderation model you would like to use. Learn more in
[the moderation guide](https://platform.openai.com/docs/guides/moderation), and learn about
available models [here](https://platform.openai.com/docs/models#moderation).

string

type ModerationModel string

One of the following:

const ModerationModelOmniModerationLatest [ModerationModel](/api/reference/go/resources/moderations#(resource)%20moderations%20%3E%20(model)%20moderation_model%20%3E%20(schema)) = "omni-moderation-latest"

const ModerationModelOmniModeration2024\_09\_26 [ModerationModel](/api/reference/go/resources/moderations#(resource)%20moderations%20%3E%20(model)%20moderation_model%20%3E%20(schema)) = "omni-moderation-2024-09-26"

const ModerationModelTextModerationLatest [ModerationModel](/api/reference/go/resources/moderations#(resource)%20moderations%20%3E%20(model)%20moderation_model%20%3E%20(schema)) = "text-moderation-latest"

const ModerationModelTextModerationStable [ModerationModel](/api/reference/go/resources/moderations#(resource)%20moderations%20%3E%20(model)%20moderation_model%20%3E%20(schema)) = "text-moderation-stable"

##### ReturnsExpand Collapse

type ModerationNewResponse struct{…}

Represents if a given text input is potentially harmful.

ID string

The unique identifier for the moderation request.

Model string

The model used to generate the moderation results.

Results [][Moderation](/api/reference/go/resources/moderations#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema))

A list of moderation objects.

Categories ModerationCategories

A list of the categories, and whether they are flagged or not.

Harassment bool

Content that expresses, incites, or promotes harassing language towards any target.

HarassmentThreatening bool

Harassment content that also includes violence or serious harm towards any target.

Hate bool

Content that expresses, incites, or promotes hate based on race, gender, ethnicity, religion, nationality, sexual orientation, disability status, or caste. Hateful content aimed at non-protected groups (e.g., chess players) is harassment.

HateThreatening bool

Hateful content that also includes violence or serious harm towards the targeted group based on race, gender, ethnicity, religion, nationality, sexual orientation, disability status, or caste.

Illicit bool

Content that includes instructions or advice that facilitate the planning or execution of wrongdoing, or that gives advice or instruction on how to commit illicit acts. For example, “how to shoplift” would fit this category.

IllicitViolent bool

Content that includes instructions or advice that facilitate the planning or execution of wrongdoing that also includes violence, or that gives advice or instruction on the procurement of any weapon.

SelfHarm bool

Content that promotes, encourages, or depicts acts of self-harm, such as suicide, cutting, and eating disorders.

SelfHarmInstructions bool

Content that encourages performing acts of self-harm, such as suicide, cutting, and eating disorders, or that gives instructions or advice on how to commit such acts.

SelfHarmIntent bool

Content where the speaker expresses that they are engaging or intend to engage in acts of self-harm, such as suicide, cutting, and eating disorders.

Sexual bool

Content meant to arouse sexual excitement, such as the description of sexual activity, or that promotes sexual services (excluding sex education and wellness).

SexualMinors bool

Sexual content that includes an individual who is under 18 years old.

Violence bool

Content that depicts death, violence, or physical injury.

ViolenceGraphic bool

Content that depicts death, violence, or physical injury in graphic detail.

CategoryAppliedInputTypes ModerationCategoryAppliedInputTypes

A list of the categories along with the input type(s) that the score applies to.

Harassment []string

The applied input type(s) for the category ‘harassment’.

HarassmentThreatening []string

The applied input type(s) for the category ‘harassment/threatening’.

Hate []string

The applied input type(s) for the category ‘hate’.

HateThreatening []string

The applied input type(s) for the category ‘hate/threatening’.

Illicit []string

The applied input type(s) for the category ‘illicit’.

IllicitViolent []string

The applied input type(s) for the category ‘illicit/violent’.

SelfHarm []string

The applied input type(s) for the category ‘self-harm’.

One of the following:

const ModerationCategoryAppliedInputTypesSelfHarmText ModerationCategoryAppliedInputTypesSelfHarm = "text"

const ModerationCategoryAppliedInputTypesSelfHarmImage ModerationCategoryAppliedInputTypesSelfHarm = "image"

SelfHarmInstructions []string

The applied input type(s) for the category ‘self-harm/instructions’.

One of the following:

const ModerationCategoryAppliedInputTypesSelfHarmInstructionText ModerationCategoryAppliedInputTypesSelfHarmInstruction = "text"

const ModerationCategoryAppliedInputTypesSelfHarmInstructionImage ModerationCategoryAppliedInputTypesSelfHarmInstruction = "image"

SelfHarmIntent []string

The applied input type(s) for the category ‘self-harm/intent’.

One of the following:

const ModerationCategoryAppliedInputTypesSelfHarmIntentText ModerationCategoryAppliedInputTypesSelfHarmIntent = "text"

const ModerationCategoryAppliedInputTypesSelfHarmIntentImage ModerationCategoryAppliedInputTypesSelfHarmIntent = "image"

Sexual []string

The applied input type(s) for the category ‘sexual’.

One of the following:

const ModerationCategoryAppliedInputTypesSexualText ModerationCategoryAppliedInputTypesSexual = "text"

const ModerationCategoryAppliedInputTypesSexualImage ModerationCategoryAppliedInputTypesSexual = "image"

SexualMinors []string

The applied input type(s) for the category ‘sexual/minors’.

Violence []string

The applied input type(s) for the category ‘violence’.

One of the following:

const ModerationCategoryAppliedInputTypesViolenceText ModerationCategoryAppliedInputTypesViolence = "text"

const ModerationCategoryAppliedInputTypesViolenceImage ModerationCategoryAppliedInputTypesViolence = "image"

ViolenceGraphic []string

The applied input type(s) for the category ‘violence/graphic’.

One of the following:

const ModerationCategoryAppliedInputTypesViolenceGraphicText ModerationCategoryAppliedInputTypesViolenceGraphic = "text"

const ModerationCategoryAppliedInputTypesViolenceGraphicImage ModerationCategoryAppliedInputTypesViolenceGraphic = "image"

CategoryScores ModerationCategoryScores

A list of the categories along with their scores as predicted by model.

Harassment float64

The score for the category ‘harassment’.

HarassmentThreatening float64

The score for the category ‘harassment/threatening’.

Hate float64

The score for the category ‘hate’.

HateThreatening float64

The score for the category ‘hate/threatening’.

Illicit float64

The score for the category ‘illicit’.

IllicitViolent float64

The score for the category ‘illicit/violent’.

SelfHarm float64

The score for the category ‘self-harm’.

SelfHarmInstructions float64

The score for the category ‘self-harm/instructions’.

SelfHarmIntent float64

The score for the category ‘self-harm/intent’.

Sexual float64

The score for the category ‘sexual’.

SexualMinors float64

The score for the category ‘sexual/minors’.

Violence float64

The score for the category ‘violence’.

ViolenceGraphic float64

The score for the category ‘violence/graphic’.

Flagged bool

Whether any of the below categories are flagged.

### Create moderation

Go

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  moderation, err := client.Moderations.New(context.TODO(), openai.ModerationNewParams{
    Input: openai.ModerationNewParamsInputUnion{
      OfString: openai.String("I want to kill them."),
  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", moderation.ID)

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
