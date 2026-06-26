<!-- source: https://developers.openai.com/api/reference/ruby/resources/moderations/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Moderations](/api/reference/ruby/resources/moderations)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create moderation

moderations.create(\*\*kwargs) -> [ModerationCreateResponse](/api/reference/ruby/resources/moderations#(resource)%20moderations%20%3E%20(model)%20moderation_create_response%20%3E%20(schema)) { id, model, results }

POST/moderations

Classifies if text and/or image inputs are potentially harmful. Learn
more in the [moderation guide](https://platform.openai.com/docs/guides/moderation).

##### ParametersExpand Collapse

input: String | Array[String] | Array[[ModerationMultiModalInput](/api/reference/ruby/resources/moderations#(resource)%20moderations%20%3E%20(model)%20moderation_multi_modal_input%20%3E%20(schema))]

Input (or inputs) to classify. Can be a single string, an array of strings, or
an array of multi-modal input objects similar to other models.

One of the following:

String = String

A string of text to classify for moderation.

UnionMember1 = Array[String]

An array of strings to classify for moderation.

ModerationMultiModalArray = Array[[ModerationMultiModalInput](/api/reference/ruby/resources/moderations#(resource)%20moderations%20%3E%20(model)%20moderation_multi_modal_input%20%3E%20(schema))]

An array of multi-modal inputs to the moderation model.

One of the following:

class ModerationImageURLInput { image\_url, type }

An object describing an image to classify.

image\_url: ImageURL{ url}

Contains either an image URL or a data URL for a base64 encoded image.

url: String

Either a URL of the image or the base64 encoded image data.

formaturi

type: :image\_url

Always `image_url`.

class ModerationTextInput { text, type }

An object describing text to classify.

text: String

A string of text to classify.

type: :text

Always `text`.

model: String | [ModerationModel](/api/reference/ruby/resources/moderations#(resource)%20moderations%20%3E%20(model)%20moderation_model%20%3E%20(schema))

The content moderation model you would like to use. Learn more in
[the moderation guide](https://platform.openai.com/docs/guides/moderation), and learn about
available models [here](https://platform.openai.com/docs/models#moderation).

One of the following:

String = String

ModerationModel = :"omni-moderation-latest" | :"omni-moderation-2024-09-26" | :"text-moderation-latest" | :"text-moderation-stable"

One of the following:

:"omni-moderation-latest"

:"omni-moderation-2024-09-26"

:"text-moderation-latest"

:"text-moderation-stable"

##### ReturnsExpand Collapse

class ModerationCreateResponse { id, model, results }

Represents if a given text input is potentially harmful.

id: String

The unique identifier for the moderation request.

model: String

The model used to generate the moderation results.

results: Array[[Moderation](/api/reference/ruby/resources/moderations#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)) { categories, category\_applied\_input\_types, category\_scores, flagged } ]

A list of moderation objects.

categories: Categories{ harassment, harassment\_threatening, hate, 10 more}

A list of the categories, and whether they are flagged or not.

harassment: bool

Content that expresses, incites, or promotes harassing language towards any target.

harassment\_threatening: bool

Harassment content that also includes violence or serious harm towards any target.

hate: bool

Content that expresses, incites, or promotes hate based on race, gender, ethnicity, religion, nationality, sexual orientation, disability status, or caste. Hateful content aimed at non-protected groups (e.g., chess players) is harassment.

hate\_threatening: bool

Hateful content that also includes violence or serious harm towards the targeted group based on race, gender, ethnicity, religion, nationality, sexual orientation, disability status, or caste.

illicit: bool

Content that includes instructions or advice that facilitate the planning or execution of wrongdoing, or that gives advice or instruction on how to commit illicit acts. For example, “how to shoplift” would fit this category.

illicit\_violent: bool

Content that includes instructions or advice that facilitate the planning or execution of wrongdoing that also includes violence, or that gives advice or instruction on the procurement of any weapon.

self\_harm: bool

Content that promotes, encourages, or depicts acts of self-harm, such as suicide, cutting, and eating disorders.

self\_harm\_instructions: bool

Content that encourages performing acts of self-harm, such as suicide, cutting, and eating disorders, or that gives instructions or advice on how to commit such acts.

self\_harm\_intent: bool

Content where the speaker expresses that they are engaging or intend to engage in acts of self-harm, such as suicide, cutting, and eating disorders.

sexual: bool

Content meant to arouse sexual excitement, such as the description of sexual activity, or that promotes sexual services (excluding sex education and wellness).

sexual\_minors: bool

Sexual content that includes an individual who is under 18 years old.

violence: bool

Content that depicts death, violence, or physical injury.

violence\_graphic: bool

Content that depicts death, violence, or physical injury in graphic detail.

category\_applied\_input\_types: CategoryAppliedInputTypes{ harassment, harassment\_threatening, hate, 10 more}

A list of the categories along with the input type(s) that the score applies to.

harassment: Array[:text]

The applied input type(s) for the category ‘harassment’.

harassment\_threatening: Array[:text]

The applied input type(s) for the category ‘harassment/threatening’.

hate: Array[:text]

The applied input type(s) for the category ‘hate’.

hate\_threatening: Array[:text]

The applied input type(s) for the category ‘hate/threatening’.

illicit: Array[:text]

The applied input type(s) for the category ‘illicit’.

illicit\_violent: Array[:text]

The applied input type(s) for the category ‘illicit/violent’.

self\_harm: Array[:text | :image]

The applied input type(s) for the category ‘self-harm’.

One of the following:

:text

:image

self\_harm\_instructions: Array[:text | :image]

The applied input type(s) for the category ‘self-harm/instructions’.

One of the following:

:text

:image

self\_harm\_intent: Array[:text | :image]

The applied input type(s) for the category ‘self-harm/intent’.

One of the following:

:text

:image

sexual: Array[:text | :image]

The applied input type(s) for the category ‘sexual’.

One of the following:

:text

:image

sexual\_minors: Array[:text]

The applied input type(s) for the category ‘sexual/minors’.

violence: Array[:text | :image]

The applied input type(s) for the category ‘violence’.

One of the following:

:text

:image

violence\_graphic: Array[:text | :image]

The applied input type(s) for the category ‘violence/graphic’.

One of the following:

:text

:image

category\_scores: CategoryScores{ harassment, harassment\_threatening, hate, 10 more}

A list of the categories along with their scores as predicted by model.

harassment: Float

The score for the category ‘harassment’.

harassment\_threatening: Float

The score for the category ‘harassment/threatening’.

hate: Float

The score for the category ‘hate’.

hate\_threatening: Float

The score for the category ‘hate/threatening’.

illicit: Float

The score for the category ‘illicit’.

illicit\_violent: Float

The score for the category ‘illicit/violent’.

self\_harm: Float

The score for the category ‘self-harm’.

self\_harm\_instructions: Float

The score for the category ‘self-harm/instructions’.

self\_harm\_intent: Float

The score for the category ‘self-harm/intent’.

sexual: Float

The score for the category ‘sexual’.

sexual\_minors: Float

The score for the category ‘sexual/minors’.

violence: Float

The score for the category ‘violence’.

violence\_graphic: Float

The score for the category ‘violence/graphic’.

flagged: bool

Whether any of the below categories are flagged.

### Create moderation

Ruby

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

moderation = openai.moderations.create(input: "I want to kill them.")

puts(moderation)

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
