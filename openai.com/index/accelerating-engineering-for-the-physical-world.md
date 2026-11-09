<!-- source: https://openai.com/index/accelerating-engineering-for-the-physical-world/ -->

November 3, 2026

[Research](/news/research/)[Publication](/research/index/publication/)

# Accelerating engineering for the physical world

Today, we’re sharing advances in how OpenAI models help engineers design, simulate, and build physical products. These capabilities span mechanical and electrical engineering and end-to-end system design, and are already helping our internal teams test ideas and iterate faster.

Across these projects, engineers need to bring together mechanical designs, electronics, software, and manufacturing requirements using specialized tools. We’re teaching models to support that work, from preparing drawings and setting up simulations to coordinating changes across disciplines. Our goal is to give engineers more time to explore ideas and improve designs.

Over the past year, improved frontier model capabilities have helped our internal teams test new ideas and iterate faster, and we are seeing early evidence of these capabilities improving professional workflows in industry as well. We’re working with collaborators to understand where these capabilities can make the biggest difference and what needs to improve. If you’re an engineer, engineering firm, or software vendor involved in the design, simulation, manufacturing, or production of complex physical products, we’d love to [work with you](/form/computer-use-research-collaboration/) to shape this effort around the tools you use and the problems you need to solve.

## Designing a device with Astra

