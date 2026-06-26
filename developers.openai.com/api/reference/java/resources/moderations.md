<!-- source: https://developers.openai.com/api/reference/java/resources/moderations/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Moderations

Given text and/or image inputs, classifies if those inputs are potentially harmful.

##### [Create moderation](/api/reference/java/resources/moderations/methods/create)

[ModerationCreateResponse](/api/reference/java/resources/moderations#(resource)%20moderations%20%3E%20(model)%20ModerationCreateResponse%20%3E%20(schema)) moderations().create(ModerationCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/moderations

##### ModelsExpand Collapse

class Moderation:

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

class ModerationImageUrlInput:

An object describing an image to classify.

ImageUrl imageUrl

Contains either an image URL or a data URL for a base64 encoded image.

String url

Either a URL of the image or the base64 encoded image data.

formaturi

JsonValue; type "image\_url"constant"image\_url"constant

Always `image_url`.

enum ModerationModel:

OMNI\_MODERATION\_LATEST("omni-moderation-latest")

OMNI\_MODERATION\_2024\_09\_26("omni-moderation-2024-09-26")

TEXT\_MODERATION\_LATEST("text-moderation-latest")

TEXT\_MODERATION\_STABLE("text-moderation-stable")

class ModerationMultiModalInput: A class that can be one of several variants.union

An object describing an image to classify.

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

class ModerationTextInput:

An object describing text to classify.

String text

A string of text to classify.

JsonValue; type "text"constant"text"constant

Always `text`.
