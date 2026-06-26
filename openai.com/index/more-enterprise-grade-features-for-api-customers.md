<!-- source: https://openai.com/index/more-enterprise-grade-features-for-api-customers/ -->

April 23, 2024

[Product](/news/product-releases/)

# Introducing more enterprise-grade features for API customers

![More Enterprise Grade Features Hero Image](https://images.ctfassets.net/kftzwdyauwt9/XhRBjRSQJNeoPTK9v6L8W/095cd962c40d1e6c66974591645b3049/DALLE2024-04-0507.40.webp?w=3840&q=90&fm=webp)

We work with many enterprises like [Klarna⁠](https://openai.com/customer-stories/klarna), [Morgan Stanley⁠](https://openai.com/customer-stories/morgan-stanley), [Oscar⁠](https://openai.com/customer-stories/oscar), [Salesforce⁠](https://openai.com/customer-stories/salesforce), and [Wix⁠](https://openai.com/customer-stories/wix) to help them build AI solutions from scratch and safely deploy AI across their organizations and products. We’re deepening our support for enterprises with new features that are useful for both large businesses and any developers who are scaling quickly on our platform.

## Enhanced enterprise-grade security

We’ve introduced Private Link, a new way that customers can ensure direct communication between Azure and OpenAI while minimizing exposure to the open internet. We’ve also released native [Multi-Factor Authentication⁠(opens in a new window)](https://help.openai.com/en/articles/7967234-enabling-multi-factor-authentication-mfa-with-openai) (MFA) to help ensure compliance with increasing access control requirements. These are new additions to our existing stack of [enterprise security features⁠(opens in a new window)](https://trust.openai.com/) including SOC 2 Type II certification, single sign-on (SSO), data encryption at rest using AES-256 and in transit using TLS 1.2, and role-based access controls. We also offer [Business Associate Agreements⁠(opens in a new window)](https://help.openai.com/en/articles/8660679-how-can-i-get-a-business-associate-agreement-baa-with-openai) for healthcare companies that require HIPAA compliance and a zero data retention policy for API customers with a qualifying use case.

## Better administrative control

With our new [Projects⁠(opens in a new window)](https://help.openai.com/en/articles/9186755) feature, organizations will have more granular control and oversight over individual projects in OpenAI. This includes the ability to scope roles and API keys to specific projects, restrict/allow which models to make available, and set usage- and rate-based limits to give access and avoid unexpected overages. Project owners will also have the ability to create service account API keys, which give access to projects without being tied to an individual user.

![More Enterprise Grade Features Product Demo-1](https://images.ctfassets.net/kftzwdyauwt9/2DzJcEhUQrr55NQuqm5sn/86c12f693859ffc8496559ce0ed5f5bb/projects-crop-2.gif?w=3840&q=90&fm=webp)

## Assistants API improvements

We’ve introduced several updates to the Assistants API for more accurate retrieval, flexibility around model behavior and tools used to complete tasks, and better control over costs. These features include:

* Improved retrieval with ‘file\_search’ which can ingest up to 10,000 files per assistant—a 500x increase from the previous file limit of 20. The tool is faster, supports parallel queries through multi-threaded searches, and has enhanced reranking and query rewriting.
* Streaming support for real-time, conversational responses—one of the top requests from developers and enterprises.  
  New ‘vector\_store’ objects in the API so files can be added to a vector store and automatically parsed, chunked, and embedded in preparation for file search. Vector stores can be used across assistants and threads, simplifying file management and billing.
* Control over the maximum number of tokens used per run, plus limits on previous and recent messages used in each run, so you can manage token usage costs.  
  New ‘tool\_choice’ parameter to select a specific tool (like ‘file\_search’, ‘code\_interpreter’, or ‘function’) in a particular run.
* Support for fine-tuned GPT‑3.5 Turbo models in the API (to start, we’ll support fine-tunes of ‘gpt-3.5-turbo-0125’).

![More Enterprise Grade Features Product Demo-2](https://images.ctfassets.net/kftzwdyauwt9/4ciXL2zuaVHJSE9UV3O7ks/9e25f52db2bb3f53931af765ae4f020f/sArea46.gif?w=3840&q=90&fm=webp)

## More options for cost management

To help organizations scale their AI usage without over-extending their budgets, we’ve added two new ways to reduce costs on consistent and asynchronous workloads:

* **Discounted usage on committed throughput:** Customers with a sustained level of tokens per minute (TPM) usage on GPT‑4 or GPT‑4 Turbo can request access to provisioned throughput to get discounts ranging from 10–50% based on the size of the commitment.
* **Reduced costs on asynchronous workloads:** Customers can use our new [Batch API⁠(opens in a new window)](https://platform.openai.com/docs/api-reference/batch)to run non-urgent workloads asynchronously. Batch API requests are priced at 50% off shared prices, offer much higher rate limits, and return results within 24 hours. This is ideal for use cases like model evaluation, offline classification, summarization, and synthetic data generation.

We plan to keep adding new features focused on enterprise-grade security, administrative controls, and cost management. For more information on these launches, visit our [API documentation⁠(opens in a new window)](https://platform.openai.com/docs/introduction) or [get in touch with our team⁠](https://openai.com/contact-sales) to discuss custom solutions for your enterprise.

* [API Platform](/news/?tags=api-platform)
* [2024](/news/?tags=2024)

## Author

## Related research

![A flock of paper planes flying over and through treetops.](//images.ctfassets.net/kftzwdyauwt9/6quMMGifGECzkdDNBAq7D/a3c19eff2e4005aebdb86ca28e53edf3/sora_paper-airplanes.png?w=3840&q=90&fm=webp)

[Video generation models as world simulators

Sora](/index/sora/)

![Sweeping strokes of orange, yellow, and purple in an abstract design](https://images.ctfassets.net/kftzwdyauwt9/ec66425e-99ca-4314-d04b087f8727/de7341b6a5281c2a220b93a737ce19b0/building-an-early-warning-system-for-llm-aided-biological-threat-creation.jpg?w=3840&q=90&fm=webp)

[Building an early warning system for LLM-aided biological threat creation

PublicationJan 31, 2024](/index/building-an-early-warning-system-for-llm-aided-biological-threat-creation/)

![A vibrant, abstract image with radiating streaks of yellow, red, blue, and purple, creating a dramatic, explosive effect reminiscent of a colorful burst of light or energy.](https://images.ctfassets.net/kftzwdyauwt9/1tCf4AONiCc3OkX47FmFy0/f95e25993d309257c631c4e64b699685/weak-to-strong-generalization.jpg?w=3840&q=90&fm=webp)

[Weak-to-strong generalization

SafetyDec 14, 2023](/index/weak-to-strong-generalization/)

![Practices For Governing Agentic AI Systems](https://images.ctfassets.net/kftzwdyauwt9/dfdeca52-d054-4ce9-18d684209ff9/f3a2e6e71ebefb70fca386ff7bbb9d92/practices-for-governing-agentic-ai-systems.jpg?w=3840&q=90&fm=webp)

[Practices for Governing Agentic AI Systems

Safety & Alignment](/index/practices-for-governing-agentic-ai-systems/)
