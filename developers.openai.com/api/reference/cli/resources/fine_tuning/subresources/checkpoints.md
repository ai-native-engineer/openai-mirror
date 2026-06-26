<!-- source: https://developers.openai.com/api/reference/cli/resources/fine_tuning/subresources/checkpoints/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Fine Tuning](/api/reference/cli/resources/fine_tuning)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Checkpoints

#### CheckpointsPermissions

Manage fine-tuning jobs to tailor a model to your specific training data.

##### [List checkpoint permissions](/api/reference/cli/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/retrieve)

Deprecated

$ openai fine-tuning:checkpoints:permissions retrieve

GET/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions

##### [List checkpoint permissions](/api/reference/cli/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/list)

$ openai fine-tuning:checkpoints:permissions list

GET/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions

##### [Create checkpoint permissions](/api/reference/cli/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/create)

$ openai fine-tuning:checkpoints:permissions create

POST/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions

##### [Delete checkpoint permission](/api/reference/cli/resources/fine_tuning/subresources/checkpoints/subresources/permissions/methods/delete)

$ openai fine-tuning:checkpoints:permissions delete

DELETE/fine\_tuning/checkpoints/{fine\_tuned\_model\_checkpoint}/permissions/{permission\_id}