We tested [Astra’s state-of-the-art performance⁠](https://openai.com/index/gpt-6-astra/) in multimodal and computer use workflows by seeing if we can create a device without any direct human edits. To do this, we used GPT‑6 to define the functional requirements and design the enclosure, printed circuit board (PCB), and software integrations needed to create a device users can use to talk to Codex.

* **Aesthetics and design:** Astra developed the look of the device, drawing on our recent [Work Louder⁠(opens in a new window)](https://worklouder.cc/codex-micro) collaboration and references from games and toys.
* **Mechanical design:** Astra designed the [enclosure⁠(opens in a new window)](https://images.ctfassets.net/kftzwdyauwt9/5aP4AhwHhDUmDxisSLcb2X/12114476f73d643b73dffe90b819cc0c/prototype-device-enclosure-diagram.png) and the internal structures that hold the components in place.
* **Electrical design:** Astra selected the electrical components and designed the printed circuit board (PCB), including component placement and connections, to fit within the enclosure.
* **UI/UX and software:** Astra designed the user interface and generated the firmware and software integrations needed to connect the device to Codex.

Two team members designed this test device with Astra in under a week while working on it as a side project. A contract manufacturer built a small batch of prototypes in under a month.

Getting the device ready for manufacturing still required several rounds of review and iteration. Astra did not consistently account for the manufacturer’s production limits, tolerances, or details required for assembly. These gaps are helping us identify what future models need to do better.

## Accelerating OpenAI hardware teams

OpenAI’s hardware and infrastructure teams use Codex and ChatGPT to create and revise computer-aided design (CAD) models, prepare manufacturing drawings, set up simulations, and review designs. This work spans robotics and compute infrastructure. Since February, model usage across our hardware teams, measured in tokens, has grown 23-fold.

1 of 3

> *“Codex has dramatically accelerated how we move from an idea to an engineered part. We’re iterating faster across CAD, converting 3D designs into production-ready 2D drawings, and setting up simulations and FEA with far less manual work.”*

— Grace Lam, Forward Deployed Engineer at OpenAI

> *“As system hardware designers, we use Codex and ChatGPT to organize cross-functional design constraints, explore system architectures, execute across ECAD environments, and conduct thorough design reviews. Today, Codex and ChatGPT are dependable, around-the-clock partners in engineering and project management, with the potential to grow into teams of hardware specialists that can take a board from concept to Gerber out.”*

— Qiong Wang, Member of Technical Staff at OpenAI

> *“In AEC and BIM, a lot of time goes into repetitive modeling, checking information across drawings and specifications, and coordinating changes between disciplines. We're starting to use Codex to automate routine tasks, flag inconsistencies, and turn coordination findings into clear, actionable issues. This frees up time for teams to evaluate design options and constructability, with architects, engineers, and BIM professionals reviewing and validating the results.”*

— Jackie Lee, Member of Infrastructure Staff at OpenAI

* — Grace Lam, Forward Deployed Engineer at OpenAI
* — Qiong Wang, Member of Technical Staff at OpenAI
* — Jackie Lee, Member of Infrastructure Staff at OpenAI

* — Grace Lam, Forward Deployed Engineer at OpenAI
* — Qiong Wang, Member of Technical Staff at OpenAI
* — Jackie Lee, Member of Infrastructure Staff at OpenAI

## Measuring progress on engineering tasks

We’re also measuring progress in newer models on tasks that combine coding with engineering knowledge. BenchCAD 2.0 tests whether models can reconstruct 3D parts and assemblies and identify connections in circuit boards. A newer internal model achieved an average score of 0.875, compared with 0.594 for GPT‑6 Astra at its highest reasoning setting. While the engineering lifecycle includes many other elements beyond design, we view improvements in capability here as early evidence of the ability of AI models to positively impact iteration speed for professional workflows.

## Safely deploying with industry collaborators

We’re working with a small group of industry collaborators to test these capabilities on real engineering problems. Their engineers review model outputs for accuracy and practical use, helping us understand which tasks models can support today and what needs to be improved for safe and reliable use.

We’re expanding our collaboration with [Chip Ganassi Racing](/index/chip-ganassi-racing/) (CGR) to explore how OpenAI models can accelerate engineering and prototyping. Working with its R&D team, we’re testing workflows that turn 3D scans of existing parts into editable CAD models and 2D manufacturing drawings. This is particularly useful when the original design files are unavailable.

CGR engineers review the models and drawings for accuracy and manufacturability. Their feedback helps us identify where models can reduce manual work and where further improvements are needed.

> “*The model has been useful for going from raw scan data to a solid body. I have been working with Codex directly in CAD. The feedback I give the model is directly applied, the manual tweaks can be made directly, and this has become a faster, more hands-off process for me**.*”

— Matthew Ortman, R&D Engineer at Chip Ganassi Racing

We’re also announcing a new research collaboration with Mazda. Our research and Forward Deployed Engineering teams are working with Mazda’s aerodynamics and crash-safety engineers to explore how OpenAI models can help develop and evaluate new vehicle designs.

The work uses simulations of airflow and structural behavior to explore improvements in performance while accounting for styling and cost. We’ll share more progress and results in the coming months.

GPT‑6 Astra helps Mazda’s aerodynamics engineers explore ways to reduce vehicle drag by modeling new nose shapes, simulating airflow, and refining the most promising designs. Agreement for use has been obtained from Mazda Motor Corporation. Any republication or reuse elsewhere is strictly prohibited.

> *“**Does it have to look like that?” Our designers often ask us when we find a shape that improves airflow. By exploring and simulating dozens of variations, Astra in Codex helps us understand which features matter for aerodynamics and where designers have room to explore. That’s why the value of Astra and collaborating with OpenAI goes beyond task automation and shortening development cycles: it is helping us bring together Mazda’s distinctive design and aerodynamic performance without treating either as a compromise.”*

— Akihiro Nakata, Principal Engineer at Mazda

## Help shape AI for engineering and manufacturing

We have been working closely with industry partners and early adopters to push the bounds of what we can do with AI agents in hardware and manufacturing. These early results have shown exciting promise, and we’re now looking for collaborators to accelerate these capability improvements and ensure we deploy these safely into industry.

If you are interested in working with us to shape the training and development of our frontier models by identifying high-value use cases, software tooling, or future opportunities in mechanical engineering, electrical engineering, electromechanical design, mechatronics, or a related field, please fill out [this form](/form/computer-use-research-collaboration/) and we'll be in touch.

## Author

[View all](/news/)

![BioBasicsBench — Cover](https://images.ctfassets.net/kftzwdyauwt9/jNZJCNxCnXJEalE02MRYi/9c7ad4cdb35bae08e5e49eb6a2f65622/biobasicsbench-cover.png?w=3840&q=90&fm=webp)

[Measuring how AI agents handle everyday wet-lab science

PublicationNov 6, 2026](/index/measuring-how-ai-agents-handle-wet-lab-science/)

![A thousand fewer paths to root — Cover](https://images.ctfassets.net/kftzwdyauwt9/6xmxSENf49pAUFzVokN3KG/3206934563d5b072f5a75139d6b26497/a-thousand-fewer-paths-to-root-cover.png?w=3840&q=90&fm=webp)

[A thousand fewer paths to root

SecurityNov 4, 2026](/index/a-thousand-fewer-paths-to-root/)

![LifeVal — Cover](https://images.ctfassets.net/kftzwdyauwt9/7qpi2dSmegt9iF29oioze0/4446550c373728d28b054322caf946ae/lifeval-cover-crayon.png?w=3840&q=90&fm=webp)

[LifeVal

ResearchNov 2, 2026](/index/lifeval/)
