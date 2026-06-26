<!-- source: https://developers.openai.com/api/reference/typescript/resources/uploads/subresources/parts/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Uploads](/api/reference/typescript/resources/uploads)

[Parts](/api/reference/typescript/resources/uploads/subresources/parts)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Add upload part

client.uploads.parts.create(stringuploadID, PartCreateParams { data } body, RequestOptionsoptions?): [UploadPart](/api/reference/typescript/resources/uploads#(resource)%20uploads.parts%20%3E%20(model)%20upload_part%20%3E%20(schema)) { id, created\_at, object, upload\_id }

POST/uploads/{upload\_id}/parts

Adds a [Part](https://platform.openai.com/docs/api-reference/uploads/part-object) to an [Upload](https://platform.openai.com/docs/api-reference/uploads/object) object. A Part represents a chunk of bytes from the file you are trying to upload.

Each Part can be at most 64 MB, and you can add Parts until you hit the Upload maximum of 8 GB.

It is possible to add multiple Parts in parallel. You can decide the intended order of the Parts when you [complete the Upload](https://platform.openai.com/docs/api-reference/uploads/complete).

##### ParametersExpand Collapse

uploadID: string

body: PartCreateParams { data }

data: [Uploadable](/api/reference/typescript/resources/uploads/subresources/parts/methods/create#(resource)%20uploads.parts%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20data%20%3E%20(schema))

The chunk of bytes for this Part.

##### ReturnsExpand Collapse

UploadPart { id, created\_at, object, upload\_id }

The upload Part represents a chunk of bytes we can add to an Upload object.

id: string

The upload Part unique identifier, which can be referenced in API endpoints.

created\_at: number

The Unix timestamp (in seconds) for when the Part was created.

formatunixtime

object: "upload.part"

The object type, which is always `upload.part`.

upload\_id: string

The ID of the Upload object that this Part was added to.

### Add upload part

TypeScript

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import fs from 'fs';
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted

const uploadPart = await client.uploads.parts.create('upload_abc123', {
  data: fs.createReadStream('path/to/file'),

console.log(uploadPart.id);

  "id": "part_def456",
  "object": "upload.part",
  "created_at": 1719185911,
  "upload_id": "upload_abc123"

##### Returns Examples

  "id": "part_def456",
  "object": "upload.part",
  "created_at": 1719185911,
  "upload_id": "upload_abc123"
