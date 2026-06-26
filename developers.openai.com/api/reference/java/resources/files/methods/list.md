<!-- source: https://developers.openai.com/api/reference/java/resources/files/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Files](/api/reference/java/resources/files)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List files

FileListPage files().list(FileListParamsparams = FileListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/files

Returns a list of files.

##### ParametersExpand Collapse

FileListParams params

Optional<String> after

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

Optional<Long> limit

A limit on the number of objects to be returned. Limit can range between 1 and 10,000, and the default is 10,000.

Optional<[Order](/api/reference/java/resources/files/methods/list#(resource)%20files%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))> order

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

ASC("asc")

DESC("desc")

Optional<String> purpose

Only return files with the given purpose.

##### ReturnsExpand Collapse

class FileObject:

The `File` object represents a document that has been uploaded to OpenAI.

String id

The file identifier, which can be referenced in the API endpoints.

long bytes

The size of the file, in bytes.

long createdAt

The Unix timestamp (in seconds) for when the file was created.

formatunixtime

String filename

The name of the file.

JsonValue; object\_ "file"constant"file"constant

The object type, which is always `file`.

Purpose purpose

The intended purpose of the file. Supported values are `assistants`, `assistants_output`, `batch`, `batch_output`, `fine-tune`, `fine-tune-results`, `vision`, and `user_data`.

One of the following:

ASSISTANTS("assistants")

ASSISTANTS\_OUTPUT("assistants\_output")

BATCH("batch")

BATCH\_OUTPUT("batch\_output")

FINE\_TUNE("fine-tune")

FINE\_TUNE\_RESULTS("fine-tune-results")

VISION("vision")

USER\_DATA("user\_data")

DeprecatedStatus status

Deprecated. The current status of the file, which can be either `uploaded`, `processed`, or `error`.

One of the following:

UPLOADED("uploaded")

PROCESSED("processed")

ERROR("error")

Optional<Long> expiresAt

The Unix timestamp (in seconds) for when the file will expire.

formatunixtime

DeprecatedOptional<String> statusDetails

Deprecated. For details on why a fine-tuning training file failed validation, see the `error` field on `fine_tuning.job`.

### List files

Java

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.files.FileListPage;
import com.openai.models.files.FileListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FileListPage page = client.files().list();

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
