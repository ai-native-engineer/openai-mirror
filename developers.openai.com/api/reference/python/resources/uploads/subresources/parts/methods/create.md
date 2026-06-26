<!-- source: https://developers.openai.com/api/reference/python/resources/uploads/subresources/parts/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Uploads](/api/reference/python/resources/uploads)

[Parts](/api/reference/python/resources/uploads/subresources/parts)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Add upload part

uploads.parts.create(strupload\_id, PartCreateParams\*\*kwargs)  -> [UploadPart](/api/reference/python/resources/uploads#(resource)%20uploads.parts%20%3E%20(model)%20upload_part%20%3E%20(schema))

POST/uploads/{upload\_id}/parts

Adds a [Part](https://platform.openai.com/docs/api-reference/uploads/part-object) to an [Upload](https://platform.openai.com/docs/api-reference/uploads/object) object. A Part represents a chunk of bytes from the file you are trying to upload.

Each Part can be at most 64 MB, and you can add Parts until you hit the Upload maximum of 8 GB.

It is possible to add multiple Parts in parallel. You can decide the intended order of the Parts when you [complete the Upload](https://platform.openai.com/docs/api-reference/uploads/complete).

##### ParametersExpand Collapse

upload\_id: str

data: [FileTypes](/api/reference/python/resources/uploads/subresources/parts/methods/create#(resource)%20uploads.parts%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20data%20%3E%20(schema))

The chunk of bytes for this Part.

##### ReturnsExpand Collapse

class UploadPart: …

The upload Part represents a chunk of bytes we can add to an Upload object.

id: str

The upload Part unique identifier, which can be referenced in API endpoints.

created\_at: int

The Unix timestamp (in seconds) for when the Part was created.

formatunixtime

object: Literal["upload.part"]

The object type, which is always `upload.part`.

upload\_id: str

The ID of the Upload object that this Part was added to.

### Add upload part

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
upload_part = client.uploads.parts.create(
    upload_id="upload_abc123",
    data=b"Example data",
print(upload_part.id)

  "id": "part_def456",
  "object": "upload.part",
  "created_at": 1719185911,
  "upload_id": "upload_abc123"

##### Returns Examples

  "id": "part_def456",
  "object": "upload.part",
  "created_at": 1719185911,
  "upload_id": "upload_abc123"
