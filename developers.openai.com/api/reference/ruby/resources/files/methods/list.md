<!-- source: https://developers.openai.com/api/reference/ruby/resources/files/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Files](/api/reference/ruby/resources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List files

files.list(\*\*kwargs) -> CursorPage<[FileObject](/api/reference/ruby/resources/files#(resource)%20files%20%3E%20(model)%20file_object%20%3E%20(schema)) { id, bytes, created\_at, 6 more } >

GET/files

Returns a list of files.

##### ParametersExpand Collapse

after: String

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

limit: Integer

A limit on the number of objects to be returned. Limit can range between 1 and 10,000, and the default is 10,000.

order: :asc | :desc

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

One of the following:

:asc

:desc

purpose: String

Only return files with the given purpose.

##### ReturnsExpand Collapse

class FileObject { id, bytes, created\_at, 6 more }

The `File` object represents a document that has been uploaded to OpenAI.

id: String

The file identifier, which can be referenced in the API endpoints.

bytes: Integer

The size of the file, in bytes.

created\_at: Integer

The Unix timestamp (in seconds) for when the file was created.

formatunixtime

filename: String

The name of the file.

object: :file

The object type, which is always `file`.

purpose: :assistants | :assistants\_output | :batch | 5 more

The intended purpose of the file. Supported values are `assistants`, `assistants_output`, `batch`, `batch_output`, `fine-tune`, `fine-tune-results`, `vision`, and `user_data`.

One of the following:

:assistants

:assistants\_output

:batch

:batch\_output

:"fine-tune"

:"fine-tune-results"

:vision

:user\_data

Deprecatedstatus: :uploaded | :processed | :error

Deprecated. The current status of the file, which can be either `uploaded`, `processed`, or `error`.

One of the following:

:uploaded

:processed

:error

expires\_at: Integer

The Unix timestamp (in seconds) for when the file will expire.

formatunixtime

Deprecatedstatus\_details: String

Deprecated. For details on why a fine-tuning training file failed validation, see the `error` field on `fine_tuning.job`.

### List files

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

page = openai.files.list

puts(page)

  "object": "list",
  "data": [
      "id": "file-abc123",
      "object": "file",
      "bytes": 175,
      "created_at": 1613677385,
      "expires_at": 1677614202,
      "filename": "salesOverview.pdf",
      "purpose": "assistants",
      "id": "file-abc456",
      "object": "file",
      "bytes": 140,
      "created_at": 1613779121,
      "expires_at": 1677614202,
      "filename": "puppy.jsonl",
      "purpose": "fine-tune",
  ],
  "first_id": "file-abc123",
  "last_id": "file-abc456",
  "has_more": false

##### Returns Examples

  "object": "list",
  "data": [
      "id": "file-abc123",
      "object": "file",
      "bytes": 175,
      "created_at": 1613677385,
      "expires_at": 1677614202,
      "filename": "salesOverview.pdf",
      "purpose": "assistants",
      "id": "file-abc456",
      "object": "file",
      "bytes": 140,
      "created_at": 1613779121,
      "expires_at": 1677614202,
      "filename": "puppy.jsonl",
      "purpose": "fine-tune",
  ],
  "first_id": "file-abc123",
  "last_id": "file-abc456",
  "has_more": false
