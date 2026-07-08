<!-- source: https://openai.com/index/introducing-genebench-pro/ -->

June 30, 2026

[Research](/news/research/)[Publication](/research/index/publication/)

# Introducing GeneBench-Pro

A research-level benchmark measuring how AI agents navigate ambiguity and make consequential judgments in computational biology.

[Read the paper(opens in a new window)](https://www.biorxiv.org/content/10.64898/2026.06.29.735386v2)

Scientific data rarely arrive with instructions. Researchers must decide whether a pattern reflects biology or noise, whether the data can support the question being asked, and how each result should change what they do next. AI agents are increasingly capable of executing complex analyses, but real scientific research also depends not simply on recalling facts or following a predefined workflow but also on making these higher-order judgments.

Today, we’re introducing GeneBench-Pro—a challenging, research-level benchmark for testing whether models can handle the kind of judgment-heavy analysis that real-world computational biology requires. It expands on [GeneBench⁠(opens in a new window)](https://www.biorxiv.org/content/10.64898/2026.04.22.720113v1) to cover harder, more realistic tasks across genomics, quantitative biology, and translational medicine, capturing the complexity, iterative nature, and ambiguity of scientific research in computational biology.

To date, there have been few convincing assessments of the system-level judgment calls that make real-world computational research difficult. These include handling ambiguity, revising assumptions, choosing the correct analysis path, and knowing when a result is decision-ready. Because these skills are difficult to formalize, they are also difficult to assess rigorously, even as weaknesses in them increasingly constrain overall AI performance.

![Diagram titled “The benchmark gap in biology” comparing traditional benchmark workflows with end-to-end scientific analysis, showing additional steps such as preprocessing, modeling, diagnostics, and iterative refinement before reaching a scientific conclusion.](https://images.ctfassets.net/kftzwdyauwt9/5P8mBbm691Wa6A18PSRDC4/d850f06a5891d06ecce9efd880008e3e/Diagram1-desktop-light.svg?w=3840&q=90)

GeneBench-Pro is designed to precisely measure these higher-level capabilities. Within GeneBench-Pro, we define “research taste” as the chains of judgment calls that shape an analysis: which questions the data can support, how early diagnostics should change the model or estimand, and when an initial plan needs to be revised. Each GeneBench-Pro problem gives the model a realistic and messy dataset, brief experimental context, and a target estimand tied to a downstream decision. To answer correctly, the model must explore the data, choose an appropriate analytical approach, engage in an iterative process of experimentation, and supply a final answer.

## Dataset construction

In biology, the cost of data generation (e.g., genome sequencing) has fallen dramatically, and [some researchers now argue⁠(opens in a new window)](https://www.nature.com/articles/s41576-022-00551-z) that the limiting factor is no longer sample collection but downstream computation and analysis. GeneBench-Pro is built to assess progress in addressing that bottleneck, with 129 questions covering a broad range of computational biology settings and methods.

## Domain Atlas: 129 problems in 10 domains and 21 sub-domains

Statistical genetics n=17

Population genetics n=21

Quantitative genetics n=17

Regulatory omics n=17

Functional genomics n=9

Proteomics n=7

Clinical, PGx & diagnostics n=26

Cancer genomics n=10

Microbial genomics n=3

Forensic genetics n=2

6Association & correction

6Causal mapping

2Heritability and architecture

3Pedigree, IBD, and phasing

7Selection & mutation

6Admixture & aDNA

8History & genealogies

6Trait architecture and variance

6Family, social, and transmission effects

5Polygenic prediction and genomic selection

8Regulatory QTLs & ASE

5Transcriptome structure

4Spatial and chromatin context

9Functional genomics

7Proteomics and biomarkers

11Clinical variant interpretation & penetrance

8Pharmacogenomics and treatment response

7Prenatal, reproductive, and clinical-risk genetics

10Cancer somatic genomics and liquid biopsy

3Microbial and metagenomic genomics

2Forensic genetics

Use the arrow keys to move between benchmark problems. The selected problem’s details appear below.

Click on a dot above to learn about a benchmark problem.

This atlas provides a preview of the breadth of GeneBench-Pro. Visit the [case studies page](/index/genebench-pro/case-studies/) to explore 10 representative questions in more detail.

GeneBench-Pro is also designed to avoid common benchmark failures. Many long-horizon biology benchmarks construct multi-step questions around messy historical datasets, where there may be no single correct path through the analysis. An agent might choose one defensible cutoff, while another might choose a different but equally defensible option, reflecting the arbitrary choices made by the benchmark creator more than any fundamental differences in model performance. The reverse can also happen: if a problem is too numerically insensitive, an agent can make fundamental errors in an analysis and still produce a passing result.

To avoid these failure modes, each GeneBench-Pro problem is built synthetically: we know the full causal structure and directly simulate the data-generating process. That enables us to tune the complexity of each problem, ensure that reasonable differences in subjective analytical choices still produce accepted numerical results, and verify (through ablation studies) that plausible but incorrect analyses fail. We then audit problem drafts through detailed trace analyses to check for information leakage and unintended solution pathways. This gives us confidence that getting the right answer depends on choosing the correct analytic pathway and not on exploiting a shortcut or matching an arbitrary author preference.

![Diagram titled “Construction and validation of a GeneBench-Pro problem,” showing a workflow from building a runnable task through review, robustness checks, agent testing, expert review, revision, and a finished benchmark problem.](https://images.ctfassets.net/kftzwdyauwt9/7z8Q2z2M1Gp5PiRigY6e25/2625e7b562f0a7fb8d10ff005a4e0387/Diagram2-desktop-light.svg?w=3840&q=90)

We sent 82 of the 129 GeneBench-Pro questions to external domain experts, including graduate students, postdoctoral researchers, industry scientists, and professors. Reviewers assessed each problem’s realism, whether the target answer was identifiable, and whether the methods and estimators were appropriate. Feedback was used to improve problems.

> “The problems I reviewed would have been challenging for a graduate student to complete without iterated feedback from an experienced supervisor. The data contained technical and quality control issues that required thoughtful and reflective data analysis with awareness of potential pitfalls to complete successfully; they were not simply applying some off-the-shelf method to clean and well curated data.”

Alexander Strudwick Young, Assistant Professor in Human Genetics at UCLA

> “Even if current models aren’t able to reliably run independent analyses from beginning to end, ones that perform well on GeneBench-Pro problems clearly would be able to assist researchers in determining correct workflows and exploring data. I could see that greatly improving the pace, thoroughness, and reproducibility of research.”

Jennifer Grundman, PhD Candidate in Human Genetics at UCLA

1 of 2

> “The problems I reviewed would have been challenging for a graduate student to complete without iterated feedback from an experienced supervisor. The data contained technical and quality control issues that required thoughtful and reflective data analysis with awareness of potential pitfalls to complete successfully; they were not simply applying some off-the-shelf method to clean and well curated data.”

Alexander Strudwick Young, Assistant Professor in Human Genetics at UCLA

> “Even if current models aren’t able to reliably run independent analyses from beginning to end, ones that perform well on GeneBench-Pro problems clearly would be able to assist researchers in determining correct workflows and exploring data. I could see that greatly improving the pace, thoroughness, and reproducibility of research.”

Jennifer Grundman, PhD Candidate in Human Genetics at UCLA

* Alexander Strudwick Young, Assistant Professor in Human Genetics at UCLA
* Jennifer Grundman, PhD Candidate in Human Genetics at UCLA

* Alexander Strudwick Young, Assistant Professor in Human Genetics at UCLA
* Jennifer Grundman, PhD Candidate in Human Genetics at UCLA

## Evaluation and grading

Each GeneBench-Pro problem is a self-contained scientific analysis. Agents receive access to an isolated workspace with a short prompt, data files, and a standard bioinformatics stack including Python, scientific computing libraries, and basic genomics packages like PLINK 2.0 (although the problems do not require domain-specific tooling).

## Structural variant-guided tumor therapy benefit-risk decision

A molecular tumor board registry contains trial-eligible advanced solid-tumor cases considered for a TXR1-directed inhibitor. Estimate, for tumors with SV-driven TXR1 target-mediated activation at time zero, the marginal effect of TXR1i versus non-TXR1 systemic therapy on week-16 clinical benefit as if all patients had an assessable week-16 visit. Also estimate the 8-week treatment-limiting toxicity/discontinuation risk under TXR1i in the same target population. Report net clinical utility = benefit risk difference (percentage points) - 0.35 \* toxicity risk (percentage points), and choose therapy\_class\_code 1 if TXR1i has positive net utility and 0 otherwise. 

Use percentage-point units for all non-code quantities. Positive benefit means TXR1i improves week-16 clinical benefit relative to non-TXR1 systemic therapy.

These data came from a real experiment; you will be graded not just on numerical correctness but the quality of analytical reasoning you exhibit; do not attempt to take any shortcuts.

Return your final answer as exactly one JSON object.  
Do not wrap the JSON in markdown.  
Do not add prose before or after the JSON.  
Do not omit any keys shown in the example.  
Return the JSON object in your final answer:

#### JSON

```` ```
1

{

2

"answer": {

3

"therapy_class_code": <int>,

4

"benefit_rd_pp": <float>,

5

"toxicity_dropout_risk_pp": <float>,

6

"net_clinical_utility_pp": <float>

7

},

8

"reasoning": "<description of method and QC>"

9

}
``` ````

Because we control the full data-generation process, we can grade correctness deterministically against known targets, avoiding model-choice variability and verbosity effects found in standard rubric-based evaluation.

Each problem also comes with rich metadata, including the intended analysis structure, attached data files, a detailed multi-page case study, and expert review outcomes. We are fully open-sourcing 10 representative GeneBench-Pro questions on [Hugging Face⁠(opens in a new window)](https://huggingface.co/datasets/ajh-oai/genebench-pro-public-package), with an [interactive web interface](/index/genebench-pro/case-studies/) for browsing them. Finally, we will provide a 50-question subset to [Artificial Analysis⁠(opens in a new window)](https://artificialanalysis.ai/) for independent, third-party benchmarking in the near future.

## Results

Our strongest model, GPT‑5.6 Sol, attains a pass rate of 28.7% at the highest reasoning level (31.5% with Pro mode enabled). That is a sharp increase from when we began building the original GeneBench; at that time, our best frontier model, GPT‑5, scored below 5%. Progress on this benchmark suggests that frontier models are improving quickly, even on less tangible, systems-level scientific reasoning. At the current pace, this benchmark may be saturated by the end of the year.

The results also show the impact of scaling test-time compute. At the lowest reasoning level, GPT‑5.6 Sol only achieves a single-digit passrate. At the highest reasoning level, GPT‑5.6 Sol solves nearly six times as many questions as GPT‑5.2 does while using about two-thirds as many tokens.

Comparisons across model families suggest that GPT models are among the strongest systems at high-level scientific reasoning under quantitative uncertainty. The performance gap between GPT‑5.6, GPT‑5.5 and leading open-source models such as GLM 5.2 is significantly larger than we would expect when extrapolating from [coding benchmarks⁠(opens in a new window)](https://deepswe.datacurve.ai/), indicating that open-source models are more specialized for coding than for broader reasoning ability.

We used frontier GPT models to evaluate and harden problems during development. As such, we suspected GeneBench-Pro might be biased against GPT models relative to other model families. However, competitor models at best matched the performance of the corresponding GPT model at the time of release, and tended to fall short considerably.

These evaluation results—as high as 31.5% on GPT‑5.6 Sol (Pro)—are striking given the difficulty of the GeneBench-Pro questions. In a survey, our reviewers estimated that a typical GeneBench-Pro problem would take a human expert around 20–40 hours to complete. At a conservative $200 per hour, that puts the human labor cost of a single problem in the thousands of dollars. Current AI agents are still too unreliable to replace human experts, but the cost gap is large, with inference costs at only several dollars per problem. That means even partial automation at current capabilities could create meaningful economic and scientific value.

> “The benchmarks are motivated by a diverse range of biological questions, but … the actual challenge comes from exploratory data analysis and reasoning upon these discoveries: identifying patterns and artifacts, and deciding whether the data should be excluded or adjusted. This resembles the messy nature of real biological datasets. Reviewing these evaluations highlights how important clear solver contracts are for agent-based scientific problem solving. Different prompt wording or task specification can greatly affect which analyses appear permissible.”

Cyrillus Tan, Postdoctoral Research Associate at the New York Genome Center

> “I liked [the questions] mostly. They tended to have a mix of: (1) Required knowledge of the subject, such as C>T bias in ancient DNA, (2) Data discrepancies, such as ancestry swaps, (3) A kind of knowledge of the right analytical tools for the job and how to implement them. It seemed like most of the agents failed on (2). They aren't cautious enough about data issues. Maybe that highlights a weakness of current models. And a lot of biological data has irregularities.”

Lex Flagel, Director of Data Science at Gencove

1 of 2

> “The benchmarks are motivated by a diverse range of biological questions, but … the actual challenge comes from exploratory data analysis and reasoning upon these discoveries: identifying patterns and artifacts, and deciding whether the data should be excluded or adjusted. This resembles the messy nature of real biological datasets. Reviewing these evaluations highlights how important clear solver contracts are for agent-based scientific problem solving. Different prompt wording or task specification can greatly affect which analyses appear permissible.”

Cyrillus Tan, Postdoctoral Research Associate at the New York Genome Center

> “I liked [the questions] mostly. They tended to have a mix of: (1) Required knowledge of the subject, such as C>T bias in ancient DNA, (2) Data discrepancies, such as ancestry swaps, (3) A kind of knowledge of the right analytical tools for the job and how to implement them. It seemed like most of the agents failed on (2). They aren't cautious enough about data issues. Maybe that highlights a weakness of current models. And a lot of biological data has irregularities.”

Lex Flagel, Director of Data Science at Gencove

* Cyrillus Tan, Postdoctoral Research Associate at the New York Genome Center
* Lex Flagel, Director of Data Science at Gencove

* Cyrillus Tan, Postdoctoral Research Associate at the New York Genome Center
* Lex Flagel, Director of Data Science at Gencove

Still, the fact that frontier models still solve fewer than a third of these problems shows that there is substantial room for improvement. Models can make partial progress on challenging problems, but they struggle to close the inferential loop. This failure pattern mirrors the contrast between human experts and novices. Experts use their experience to frame the problem and adapt their approach, while novices make observations but struggle to integrate them into the broader context of the problem.

## Problem: Pharmacogenomic time-to-event response with time-varying treatment

Treatment initiation, genotype-specific response, delayed pharmacodynamics, prevalent-user flags, and longitudinal biomarkers jointly determine the causal survival estimand.

## GPT-5.5 pattern

**Handles treatment timing with a conventional Cox outcome model but does not address treatment-confounder feedback.**

> Fit a counting-process Cox model with treatment as a time-varying exposure, effective only after `treat_start`+90 days ... The model included G, treatment×G, baseline severity, age, and sex.

## GPT-5.6 Sol pattern

**Uses a more appropriate causal inference method to properly account for treatment-confounder feedback.**

> Used a new-user marginal structural Cox model: excluded 818 flagged prevalent users, modeled treatment initiation with stabilized inverse-probability weights using baseline covariates and current biomarker, and treated exposure as time-varying with a 90-day efficacy lag.

Achieving near-perfect performance will require evaluations that both reliably measure progress and identify where models still fail. Benchmarks like GeneBench-Pro can help to turn a vague capability deficiency into something we can diagnose and improve.

If agents can reliably automate this class of analysis, they could significantly accelerate scientific discovery. Human genetic evidence is already central to target prioritization and translational follow-up, because mechanisms with genetic support are much more likely to lead to approved treatments.

Meanwhile, sequencing costs have plummeted, and biobank-scale datasets now link molecular, phenotypic, and health-record information at unprecedented breadth. The limiting factor is shifting from data generation to turning the information into actionable insights. Models that can consistently perform analyses now handled by teams of human experts could transform industrial research by accelerating hypothesis triage, target follow-up, and the iteration cycle between data generation and decision-making.

GeneBench-Pro represents an initial effort to evaluate the more abstract skills involved in good scientific judgment possessed by experienced. These skills allow them to intuit and identify the most promising initial analyses, iterate and revise their thinking when data contradict initial assumptions, and arrive at conclusions upon which downstream clinical, academic, or business decisions may depend.

We anticipate that as model capabilities advance, benchmarks that probe model abilities at these higher levels of abstraction will become increasingly useful, beyond those that simply test book knowledge or the ability to execute routine analyses.

![A near-autonomous AI chemist improves a challenging reaction](https://images.ctfassets.net/kftzwdyauwt9/QgPPg4etNE5C4Ao0G94sk/e5f2a50e5de4619d0e0fe8483698718b/molecule-one-art-card.png?w=3840&q=90&fm=webp)

[A near-autonomous AI chemist improves a challenging reaction in medicinal chemistry

ResearchJun 17, 2026](/index/ai-chemist-improves-reaction/)

![LifeSciBench 1x1](https://images.ctfassets.net/kftzwdyauwt9/1iV0eZRf28MZRvIxYY4eLf/4379e20807f5ff44efccf518a97e480a/LifeSciBench_1x1.png?w=3840&q=90&fm=webp)

[Introducing LifeSciBench

ResearchJun 17, 2026](/index/introducing-life-sci-bench/)

![Production Resampling > Art Card](https://images.ctfassets.net/kftzwdyauwt9/6TwSElUf3XVkAiLOvIis8O/de2de5d4b9f94a3dea5403702a4f34ce/Art_Card.png?w=3840&q=90&fm=webp)

[Predicting model behavior before release by simulating deployment

ResearchJun 16, 2026](/index/deployment-simulation/)
