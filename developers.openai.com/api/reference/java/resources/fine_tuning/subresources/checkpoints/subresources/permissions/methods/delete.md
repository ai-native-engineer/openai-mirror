<!-- source: https://developers.openai.com/api/reference/java/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Fine Tuning](/api/reference/java/resources/fine_tuning)

[Checkpoints](/api/reference/java/resources/fine_tuning/subresources/checkpoints)

[Permissions](/api/reference/java/resources/fine_tuning/subresources/checkpoints/subresources/permissions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete checkpoint permission

[PermissionDeleteResponse](/api/reference/java/resources/fine_tuning#(resource)%20fine_tuning.checkpoints.permissions%20%3E%20(model)%20PermissionDeleteResponse%20%3E%20(schema)) fineTuning().checkpoints().permissions().delete(PermissionDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions/{permission\_id}

**NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

Organization owners can use this endpoint to delete a permission for a fine-tuned model checkpoint.

##### ParametersExpand Collapse

PermissionDeleteParams params

String fineTunedModelCheckpoint

Optional<String> permissionId

##### ReturnsExpand Collapse

class PermissionDeleteResponse:

String id

The ID of the fine-tuned model checkpoint permission that was deleted.

boolean deleted

Whether the fine-tuned model checkpoint permission was successfully deleted.

JsonValue; object\_ "checkpoint.permission"constant"checkpoint.permission"constant

The object type, which is always “checkpoint.permission”.

### Delete checkpoint permission

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
import com.openai.models.finetuning.checkpoints.permissions.PermissionDeleteParams;
import com.openai.models.finetuning.checkpoints.permissions.PermissionDeleteResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        PermissionDeleteParams params = PermissionDeleteParams.builder()
            .fineTunedModelCheckpoint("ft:gpt-4o-mini-2024-07-18:org:weather:B7R9VjQd")
            .permissionId("cp_zc4Q7MP6XxulcVzj4MZdwsAB")
            .build();
        PermissionDeleteResponse permission = client.fineTuning().checkpoints().permissions().delete(params);

  "object": "checkpoint.permission",
  "id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
  "deleted": true

##### Returns Examples

  "object": "checkpoint.permission",
  "id": "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
  "deleted": true
