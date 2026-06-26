<!-- source: https://developers.openai.com/api/reference/go/resources/images/methods/create_variation/ -->

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

# Create image variation

client.Images.NewVariation(ctx, body) (\*[ImagesResponse](/api/reference/go/resources/images#(resource)%20images%20%3E%20(model)%20images_response%20%3E%20(schema)), error)

POST/images/variations

Creates a variation of a given image. This endpoint only supports `dall-e-2`.

##### ParametersExpand Collapse

body ImageNewVariationParams

Image param.Field[[Reader](/api/reference/go/resources/images/methods/create_variation#(resource)%20images%20%3E%20(method)%20create_variation%20%3E%20(params)%20default%20%3E%20(param)%20image%20%3E%20(schema))]

The image to use as the basis for the variation(s). Must be a valid PNG file, less than 4MB, and square.

Model param.Field[[ImageModel](/api/reference/go/resources/images#(resource)%20images%20%3E%20(model)%20image_model%20%3E%20(schema))]Optional

The model to use for image generation. Only `dall-e-2` is supported at this time.

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

ResponseFormat param.Field[[ImageNewVariationParamsResponseFormat](/api/reference/go/resources/images/methods/create_variation#(resource)%20images%20%3E%20(method)%20create_variation%20%3E%20(params)%20default%20%3E%20(param)%20response_format%20%3E%20(schema))]Optional

The format in which the generated images are returned. Must be one of `url` or `b64_json`. URLs are only valid for 60 minutes after the image has been generated.

const ImageNewVariationParamsResponseFormatURL [ImageNewVariationParamsResponseFormat](/api/reference/go/resources/images/methods/create_variation#(resource)%20images%20%3E%20(method)%20create_variation%20%3E%20(params)%20default%20%3E%20(param)%20response_format%20%3E%20(schema)) = "url"

const ImageNewVariationParamsResponseFormatB64JSON [ImageNewVariationParamsResponseFormat](/api/reference/go/resources/images/methods/create_variation#(resource)%20images%20%3E%20(method)%20create_variation%20%3E%20(params)%20default%20%3E%20(param)%20response_format%20%3E%20(schema)) = "b64\_json"

Size param.Field[[ImageNewVariationParamsSize](/api/reference/go/resources/images/methods/create_variation#(resource)%20images%20%3E%20(method)%20create_variation%20%3E%20(params)%20default%20%3E%20(param)%20size%20%3E%20(schema))]Optional

The size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024`.

const ImageNewVariationParamsSize256x256 [ImageNewVariationParamsSize](/api/reference/go/resources/images/methods/create_variation#(resource)%20images%20%3E%20(method)%20create_variation%20%3E%20(params)%20default%20%3E%20(param)%20size%20%3E%20(schema)) = "256x256"

const ImageNewVariationParamsSize512x512 [ImageNewVariationParamsSize](/api/reference/go/resources/images/methods/create_variation#(resource)%20images%20%3E%20(method)%20create_variation%20%3E%20(params)%20default%20%3E%20(param)%20size%20%3E%20(schema)) = "512x512"

const ImageNewVariationParamsSize1024x1024 [ImageNewVariationParamsSize](/api/reference/go/resources/images/methods/create_variation#(resource)%20images%20%3E%20(method)%20create_variation%20%3E%20(params)%20default%20%3E%20(param)%20size%20%3E%20(schema)) = "1024x1024"

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

### Create image variation

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
  imagesResponse, err := client.Images.NewVariation(context.TODO(), openai.ImageNewVariationParams{
    Image: io.Reader(bytes.NewBuffer([]byte("Example data"))),
  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", imagesResponse.Created)

  "created": 1589478378,
  "data": [
      "url": "https://..."
      "url": "https://..."
  ]

##### Returns Examples

  "created": 1589478378,
  "data": [
      "url": "https://..."
      "url": "https://..."
  ]
