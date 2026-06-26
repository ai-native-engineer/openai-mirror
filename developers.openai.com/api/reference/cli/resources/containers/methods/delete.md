<!-- source: https://developers.openai.com/api/reference/cli/resources/containers/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Containers](/api/reference/cli/resources/containers)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete a container

$ openai containers delete

DELETE/containers/{container\_id}

Delete Container

##### ParametersExpand Collapse

--container-id: string

The ID of the container to delete.

### Delete a container

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai containers delete \
  --api-key 'My API Key' \
  --container-id container_id

    "id": "cntr_682dfebaacac8198bbfe9c2474fb6f4a085685cbe3cb5863",
    "object": "container.deleted",
    "deleted": true

##### Returns Examples

    "id": "cntr_682dfebaacac8198bbfe9c2474fb6f4a085685cbe3cb5863",
    "object": "container.deleted",
    "deleted": true
