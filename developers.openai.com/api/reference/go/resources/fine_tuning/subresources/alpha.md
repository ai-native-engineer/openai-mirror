<!-- source: https://developers.openai.com/api/reference/go/resources/fine_tuning/subresources/alpha/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Fine Tuning](/api/reference/go/resources/fine_tuning)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Alpha

#### AlphaGraders

Manage fine-tuning jobs to tailor a model to your specific training data.

##### [Run grader](/api/reference/go/resources/fine_tuning/subresources/alpha/subresources/graders/methods/run)

client.FineTuning.Alpha.Graders.Run(ctx, body) (\*[FineTuningAlphaGraderRunResponse](/api/reference/go/resources/fine_tuning#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20FineTuningAlphaGraderRunResponse%20%3E%20(schema)), error)

POST/fine\_tuning/alpha/graders/run

##### [Validate grader](/api/reference/go/resources/fine_tuning/subresources/alpha/subresources/graders/methods/validate)

client.FineTuning.Alpha.Graders.Validate(ctx, body) (\*[FineTuningAlphaGraderValidateResponse](/api/reference/go/resources/fine_tuning#(resource)%20fine_tuning.alpha.graders%20%3E%20(model)%20FineTuningAlphaGraderValidateResponse%20%3E%20(schema)), error)

POST/fine\_tuning/alpha/graders/validate
