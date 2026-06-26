<!-- source: https://help.openai.com/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt -->

# Data residency and inference residency for ChatGPT

Updated: 2 days ago

Data residency for ChatGPT allows customers to keep their in-scope **customer content** stored at rest in a specific geographic region. Inference residency for ChatGPT allows eligible customers to additionally ensure that **model inference (GPU execution) on their in-scope customer content** happens exclusively in-region for supported locations.  
  
This feature helps organizations in their region meet internal policies or regulatory obligations that dictate where data should reside.

For information about data residency and inference residency for the OpenAI API, please see our separate [API data residency article](https://platform.openai.com/docs/guides/your-data).

---

## Who can use this feature?

Eligible API customers and new ChatGPT Enterprise/Edu customers can choose to have in-scope customer content stored at rest in supported countries.  
  
  
**Inference residency** is available to eligible ChatGPT Enterprise/Edu customers with data residency enabled in supported inference regions (see below).  
  
If you’re unsure whether your organization is eligible, [contact our Sales team](https://openai.com/contact-sales/).

## What regions are supported?

### Data residency (storage at rest)

**Data residency** for ChatGPT is currently available in the following regions:

* Australia
* Canada
* Europe (EEA + Switzerland)
* India
* Japan
* Singapore
* South Korea
* United Arab Emirates
* United Kingdom
* United States

We plan to offer more data residency regions in the future.

### Inference residency (model inference)

**Inference residency** keeps **model inference on in-scope customer content** (GPU execution) in-region for supported locations.  
  
Inference residency for ChatGPT is currently available for the following regions. Note that inference residency requires that data residency be enabled in the same region:

* Europe (EEA + Switzerland)
* United States
* United Arab Emirates

For United Arab Emirates inference residency, **the following limitations apply:**

* Only GPT-5.2 is currently available for ChatGPT. This also applies to API inference in the UAE.
* In ChatGPT, image generation and internal search are not supported.

* Internal search means offline search using OpenAI's internal index.
* External search, such as online web search, remains available unless [Lockdown Mode](https://help.openai.com/articles/20001061) or workspace search controls disable it. If external search is disabled for the workspace, Search is unavailable.

We plan to expand supported inference residency regions over time and will update this article as new regions become available.

## What data is stored in-region under data residency?

When a new ChatGPT workspace is provisioned with data residency, we store \***customer content** in the selected region at rest for the following features:

Backups and replicas of in-scope customer content are also stored in-region.

* **ChatGPT Memory** (stored conversation context)
* **Code Interpreter & Data Analysis** artifacts
* **Conversations** (text, image, voice)
* **Custom GPTs** (and associated prompts/outputs)
* **Files** (e.g., uploaded images, documents)
* **Image Generation** inputs/outputs

Data residency only applies to customer content for the features listed above. If OpenAI releases any new features or modalities, they will not be data residency eligible unless listed above.  
  
\**Customer content refers to what you and your users put into and receive from the services (for example, prompts, files, and model outputs), as defined in your services agreement.*

## What data might be stored outside the region under data residency?

Certain categories of data may be stored outside the chosen data region. This includes (but may not be limited to):

* Data that is stored and processed outside OpenAIs infrastructure through external integrations (e.g., Apps & MCP, Web Search, if enabled)
* Transient or processing steps needed for service functionality
* Workspace metadata

* Workspace name
* Billing information
* User logins

*Some data may be processed or held transiently outside the region and is automatically purged when it’s no longer necessary.*

## What inference happens in-region under inference residency?

When inference residency is enabled for a supported region:

* **GPU inference on customer content stays in-region.**

Model inference (GPU execution) on in-scope customer content is performed on GPUs located in the selected region. This applies to the same categories of customer content listed in **“What data is stored in-region?”** (for example, prompts, files, conversations, and embeddings derived from that content).

* **Non-GPU processing may still occur globally.**

Inference residency does not extend to all CPU-based processing or to system data more broadly. Activities such as authentication, routing, and analytics may still occur outside the selected region.  
  
Inference residency adds an additional **location guarantee for GPU execution on in-scope customer content**; it does not change what is stored in-region or how system data is handled. Inference residency only applies to customer content for the features listed under “What data is stored in-region under data residency?”

## What processing may still occur outside the region under inference residency?

Inference residency adds a **location guarantee for GPU execution on in-scope customer content**, but does not confine all processing to the region.  
  
With inference residency enabled, the following may still occur outside the selected region:

* **CPU-based processing, including but not limited to**

* **External integrations**

* Data sent to third-party services such as apps, MCP servers, web browsing providers, or other external tools. Once data is sent to an external provider, it is handled under that provider’s residency, security, and compliance terms.

## What features are not supported under data or inference residency?

The following features are **not** eligible for data or inference residency:

* Apple Intelligence (including Xcode "Code Intelligence")
* Features that are not Generally Available (i.e. anything still in beta/alpha)
* All apps with sync are supported in the United States, Europe (EEA + Switzerland), and Japan. Google Drive and GitHub apps with sync are also supported in all other currently supported data residency regions.
* Third-Party GPTs
* Codex Web (the Codex app and CLI are supported)
* [ChatGPT Sites](https://developers.openai.com/codex/sites), including deployed Sites, site code, D1/R2 data or file storage, generated site artifacts, and related logs, at launch.

Inference residency follows the same feature availability limitations as data residency, with unsupported features disabled.

## Pricing for data residency

Data residency is **included** at no additional cost for ChatGPT Enterprise and Education plans.

## FAQ

### How is data residency different from inference residency?

* **Data residency (storage at rest)**  
    
  Controls **where in-scope customer content is stored** when it is saved by the service (for example, chat history, files, and GPT configurations).
* **Inference residency (model execution)**  
    
  Controls **where model inference on in-scope customer content runs on GPUs** (for example, generating responses, embedding documents), for supported regions.

Inference residency builds on data residency: you must have data residency enabled in a region to use inference residency in that region.

### What data is in scope for residency?

Residency controls apply to **in-scope customer content** only. They do **not** apply to all user data or system data.  
  
  
**In scope:** Customer content (for example, prompts, files, model outputs) for the features listed under “What data is stored in-region under data residency?”  
  
  
**Out of scope:** Account data, billing details, high-level usage statistics, logs without content, and other metadata used to operate and secure the service

### Does inference residency guarantee that *all* processing stays in-region?

No. Inference residency guarantees that **GPU execution on in-scope customer content** runs in the selected region for supported workloads. Other processing (for example, authentication, routing, indexing, logging without content) may still occur outside the region.  
  
If you require stricter controls, talk to your account team about our roadmap for broader compute residency options which is being actively developed.

### Are there restrictions on GPT sharing?

Yes. Workspaces with data residency enabled will not have the ability to set GPT sharing settings to "Anyone".

Only users within the same data residency region can access a shared GPT.

## Ready to get started?

[**Contact our Sales team**](https://openai.com/contact-sales/) to discuss enabling data residency for your organization.
