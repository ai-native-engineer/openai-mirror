<!-- source: https://developers.openai.com/api/reference/go/resources/images/methods/edit/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Images](/api/reference/go/resources/images)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create image edit

client.Images.Edit(ctx, body) (\*[ImagesResponse](/api/reference/go/resources/images#(resource)%20images%20%3E%20(model)%20images_response%20%3E%20(schema)), error)

POST/images/edits

Creates an edited or extended image given one or more source images and a prompt. This endpoint supports GPT Image models (`gpt-image-1.5`, `gpt-image-1`, `gpt-image-1-mini`, and `chatgpt-image-latest`) and `dall-e-2`.

##### ParametersExpand Collapse

body ImageEditParams

Image param.Field[[ImageEditParamsImageUnion](/api/reference/go/resources/images/methods/edit#(resource)%20images%20%3E%20(method)%20edit%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20image%20%3E%20(schema))]

The image(s) to edit. Must be a supported image file or an array of images.

For the GPT image models (`gpt-image-1`, `gpt-image-1-mini`,
`gpt-image-1.5`, `gpt-image-2`, `gpt-image-2-2026-04-21`, and
`chatgpt-image-latest`), each image should be a `png`, `webp`, or
`jpg` file less than 50MB. You can provide up to 16 images.

For `dall-e-2`, you can only provide one image, and it should be a
square `png` file less than 4MB.

Reader

[]Reader

Prompt param.Field[string]

A text description of the desired image(s). The maximum length is 1000 characters for `dall-e-2`, and 32000 characters for the GPT image models.

Background param.Field[[ImageEditParamsBackground](/api/reference/go/resources/images/methods/edit#(resource)%20images%20%3E%20(method)%20edit%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20background%20%3E%20(schema))]Optional

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

const ImageEditParamsBackgroundTransparent [ImageEditParamsBackground](/api/reference/go/resources/images/methods/edit#(resource)%20images%20%3E%20(method)%20edit%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20background%20%3E%20(schema)) = "transparent"

const ImageEditParamsBackgroundOpaque [ImageEditParamsBackground](/api/reference/go/resources/images/methods/edit#(resource)%20images%20%3E%20(method)%20edit%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20background%20%3E%20(schema)) = "opaque"

const ImageEditParamsBackgroundAuto [ImageEditParamsBackground](/api/reference/go/resources/images/methods/edit#(resource)%20images%20%3E%20(method)%20edit%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20background%20%3E%20(schema)) = "auto"

InputFidelity param.Field[[ImageEditParamsInputFidelity](/api/reference/go/resources/images/methods/edit#(resource)%20images%20%3E%20(method)%20edit%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20input_fidelity%20%3E%20(schema))]Optional

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

const ImageEditParamsInputFidelityHigh [ImageEditParamsInputFidelity](/api/reference/go/resources/images/methods/edit#(resource)%20images%20%3E%20(method)%20edit%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20input_fidelity%20%3E%20(schema)) = "high"

const ImageEditParamsInputFidelityLow [ImageEditParamsInputFidelity](/api/reference/go/resources/images/methods/edit#(resource)%20images%20%3E%20(method)%20edit%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20input_fidelity%20%3E%20(schema)) = "low"

Mask param.Field[[Reader](/api/reference/go/resources/images/methods/edit#(resource)%20images%20%3E%20(method)%20edit%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20mask%20%3E%20(schema))]Optional

An additional image whose fully transparent areas (e.g. where alpha is zero) indicate where `image` should be edited. If there are multiple images provided, the mask will be applied on the first image. Must be a valid PNG file, less than 4MB, and have the same dimensions as `image`.

Model param.Field[[ImageModel](/api/reference/go/resources/images#(resource)%20images%20%3E%20(model)%20image_model%20%3E%20(schema))]Optional

The model to use for image generation. One of `dall-e-2` or a GPT image model (`gpt-image-1`, `gpt-image-1-mini`, `gpt-image-1.5`, `gpt-image-2`, `gpt-image-2-2026-04-21`, or `chatgpt-image-latest`). Defaults to `gpt-image-1.5`.

string

type ImageModel string

One of the following:

const ImageModelGPTImage1 [ImageModel](/api/reference/go/resources/images#(resource)%20images%20%3E%20(model)%20image_model%20%3E%20(schema)) = "gpt-image-1"

const ImageModelGPTImage1Mini [ImageModel](/api/reference/go/resources/images#(resource)%20images%20%3E%20(model)%20image_model%20%3E%20(schema)) = "gpt-image-1-mini"

const ImageModelGPTImage2 [ImageModel](/api/reference/go/resources/images#(resource)%20images%20%3E%20(model)%20image_model%20%3E%20(schema)) = "gpt-image-2"

const ImageModelGPTImage2\_2026\_04\_21 [ImageModel](/api/reference/go/resources/images#(resource)%20images%20%3E%20(model)%20image_model%20%3E%20(schema)) = "gpt-image-2-2026-04-21"

const ImageModelGPTImage1\_5 [ImageModel](/api/reference/go/resources/images#(resource)%20images%20%3E%20(model)%20image_model%20%3E%20(schema)) = "gpt-image-1.5"

const ImageModelChatgptImageLatest [ImageModel](/api/reference/go/resources/images#(resource)%20images%20%3E%20(model)%20image_model%20%3E%20(schema)) = "chatgpt-image-latest"

const ImageModelDallE2 [ImageModel](/api/reference/go/resources/images#(resource)%20images%20%3E%20(model)%20image_model%20%3E%20(schema)) = "dall-e-2"

const ImageModelDallE3 [ImageModel](/api/reference/go/resources/images#(resource)%20images%20%3E%20(model)%20image_model%20%3E%20(schema)) = "dall-e-3"

N param.Field[int64]Optional

The number of images to generate. Must be between 1 and 10.

minimum1

maximum10

OutputCompression param.Field[int64]Optional

The compression level (0-100%) for the generated images. This parameter
is only supported for the GPT image models with the `webp` or `jpeg` output
formats, and defaults to 100.

OutputFormat param.Field[[ImageEditParamsOutputFormat](/api/reference/go/resources/images/methods/edit#(resource)%20images%20%3E%20(method)%20edit%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20output_format%20%3E%20(schema))]Optional

The format in which the generated images are returned. This parameter is
only supported for the GPT image models. Must be one of `png`, `jpeg`, or `webp`.
The default value is `png`.

const ImageEditParamsOutputFormatPNG [ImageEditParamsOutputFormat](/api/reference/go/resources/images/methods/edit#(resource)%20images%20%3E%20(method)%20edit%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20output_format%20%3E%20(schema)) = "png"

const ImageEditParamsOutputFormatJPEG [ImageEditParamsOutputFormat](/api/reference/go/resources/images/methods/edit#(resource)%20images%20%3E%20(method)%20edit%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20output_format%20%3E%20(schema)) = "jpeg"

const ImageEditParamsOutputFormatWebP [ImageEditParamsOutputFormat](/api/reference/go/resources/images/methods/edit#(resource)%20images%20%3E%20(method)%20edit%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20output_format%20%3E%20(schema)) = "webp"

PartialImages param.Field[int64]Optional

The number of partial images to generate. This parameter is used for
streaming responses that return partial images. Value must be between 0 and 3.
When set to 0, the response will be a single image sent in one streaming event.

Note that the final image may be sent before the full number of partial images
are generated if the full image is generated more quickly.

maximum3

minimum0

Quality param.Field[[ImageEditParamsQuality](/api/reference/go/resources/images/methods/edit#(resource)%20images%20%3E%20(method)%20edit%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20quality%20%3E%20(schema))]Optional

The quality of the image that will be generated for GPT image models. Defaults to `auto`.

const ImageEditParamsQualityStandard [ImageEditParamsQuality](/api/reference/go/resources/images/methods/edit#(resource)%20images%20%3E%20(method)%20edit%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20quality%20%3E%20(schema)) = "standard"

const ImageEditParamsQualityLow [ImageEditParamsQuality](/api/reference/go/resources/images/methods/edit#(resource)%20images%20%3E%20(method)%20edit%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20quality%20%3E%20(schema)) = "low"

const ImageEditParamsQualityMedium [ImageEditParamsQuality](/api/reference/go/resources/images/methods/edit#(resource)%20images%20%3E%20(method)%20edit%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20quality%20%3E%20(schema)) = "medium"

const ImageEditParamsQualityHigh [ImageEditParamsQuality](/api/reference/go/resources/images/methods/edit#(resource)%20images%20%3E%20(method)%20edit%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20quality%20%3E%20(schema)) = "high"

const ImageEditParamsQualityAuto [ImageEditParamsQuality](/api/reference/go/resources/images/methods/edit#(resource)%20images%20%3E%20(method)%20edit%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20quality%20%3E%20(schema)) = "auto"

ResponseFormat param.Field[[ImageEditParamsResponseFormat](/api/reference/go/resources/images/methods/edit#(resource)%20images%20%3E%20(method)%20edit%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20response_format%20%3E%20(schema))]Optional

The format in which the generated images are returned. Must be one of `url` or `b64_json`. URLs are only valid for 60 minutes after the image has been generated. This parameter is only supported for `dall-e-2` (default is `url` for `dall-e-2`), as GPT image models always return base64-encoded images.

const ImageEditParamsResponseFormatURL [ImageEditParamsResponseFormat](/api/reference/go/resources/images/methods/edit#(resource)%20images%20%3E%20(method)%20edit%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20response_format%20%3E%20(schema)) = "url"

const ImageEditParamsResponseFormatB64JSON [ImageEditParamsResponseFormat](/api/reference/go/resources/images/methods/edit#(resource)%20images%20%3E%20(method)%20edit%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20response_format%20%3E%20(schema)) = "b64\_json"

Size param.Field[ImageEditParamsSize]Optional

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

string

ImageEditParamsSize

One of the following:

const ImageEditParamsSize256x256 ImageEditParamsSize = "256x256"

const ImageEditParamsSize512x512 ImageEditParamsSize = "512x512"

const ImageEditParamsSize1024x1024 ImageEditParamsSize = "1024x1024"

const ImageEditParamsSize1536x1024 ImageEditParamsSize = "1536x1024"

const ImageEditParamsSize1024x1536 ImageEditParamsSize = "1024x1536"

const ImageEditParamsSizeAuto ImageEditParamsSize = "auto"

User param.Field[string]Optional

A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#end-user-ids).

##### ReturnsExpand Collapse

type ImagesResponse struct{…}

The response from the image generation endpoint.

Created int64

The Unix timestamp (in seconds) of when the image was created.

formatunixtime

Background ImagesResponseBackgroundOptional

The background parameter used for the image generation. Either `transparent` or `opaque`.

One of the following:

const ImagesResponseBackgroundTransparent ImagesResponseBackground = "transparent"

const ImagesResponseBackgroundOpaque ImagesResponseBackground = "opaque"

Data [][Image](/api/reference/go/resources/images#(resource)%20images%20%3E%20(model)%20image%20%3E%20(schema))Optional

The list of generated images.

B64JSON stringOptional

The base64-encoded JSON of the generated image. Returned by default for the GPT image models, and only present if `response_format` is set to `b64_json` for `dall-e-2` and `dall-e-3`.

RevisedPrompt stringOptional

For `dall-e-3` only, the revised prompt that was used to generate the image.

URL stringOptional

When using `dall-e-2` or `dall-e-3`, the URL of the generated image if `response_format` is set to `url` (default value). Unsupported for the GPT image models.

formaturi

OutputFormat ImagesResponseOutputFormatOptional

The output format of the image generation. Either `png`, `webp`, or `jpeg`.

One of the following:

const ImagesResponseOutputFormatPNG ImagesResponseOutputFormat = "png"

const ImagesResponseOutputFormatWebP ImagesResponseOutputFormat = "webp"

const ImagesResponseOutputFormatJPEG ImagesResponseOutputFormat = "jpeg"

Quality ImagesResponseQualityOptional

The quality of the image generated. Either `low`, `medium`, or `high`.

One of the following:

const ImagesResponseQualityLow ImagesResponseQuality = "low"

const ImagesResponseQualityMedium ImagesResponseQuality = "medium"

const ImagesResponseQualityHigh ImagesResponseQuality = "high"

Size ImagesResponseSizeOptional

The size of the image generated. Either `1024x1024`, `1024x1536`, or `1536x1024`.

One of the following:

const ImagesResponseSize1024x1024 ImagesResponseSize = "1024x1024"

const ImagesResponseSize1024x1536 ImagesResponseSize = "1024x1536"

const ImagesResponseSize1536x1024 ImagesResponseSize = "1536x1024"

Usage ImagesResponseUsageOptional

For `gpt-image-1` only, the token usage information for the image generation.

InputTokens int64

The number of tokens (images and text) in the input prompt.

InputTokensDetails ImagesResponseUsageInputTokensDetails

The input tokens detailed information for the image generation.

ImageTokens int64

The number of image tokens in the input prompt.

TextTokens int64

The number of text tokens in the input prompt.

OutputTokens int64

The number of output tokens generated by the model.

TotalTokens int64

The total number of tokens (images and text) used for the image generation.

OutputTokensDetails ImagesResponseUsageOutputTokensDetailsOptional

The output token details for the image generation.

ImageTokens int64

The number of image output tokens generated by the model.

TextTokens int64

The number of text output tokens generated by the model.

type ImageEditStreamEventUnion interface{…}

Emitted when a partial image is available during image editing streaming.

One of the following:

type ImageEditPartialImageEvent struct{…}

Emitted when a partial image is available during image editing streaming.

B64JSON string

Base64-encoded partial image data, suitable for rendering as an image.

Background ImageEditPartialImageEventBackground

The background setting for the requested edited image.

One of the following:

const ImageEditPartialImageEventBackgroundTransparent ImageEditPartialImageEventBackground = "transparent"

const ImageEditPartialImageEventBackgroundOpaque ImageEditPartialImageEventBackground = "opaque"

const ImageEditPartialImageEventBackgroundAuto ImageEditPartialImageEventBackground = "auto"

CreatedAt int64

The Unix timestamp when the event was created.

formatunixtime

OutputFormat ImageEditPartialImageEventOutputFormat

The output format for the requested edited image.

One of the following:

const ImageEditPartialImageEventOutputFormatPNG ImageEditPartialImageEventOutputFormat = "png"

const ImageEditPartialImageEventOutputFormatWebP ImageEditPartialImageEventOutputFormat = "webp"

const ImageEditPartialImageEventOutputFormatJPEG ImageEditPartialImageEventOutputFormat = "jpeg"

PartialImageIndex int64

0-based index for the partial image (streaming).

Quality ImageEditPartialImageEventQuality

The quality setting for the requested edited image.

One of the following:

const ImageEditPartialImageEventQualityLow ImageEditPartialImageEventQuality = "low"

const ImageEditPartialImageEventQualityMedium ImageEditPartialImageEventQuality = "medium"

const ImageEditPartialImageEventQualityHigh ImageEditPartialImageEventQuality = "high"

const ImageEditPartialImageEventQualityAuto ImageEditPartialImageEventQuality = "auto"

Size ImageEditPartialImageEventSize

The size of the requested edited image.

One of the following:

const ImageEditPartialImageEventSize1024x1024 ImageEditPartialImageEventSize = "1024x1024"

const ImageEditPartialImageEventSize1024x1536 ImageEditPartialImageEventSize = "1024x1536"

const ImageEditPartialImageEventSize1536x1024 ImageEditPartialImageEventSize = "1536x1024"

const ImageEditPartialImageEventSizeAuto ImageEditPartialImageEventSize = "auto"

Type ImageEditPartialImage

The type of the event. Always `image_edit.partial_image`.

type ImageEditCompletedEvent struct{…}

Emitted when image editing has completed and the final image is available.

B64JSON string

Base64-encoded final edited image data, suitable for rendering as an image.

Background ImageEditCompletedEventBackground

The background setting for the edited image.

One of the following:

const ImageEditCompletedEventBackgroundTransparent ImageEditCompletedEventBackground = "transparent"

const ImageEditCompletedEventBackgroundOpaque ImageEditCompletedEventBackground = "opaque"

const ImageEditCompletedEventBackgroundAuto ImageEditCompletedEventBackground = "auto"

CreatedAt int64

The Unix timestamp when the event was created.

formatunixtime

OutputFormat ImageEditCompletedEventOutputFormat

The output format for the edited image.

One of the following:

const ImageEditCompletedEventOutputFormatPNG ImageEditCompletedEventOutputFormat = "png"

const ImageEditCompletedEventOutputFormatWebP ImageEditCompletedEventOutputFormat = "webp"

const ImageEditCompletedEventOutputFormatJPEG ImageEditCompletedEventOutputFormat = "jpeg"

Quality ImageEditCompletedEventQuality

The quality setting for the edited image.

One of the following:

const ImageEditCompletedEventQualityLow ImageEditCompletedEventQuality = "low"

const ImageEditCompletedEventQualityMedium ImageEditCompletedEventQuality = "medium"

const ImageEditCompletedEventQualityHigh ImageEditCompletedEventQuality = "high"

const ImageEditCompletedEventQualityAuto ImageEditCompletedEventQuality = "auto"

Size ImageEditCompletedEventSize

The size of the edited image.

One of the following:

const ImageEditCompletedEventSize1024x1024 ImageEditCompletedEventSize = "1024x1024"

const ImageEditCompletedEventSize1024x1536 ImageEditCompletedEventSize = "1024x1536"

const ImageEditCompletedEventSize1536x1024 ImageEditCompletedEventSize = "1536x1024"

const ImageEditCompletedEventSizeAuto ImageEditCompletedEventSize = "auto"

Type ImageEditCompleted

The type of the event. Always `image_edit.completed`.

Usage ImageEditCompletedEventUsage

For the GPT image models only, the token usage information for the image generation.

InputTokens int64

The number of tokens (images and text) in the input prompt.

InputTokensDetails ImageEditCompletedEventUsageInputTokensDetails

The input tokens detailed information for the image generation.

ImageTokens int64

The number of image tokens in the input prompt.

TextTokens int64

The number of text tokens in the input prompt.

OutputTokens int64

The number of image tokens in the output image.

TotalTokens int64

The total number of tokens (images and text) used for the image generation.

### Create image edit

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
  "bytes"
  "context"
  "fmt"
  "io"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  imagesResponse, err := client.Images.Edit(context.TODO(), openai.ImageEditParams{
    Image: openai.ImageEditParamsImageUnion{
      OfFile: io.Reader(bytes.NewBuffer([]byte("Example data"))),
    Prompt: "A cute baby sea otter wearing a beret",
  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", imagesResponse)

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
