<!-- source: https://developers.openai.com/api/reference/cli/resources/moderations/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Moderations](/api/reference/cli/resources/moderations)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create moderation

$ openai moderations create

POST/moderations

Classifies if text and/or image inputs are potentially harmful. Learn
more in the [moderation guide](https://platform.openai.com/docs/guides/moderation).

##### ParametersExpand Collapse

--input: string or array of string or array of [ModerationMultiModalInput](/api/reference/cli/resources/moderations#(resource)%20moderations%20%3E%20(model)%20moderation_multi_modal_input%20%3E%20(schema))

Input (or inputs) to classify. Can be a single string, an array of strings, or
an array of multi-modal input objects similar to other models.

--model: optional string or [ModerationModel](/api/reference/cli/resources/moderations#(resource)%20moderations%20%3E%20(model)%20moderation_model%20%3E%20(schema))

The content moderation model you would like to use. Learn more in
[the moderation guide](https://platform.openai.com/docs/guides/moderation), and learn about
available models [here](https://platform.openai.com/docs/models#moderation).

##### ReturnsExpand Collapse

ModerationNewResponse: object { id, model, results }

Represents if a given text input is potentially harmful.

id: string

The unique identifier for the moderation request.

model: string

The model used to generate the moderation results.

results: array of [Moderation](/api/reference/cli/resources/moderations#(resource)%20moderations%20%3E%20(model)%20moderation%20%3E%20(schema)) { categories, category\_applied\_input\_types, category\_scores, flagged }

A list of moderation objects.

categories: object { harassment, "harassment/threatening", hate, 10 more }

A list of the categories, and whether they are flagged or not.

harassment: boolean

Content that expresses, incites, or promotes harassing language towards any target.

harassment/threatening: boolean

Harassment content that also includes violence or serious harm towards any target.

hate: boolean

Content that expresses, incites, or promotes hate based on race, gender, ethnicity, religion, nationality, sexual orientation, disability status, or caste. Hateful content aimed at non-protected groups (e.g., chess players) is harassment.

hate/threatening: boolean

Hateful content that also includes violence or serious harm towards the targeted group based on race, gender, ethnicity, religion, nationality, sexual orientation, disability status, or caste.

illicit: boolean

Content that includes instructions or advice that facilitate the planning or execution of wrongdoing, or that gives advice or instruction on how to commit illicit acts. For example, “how to shoplift” would fit this category.

illicit/violent: boolean

Content that includes instructions or advice that facilitate the planning or execution of wrongdoing that also includes violence, or that gives advice or instruction on the procurement of any weapon.

self-harm: boolean

Content that promotes, encourages, or depicts acts of self-harm, such as suicide, cutting, and eating disorders.

self-harm/instructions: boolean

Content that encourages performing acts of self-harm, such as suicide, cutting, and eating disorders, or that gives instructions or advice on how to commit such acts.

self-harm/intent: boolean

Content where the speaker expresses that they are engaging or intend to engage in acts of self-harm, such as suicide, cutting, and eating disorders.

sexual: boolean

Content meant to arouse sexual excitement, such as the description of sexual activity, or that promotes sexual services (excluding sex education and wellness).

sexual/minors: boolean

Sexual content that includes an individual who is under 18 years old.

violence: boolean

Content that depicts death, violence, or physical injury.

violence/graphic: boolean

Content that depicts death, violence, or physical injury in graphic detail.

category\_applied\_input\_types: object { harassment, "harassment/threatening", hate, 10 more }

A list of the categories along with the input type(s) that the score applies to.

harassment: array of "text"

The applied input type(s) for the category ‘harassment’.

"text"

harassment/threatening: array of "text"

The applied input type(s) for the category ‘harassment/threatening’.

"text"

hate: array of "text"

The applied input type(s) for the category ‘hate’.

"text"

hate/threatening: array of "text"

The applied input type(s) for the category ‘hate/threatening’.

"text"

illicit: array of "text"

The applied input type(s) for the category ‘illicit’.

"text"

illicit/violent: array of "text"

The applied input type(s) for the category ‘illicit/violent’.

"text"

self-harm: array of "text" or "image"

The applied input type(s) for the category ‘self-harm’.

"text"

"image"

self-harm/instructions: array of "text" or "image"

The applied input type(s) for the category ‘self-harm/instructions’.

"text"

"image"

self-harm/intent: array of "text" or "image"

The applied input type(s) for the category ‘self-harm/intent’.

"text"

"image"

sexual: array of "text" or "image"

The applied input type(s) for the category ‘sexual’.

"text"

"image"

sexual/minors: array of "text"

The applied input type(s) for the category ‘sexual/minors’.

"text"

violence: array of "text" or "image"

The applied input type(s) for the category ‘violence’.

"text"

"image"

violence/graphic: array of "text" or "image"

The applied input type(s) for the category ‘violence/graphic’.

"text"

"image"

category\_scores: object { harassment, "harassment/threatening", hate, 10 more }

A list of the categories along with their scores as predicted by model.

harassment: number

The score for the category ‘harassment’.

harassment/threatening: number

The score for the category ‘harassment/threatening’.

hate: number

The score for the category ‘hate’.

hate/threatening: number

The score for the category ‘hate/threatening’.

illicit: number

The score for the category ‘illicit’.

illicit/violent: number

The score for the category ‘illicit/violent’.

self-harm: number

The score for the category ‘self-harm’.

self-harm/instructions: number

The score for the category ‘self-harm/instructions’.

self-harm/intent: number

The score for the category ‘self-harm/intent’.

sexual: number

The score for the category ‘sexual’.

sexual/minors: number

The score for the category ‘sexual/minors’.

violence: number

The score for the category ‘violence’.

violence/graphic: number

The score for the category ‘violence/graphic’.

flagged: boolean

Whether any of the below categories are flagged.

### Create moderation

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai moderations create \
  --api-key 'My API Key' \
  --input 'I want to kill them.'

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
