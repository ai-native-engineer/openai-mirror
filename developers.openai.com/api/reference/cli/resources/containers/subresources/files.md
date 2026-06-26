<!-- source: https://developers.openai.com/api/reference/cli/resources/containers/subresources/files/ -->

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

# Files

##### [List container files](/api/reference/cli/resources/containers/subresources/files/methods/list)

$ openai containers:files list

GET/containers/{container\_id}/files

##### [Create container file](/api/reference/cli/resources/containers/subresources/files/methods/create)

$ openai containers:files create

POST/containers/{container\_id}/files

##### [Retrieve container file](/api/reference/cli/resources/containers/subresources/files/methods/retrieve)

$ openai containers:files retrieve

GET/containers/{container\_id}/files/{file\_id}

##### [Delete a container file](/api/reference/cli/resources/containers/subresources/files/methods/delete)

$ openai containers:files delete

DELETE/containers/{container\_id}/files/{file\_id}

#### FilesContent

##### [Retrieve container file content](/api/reference/cli/resources/containers/subresources/files/subresources/content/methods/retrieve)

$ openai containers:files:content retrieve

GET/containers/{container\_id}/files/{file\_id}/content
