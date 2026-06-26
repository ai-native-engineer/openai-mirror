<!-- source: https://developers.openai.com/api/reference/go/resources/moderations/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Moderations

Given text and/or image inputs, classifies if those inputs are potentially harmful.

##### [Create moderation](/api/reference/go/resources/moderations/methods/create)

client.Moderations.New(ctx, body) (\*[ModerationNewResponse](/api/reference/go/resources/moderations#(resource)%20moderations%20%3E%20(model)%20ModerationNewResponse%20%3E%20(schema)), error)

POST/moderations

##### ModelsExpand Collapse

type Moderation struct{…}

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

type ModerationImageURLInput struct{…}

An object describing an image to classify.

ImageURL ModerationImageURLInputImageURL

Contains either an image URL or a data URL for a base64 encoded image.

URL string

Either a URL of the image or the base64 encoded image data.

formaturi

Type ImageURL

Always `image_url`.

type ModerationModel string

One of the following:

const ModerationModelOmniModerationLatest [ModerationModel](/api/reference/go/resources/moderations#(resource)%20moderations%20%3E%20(model)%20moderation_model%20%3E%20(schema)) = "omni-moderation-latest"

const ModerationModelOmniModeration2024\_09\_26 [ModerationModel](/api/reference/go/resources/moderations#(resource)%20moderations%20%3E%20(model)%20moderation_model%20%3E%20(schema)) = "omni-moderation-2024-09-26"

const ModerationModelTextModerationLatest [ModerationModel](/api/reference/go/resources/moderations#(resource)%20moderations%20%3E%20(model)%20moderation_model%20%3E%20(schema)) = "text-moderation-latest"

const ModerationModelTextModerationStable [ModerationModel](/api/reference/go/resources/moderations#(resource)%20moderations%20%3E%20(model)%20moderation_model%20%3E%20(schema)) = "text-moderation-stable"

type ModerationMultiModalInputUnion interface{…}

An object describing an image to classify.

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

type ModerationTextInput struct{…}

An object describing text to classify.

Text string

A string of text to classify.

Type Text

Always `text`.
