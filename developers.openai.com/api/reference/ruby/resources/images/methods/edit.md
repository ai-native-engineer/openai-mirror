<!-- source: https://developers.openai.com/api/reference/ruby/resources/images/methods/edit/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Images](/api/reference/ruby/resources/images)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create image edit

images.edit(\*\*kwargs) -> [ImagesResponse](/api/reference/ruby/resources/images#(resource)%20images%20%3E%20(model)%20images_response%20%3E%20(schema)) { created, background, data, 4 more }

POST/images/edits

Creates an edited or extended image given one or more source images and a prompt. This endpoint supports GPT Image models (`gpt-image-1.5`, `gpt-image-1`, `gpt-image-1-mini`, and `chatgpt-image-latest`) and `dall-e-2`.

##### ParametersExpand Collapse

image: String | Array[String]

The image(s) to edit. Must be a supported image file or an array of images.

For the GPT image models (`gpt-image-1`, `gpt-image-1-mini`,
`gpt-image-1.5`, `gpt-image-2`, `gpt-image-2-2026-04-21`, and
`chatgpt-image-latest`), each image should be a `png`, `webp`, or
`jpg` file less than 50MB. You can provide up to 16 images.

For `dall-e-2`, you can only provide one image, and it should be a
square `png` file less than 4MB.

One of the following:

String = String

UnionMember1 = Array[String]

prompt: String

A text description of the desired image(s). The maximum length is 1000 characters for `dall-e-2`, and 32000 characters for the GPT image models.

background: :transparent | :opaque | :auto

Allows to set transparency for the background of the generated image(s).
This parameter is only supported for GPT image models that support
transparent backgrounds. Must be one of `transparent`, `opaque`, or
`auto` (default value). When `auto` is used, the model will
automatically determine the best background for the image.

`gpt-image-2` and `gpt-image-2-2026-04-21` do not support
transparent backgrounds. Requests with `background` set to
`transparent` will return an error for these models; use `opaque` or
`auto` instead.

If `transparent`, the output format needs to support transparency,
so it should be set to either `png` (default value) or `webp`.

One of the following:

:transparent

:opaque

:auto

input\_fidelity: :high | :low

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

One of the following:

:high

:low

mask: FileInput

An additional image whose fully transparent areas (e.g. where alpha is zero) indicate where `image` should be edited. If there are multiple images provided, the mask will be applied on the first image. Must be a valid PNG file, less than 4MB, and have the same dimensions as `image`.

model: String | [ImageModel](/api/reference/ruby/resources/images#(resource)%20images%20%3E%20(model)%20image_model%20%3E%20(schema))

The model to use for image generation. One of `dall-e-2` or a GPT image model (`gpt-image-1`, `gpt-image-1-mini`, `gpt-image-1.5`, `gpt-image-2`, `gpt-image-2-2026-04-21`, or `chatgpt-image-latest`). Defaults to `gpt-image-1.5`.

One of the following:

String = String

ImageModel = :"gpt-image-1" | :"gpt-image-1-mini" | :"gpt-image-2" | 5 more

One of the following:

:"gpt-image-1"

:"gpt-image-1-mini"

:"gpt-image-2"

:"gpt-image-2-2026-04-21"

:"gpt-image-1.5"

:"chatgpt-image-latest"

:"dall-e-2"

:"dall-e-3"

n: Integer

The number of images to generate. Must be between 1 and 10.

minimum1

maximum10

output\_compression: Integer

The compression level (0-100%) for the generated images. This parameter
is only supported for the GPT image models with the `webp` or `jpeg` output
formats, and defaults to 100.

output\_format: :png | :jpeg | :webp

The format in which the generated images are returned. This parameter is
only supported for the GPT image models. Must be one of `png`, `jpeg`, or `webp`.
The default value is `png`.

One of the following:

:png

:jpeg

:webp

partial\_images: Integer

The number of partial images to generate. This parameter is used for
streaming responses that return partial images. Value must be between 0 and 3.
When set to 0, the response will be a single image sent in one streaming event.

Note that the final image may be sent before the full number of partial images
are generated if the full image is generated more quickly.

maximum3

minimum0

quality: :standard | :low | :medium | 2 more

The quality of the image that will be generated for GPT image models. Defaults to `auto`.

One of the following:

:standard

:low

:medium

:high

:auto

response\_format: :url | :b64\_json

The format in which the generated images are returned. Must be one of `url` or `b64_json`. URLs are only valid for 60 minutes after the image has been generated. This parameter is only supported for `dall-e-2` (default is `url` for `dall-e-2`), as GPT image models always return base64-encoded images.

One of the following:

:url

:b64\_json

size: String | :"256x256" | :"512x512" | :"1024x1024" | 3 more

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

String = String

Size = :"256x256" | :"512x512" | :"1024x1024" | 3 more

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

:"256x256"

:"512x512"

:"1024x1024"

:"1536x1024"

:"1024x1536"

:auto

stream: bool

Edit the image in streaming mode. Defaults to `false`. See the
[Image generation guide](https://platform.openai.com/docs/guides/image-generation) for more information.

user: String

A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#end-user-ids).

##### ReturnsExpand Collapse

class ImagesResponse { created, background, data, 4 more }

The response from the image generation endpoint.

created: Integer

The Unix timestamp (in seconds) of when the image was created.

formatunixtime

background: :transparent | :opaque

The background parameter used for the image generation. Either `transparent` or `opaque`.

One of the following:

:transparent

:opaque

data: Array[[Image](/api/reference/ruby/resources/images#(resource)%20images%20%3E%20(model)%20image%20%3E%20(schema)) { b64\_json, revised\_prompt, url } ]

The list of generated images.

b64\_json: String

The base64-encoded JSON of the generated image. Returned by default for the GPT image models, and only present if `response_format` is set to `b64_json` for `dall-e-2` and `dall-e-3`.

revised\_prompt: String

For `dall-e-3` only, the revised prompt that was used to generate the image.

url: String

When using `dall-e-2` or `dall-e-3`, the URL of the generated image if `response_format` is set to `url` (default value). Unsupported for the GPT image models.

formaturi

output\_format: :png | :webp | :jpeg

The output format of the image generation. Either `png`, `webp`, or `jpeg`.

One of the following:

:png

:webp

:jpeg

quality: :low | :medium | :high

The quality of the image generated. Either `low`, `medium`, or `high`.

One of the following:

:low

:medium

:high

size: :"1024x1024" | :"1024x1536" | :"1536x1024"

The size of the image generated. Either `1024x1024`, `1024x1536`, or `1536x1024`.

One of the following:

:"1024x1024"

:"1024x1536"

:"1536x1024"

usage: Usage{ input\_tokens, input\_tokens\_details, output\_tokens, 2 more}

For `gpt-image-1` only, the token usage information for the image generation.

input\_tokens: Integer

The number of tokens (images and text) in the input prompt.

input\_tokens\_details: InputTokensDetails{ image\_tokens, text\_tokens}

The input tokens detailed information for the image generation.

image\_tokens: Integer

The number of image tokens in the input prompt.

text\_tokens: Integer

The number of text tokens in the input prompt.

output\_tokens: Integer

The number of output tokens generated by the model.

total\_tokens: Integer

The total number of tokens (images and text) used for the image generation.

output\_tokens\_details: OutputTokensDetails{ image\_tokens, text\_tokens}

The output token details for the image generation.

image\_tokens: Integer

The number of image output tokens generated by the model.

text\_tokens: Integer

The number of text output tokens generated by the model.

ImageEditStreamEvent = [ImageEditPartialImageEvent](/api/reference/ruby/resources/images#(resource)%20images%20%3E%20(model)%20image_edit_partial_image_event%20%3E%20(schema)) { b64\_json, background, created\_at, 5 more }  | [ImageEditCompletedEvent](/api/reference/ruby/resources/images#(resource)%20images%20%3E%20(model)%20image_edit_completed_event%20%3E%20(schema)) { b64\_json, background, created\_at, 5 more }

Emitted when a partial image is available during image editing streaming.

One of the following:

class ImageEditPartialImageEvent { b64\_json, background, created\_at, 5 more }

Emitted when a partial image is available during image editing streaming.

b64\_json: String

Base64-encoded partial image data, suitable for rendering as an image.

background: :transparent | :opaque | :auto

The background setting for the requested edited image.

One of the following:

:transparent

:opaque

:auto

created\_at: Integer

The Unix timestamp when the event was created.

formatunixtime

output\_format: :png | :webp | :jpeg

The output format for the requested edited image.

One of the following:

:png

:webp

:jpeg

partial\_image\_index: Integer

0-based index for the partial image (streaming).

quality: :low | :medium | :high | :auto

The quality setting for the requested edited image.

One of the following:

:low

:medium

:high

:auto

size: :"1024x1024" | :"1024x1536" | :"1536x1024" | :auto

The size of the requested edited image.

One of the following:

:"1024x1024"

:"1024x1536"

:"1536x1024"

:auto

type: :"image\_edit.partial\_image"

The type of the event. Always `image_edit.partial_image`.

class ImageEditCompletedEvent { b64\_json, background, created\_at, 5 more }

Emitted when image editing has completed and the final image is available.

b64\_json: String

Base64-encoded final edited image data, suitable for rendering as an image.

background: :transparent | :opaque | :auto

The background setting for the edited image.

One of the following:

:transparent

:opaque

:auto

created\_at: Integer

The Unix timestamp when the event was created.

formatunixtime

output\_format: :png | :webp | :jpeg

The output format for the edited image.

One of the following:

:png

:webp

:jpeg

quality: :low | :medium | :high | :auto

The quality setting for the edited image.

One of the following:

:low

:medium

:high

:auto

size: :"1024x1024" | :"1024x1536" | :"1536x1024" | :auto

The size of the edited image.

One of the following:

:"1024x1024"

:"1024x1536"

:"1536x1024"

:auto

type: :"image\_edit.completed"

The type of the event. Always `image_edit.completed`.

usage: Usage{ input\_tokens, input\_tokens\_details, output\_tokens, total\_tokens}

For the GPT image models only, the token usage information for the image generation.

input\_tokens: Integer

The number of tokens (images and text) in the input prompt.

input\_tokens\_details: InputTokensDetails{ image\_tokens, text\_tokens}

The input tokens detailed information for the image generation.

image\_tokens: Integer

The number of image tokens in the input prompt.

text\_tokens: Integer

The number of text tokens in the input prompt.

output\_tokens: Integer

The number of image tokens in the output image.

total\_tokens: Integer

The total number of tokens (images and text) used for the image generation.

### Create image edit

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

images_response = openai.images.edit(image: StringIO.new("Example data"), prompt: "A cute baby sea otter wearing a beret")

puts(images_response)

200 example

  "created": 0,
  "background": "transparent",
  "data": [
      "b64_json": "b64_json",
      "revised_prompt": "revised_prompt",
      "url": "https://example.com"
  ],
  "output_format": "png",
  "quality": "low",
  "size": "1024x1024",
  "usage": {
    "input_tokens": 0,
    "input_tokens_details": {
      "image_tokens": 0,
      "text_tokens": 0
    "output_tokens": 0,
    "total_tokens": 0,
    "output_tokens_details": {
      "image_tokens": 0,
      "text_tokens": 0

##### Returns Examples

200 example

  "created": 0,
  "background": "transparent",
  "data": [
      "b64_json": "b64_json",
      "revised_prompt": "revised_prompt",
      "url": "https://example.com"
  ],
  "output_format": "png",
  "quality": "low",
  "size": "1024x1024",
  "usage": {
    "input_tokens": 0,
    "input_tokens_details": {
      "image_tokens": 0,
      "text_tokens": 0
    "output_tokens": 0,
    "total_tokens": 0,
    "output_tokens_details": {
      "image_tokens": 0,
      "text_tokens": 0
