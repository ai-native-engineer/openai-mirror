<!-- source: https://help.openai.com/en/articles/11870455-openai-open-weight-models-gpt-oss -->

# OpenAI open-weight models (gpt-oss)

Learn about OpenAI’s open‑weight models (gpt-oss) and where to get support

Updated: 15 days ago

***Note:*** *This article provides a high‑level overview. Information for technical setup can be found on the* [*gpt-oss website*](https://openai.com/open-models/)*,* [*GitHub*](https://github.com/openai/gpt-oss)*,* [*Hugging Face*](https://huggingface.co/collections/openai/gpt-oss-68911959590a1634ba11c7a4)*, and* [*OpenAI Cookbooks*](https://cookbook.openai.com/topic/gpt-oss)*.*

# Overview

Introducing two open‑weight reasoning models: gpt‑oss‑120b and gpt‑oss‑20b. They run on infrastructure you control, or through hosting providers.

***Note:*** *These models are not served through the OpenAI API and are not available in ChatGPT.*

## Why open-weights

* **Choice and control:** Run models on‑premises or in your private cloud, keep data residency, and tailor performance for your needs.
* **Customization:** Fine‑tune or adapt the models with your preferred open tooling.

## Availability and licensing

* **License:** Apache 2.0 allows broad use, modification, and redistribution, including commercial use (subject to our gpt-oss [usage policy](https://huggingface.co/openai/gpt-oss-120b/blob/main/USAGE_POLICY)).
* **Serving:** Not available through the OpenAI API, so API pricing and rate limits do not apply.
* **Compatibility:** Can be run with common open inference stacks such as vLLM, Ollama, llama.cpp, and on cloud or self‑managed GPU environments.

# Getting started

To get the model weights and supporting resources, you can:

* Visit the [gpt-oss website](https://gpt-oss.com/) for an overview and direct links.
* Download weights from the [Hugging Face collection](https://huggingface.co/collections/openai/gpt-oss-68911959590a1634ba11c7a4) — a community hub where you can find both models, see usage examples, and optionally run inference directly through Hugging Face’s services.
* Access our [GitHub repo](https://github.com/openai/gpt-oss) for reference inference code.
* Use guides in the [OpenAI Cookbook](https://cookbook.openai.com/topic/gpt-oss) for setup with supported runtimes like Ollama, vLLM, and Transformers. The Cookbook also includes step‑by‑step instructions for running locally, using common runtimes, and—where supported—fine‑tuning gpt‑oss models.

# gpt‑oss‑safeguard (research preview)

`gpt‑oss‑safeguard` is a pair of **open‑weight safety reasoning models** built on top of gpt‑oss. They are designed for **policy‑based safety classification** and related trust & safety tasks you run on infrastructure you control. Like other gpt‑oss models, these weights are not served through the OpenAI API or ChatGPT.

* **Text‑only models** with reference structured‑output schemas (e.g., policy verdict, rationale).
* **Bring‑your‑own policy:** the model interprets your written policy so it can generalize across products with minimal engineering.
* **Reasoned decisions:** optional reasoning traces to aid debugging and audits (intended for developers and safety practitioners, not for end‑user display).
* **Configurable reasoning effort:** choose low / medium / high to trade off latency vs. depth.
* **License:** Apache 2.0 (see *Availability and licensing* below).

`gpt‑oss‑safeguard` is a good fit for input/output filtering for LLMs, online content labeling, and offline batch labeling or review workflows. For general applications (chat, agents, etc.), we recommend the core gpt‑oss models.

You can adapt the schema to your needs. Please refer to the [OpenAI Cookbook](https://cookbook.openai.com/articles/gpt-oss-safeguard-guide) for guides on prompting and examples.

## Model variants & sizing

| **Model** | **Intended use** | **Notes** |
| --- | --- | --- |
| **gpt‑oss‑safeguard‑120b** | Production, high‑capacity safety reasoning | 117B parameters (≈5.1B active). Designed to fit on a   **single 80 GB GPU**  (e.g., NVIDIA H100; also runs on larger‑memory GPUs such as AMD MI300X). |
| **gpt‑oss‑safeguard‑20b** | Lower‑latency / constrained environments | 21B parameters (≈3.6B active). |

Both models are fine‑tuned from gpt‑oss with no architecture change. They use the same chat template as gpt‑oss; you can keep your existing setup. A recommended prompting pattern is to place your policy in a developer message and the content to evaluate in a user message.

# Support and community

Open‑weight deployments are self‑managed and self-serviced. Here’s where to get support:

* **Questions, discussion, tips:** Use the [Hugging Face model pages](https://huggingface.co/collections/openai/gpt-oss-68911959590a1634ba11c7a4) to engage with the community.
* **Reproducible bugs in OpenAI’s reference inference code:** Open an issue on the gpt-oss [GitHub repo](https://github.com/openai/gpt-oss).
* **Issues with a third‑party runtime (e.g., vLLM, Ollama, llama.cpp):** Use the respective project’s issue tracker, forums, or support process.

OpenAI does **not** provide assistance, hands‑on implementation, or debugging support for any self‑hosted or third‑party‑hosted open‑weight setups, configurations, environments, or applications.  
  
We’ll continue to iterate with the community to improve open safety tooling, including through the ROOST Model Community (RMC). The RMC brings together safety practitioners and researchers to share best practices for implementing open source AI models into safety workflows, including evaluation outcomes and model feedback. Visit the [RMC GitHub repo](https://github.com/roostorg/open-models) to learn more about this partnership and how to get involved.

# Support and community

Open‑weight deployments are self‑managed and self-serviced. Here’s where to get support:

* **Questions, discussion, tips:** Use the [Hugging Face model pages](https://huggingface.co/collections/openai/gpt-oss-68911959590a1634ba11c7a4) to engage with the community.
* **Reproducible bugs in OpenAI’s reference inference code:** Open an issue on the gpt-oss [GitHub repo](https://github.com/openai/gpt-oss).
* **Issues with a third‑party runtime (e.g., vLLM, Ollama, llama.cpp):** Use the respective project’s issue tracker, forums, or support process.

OpenAI does **not** provide assistance, hands‑on implementation, or debugging support for any self‑hosted or third‑party‑hosted open‑weight setups, configurations, environments, or applications.

# Privacy and safety

## Privacy and data

These models are designed to run on infrastructure you control (on-premises or in your cloud or hosting partner). OpenAI does not receive or process the data you send to these self-hosted models unless you explicitly share it with OpenAI, or use one of our managed hosting partners.

## Safety

These models underwent extensive safety training and testing. For more details, see our [model card](https://openai.com/index/gpt-oss-model-card/) and [technical report](https://openai.com/index/gpt-oss-safeguard-technical-report/).

## Reporting content violations

If you believe content generated with gpt‑oss models violates our policies, you can report it through our [Report Content form](https://openai.com/form/report-content/). Please provide as much detail as possible to help our team review your submission.

# FAQ

## Are these models free?

The gpt-oss model weights are free to download and use under the Apache 2.0 license and gpt-oss [usage policy](https://huggingface.co/openai/gpt-oss-120b/blob/main/USAGE_POLICY). However, you are responsible for any costs associated with running them — such as compute, storage, or third-party hosting fees. Pricing for those will depend on your chosen infrastructure or provider.

## Are these models “open source”?

We use the term *open models* or *open-weight* to indicate that the trained weights are publicly available under the permissive Apache 2.0 license and gpt-oss [usage policy](https://huggingface.co/openai/gpt-oss-120b/blob/main/USAGE_POLICY). This means you can download the models, run them on your own infrastructure or with supported hosting frameworks, and customize or fine-tune them.  
  
Open models give developers and organizations greater control and flexibility. You can choose where to host, adapt the models for specific use cases, and benefit from licensing that allows broad use, modification, and redistribution. While the trained weights are open, some surrounding infrastructure or tooling may remain proprietary to their providers.

## Can I access these models through the OpenAI API or ChatGPT?

No. These models are not served in the OpenAI API and do not appear in ChatGPT.

## Can I fine‑tune the models?

Yes. You can fine‑tune using open‑source tools and your preferred infrastructure. We do not offer fine‑tuning through OpenAI APIs for these models.

## Are open‑weight models cheaper than using the API?

Costs vary based on infrastructure, workload, and operational approach. Self‑hosting may be cheaper in some cases, while our [API Platform](https://platform.openai.com/) may be more efficient when factoring in hosting, maintenance, and upgrades.

## What features do these models support?

These models are currently text‑only reasoning models. Common runtimes support streaming, function calling, and structured outputs. Check your runtime’s documentation for exact capabilities.

## How is this different from ModAPI?

This is a highly capable reasoning model that allows you to bring your own policy. It can work in tandem with ModAPI but likely not a replacement for low latency use cases.
