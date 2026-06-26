<!-- source: https://developers.openai.com/api/reference/cli/resources/containers/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Containers

##### [List containers](/api/reference/cli/resources/containers/methods/list)

$ openai containers list

GET/containers

##### [Create container](/api/reference/cli/resources/containers/methods/create)

$ openai containers create

POST/containers

##### [Retrieve container](/api/reference/cli/resources/containers/methods/retrieve)

$ openai containers retrieve

GET/containers/{container\_id}

##### [Delete a container](/api/reference/cli/resources/containers/methods/delete)

$ openai containers delete

DELETE/containers/{container\_id}

#### ContainersFiles

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

#### ContainersFilesContent

##### [Retrieve container file content](/api/reference/cli/resources/containers/subresources/files/subresources/content/methods/retrieve)

$ openai containers:files:content retrieve

GET/containers/{container\_id}/files/{file\_id}/content
