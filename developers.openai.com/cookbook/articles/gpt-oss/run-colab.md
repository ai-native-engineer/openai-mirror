<!-- source: https://developers.openai.com/cookbook/articles/gpt-oss/run-colab/ -->

## Search the cookbook

Aug 6, 2025

# How to run gpt-oss-20b on Google Colab

This recipe is archived and may reference outdated models or APIs.

[![Pedro Cuenca](https://cdn-avatars.huggingface.co/v1/production/uploads/1617264212503-603d25b75f9d390ab190b777.jpeg)  PC](https://huggingface.co/pcuenq)  [![vb](https://cdn-avatars.huggingface.co/v1/production/uploads/1655385361868-61b85ce86eb1f2c5e6233736.jpeg)  VB](https://huggingface.co/reach-vb)

[Pedro Cuenca ,](https://huggingface.co/pcuenq)  [vb](https://huggingface.co/reach-vb)

[View on GitHub](https://github.com/openai/openai-cookbook/blob/main/articles/gpt-oss/run-colab.ipynb) [Download raw](https://raw.githubusercontent.com/openai/openai-cookbook/main/articles/gpt-oss/run-colab.ipynb)

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/openai/openai-cookbook/blob/main/articles/gpt-oss/run-colab.ipynb)

# Run OpenAI gpt-oss 20B in a FREE Google Colab

OpenAI released `gpt-oss` [120B](https://hf.co/openai/gpt-oss-120b) and [20B](https://hf.co/openai/gpt-oss-20b). Both models are Apache 2.0 licensed.

Specifically, `gpt-oss-20b` was made for lower latency and local or specialized use cases (21B parameters with 3.6B active parameters).

Since the models were trained in native MXFP4 quantization it makes it easy to run the 20B even in resource constrained environments like Google Colab.

Authored by: [Pedro](https://huggingface.co/pcuenq) and [VB](https://huggingface.co/reach-vb)

## Setup environment

Since support for mxfp4 in transformers is bleeding edge, we need a recent version of PyTorch and CUDA, in order to be able to install the `mxfp4` triton kernels.

We also need to install transformers from source, and we uninstall `torchvision` and `torchaudio` to remove dependency conflicts.

!pip install -q --upgrade torch

!pip install -q transformers triton==3.4 kernels

!pip uninstall -q torchvision torchaudio -y

Please, restart your Colab runtime session after installing the packages above.

## Load the model from Hugging Face in Google Colab

We load the model from here: [openai/gpt-oss-20b](https://hf.co/openai/gpt-oss-20b)

from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "openai/gpt-oss-20b"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype="auto",
    device_map="cuda",

## Setup messages/ chat

You can provide an optional system prompt or directly the input.

messages = [
    {"role": "system", "content": "Always respond in riddles"},
    {"role": "user", "content": "What is the weather like in Madrid?"},
]

inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt",
    return_dict=True,
).to(model.device)

generated = model.generate(**inputs, max_new_tokens=500)
print(tokenizer.decode(generated[0][inputs["input_ids"].shape[-1]:]))

## Specify Reasoning Effort

Simply pass it as an additional argument to `apply_chat_template()`. Supported values are `"low"`, `"medium"` (default), or `"high"`.

messages = [
    {"role": "system", "content": "Always respond in riddles"},
    {"role": "user", "content": "Explain why the meaning of life is 42"},
]

inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt",
    return_dict=True,
    reasoning_effort="high",
).to(model.device)

generated = model.generate(**inputs, max_new_tokens=500)
print(tokenizer.decode(generated[0][inputs["input_ids"].shape[-1]:]))

## Try out other prompts and ideas!

Check out our blogpost for other ideas: <https://hf.co/blog/welcome-openai-gpt-oss>
