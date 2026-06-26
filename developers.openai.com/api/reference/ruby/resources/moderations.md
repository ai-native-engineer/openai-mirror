<!-- source: https://developers.openai.com/api/reference/ruby/resources/moderations/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Moderations

Given text and/or image inputs, classifies if those inputs are potentially harmful.

##### [Create moderation](/api/reference/ruby/resources/moderations/methods/create)

moderations.create(\*\*kwargs) -> [ModerationCreateResponse](/api/reference/ruby/resources/moderations#(resource)%20moderations%20%3E%20(model)%20moderation_create_response%20%3E%20(schema)) { id, model, results }

POST/moderations

##### ModelsExpand Collapse

class Moderation { categories, category\_applied\_input\_types, category\_scores, flagged }

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

class ModerationImageURLInput { image\_url, type }

An object describing an image to classify.

image\_url: ImageURL{ url}

Contains either an image URL or a data URL for a base64 encoded image.

url: String

Either a URL of the image or the base64 encoded image data.

formaturi

type: :image\_url

Always `image_url`.

ModerationModel = :"omni-moderation-latest" | :"omni-moderation-2024-09-26" | :"text-moderation-latest" | :"text-moderation-stable"

One of the following:

:"omni-moderation-latest"

:"omni-moderation-2024-09-26"

:"text-moderation-latest"

:"text-moderation-stable"

ModerationMultiModalInput = [ModerationImageURLInput](/api/reference/ruby/resources/moderations#(resource)%20moderations%20%3E%20(model)%20moderation_image_url_input%20%3E%20(schema)) { image\_url, type }  | [ModerationTextInput](/api/reference/ruby/resources/moderations#(resource)%20moderations%20%3E%20(model)%20moderation_text_input%20%3E%20(schema)) { text, type }

An object describing an image to classify.

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

class ModerationTextInput { text, type }

An object describing text to classify.

text: String

A string of text to classify.

type: :text

Always `text`.

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
