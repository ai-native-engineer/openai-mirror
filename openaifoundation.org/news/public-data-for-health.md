<!-- source: https://openaifoundation.org/news/public-data-for-health -->

# Public Data for Health

By Abhishaike Mahajan and Jacob Trefethen

Our initial grants

In April, [we launched⁠](/news/ai-for-alzheimers) AI for Alzheimer’s, the OpenAI Foundation’s first program in Life Sciences and Curing Diseases. Today, we are introducing our second science program: Public Data for Health.

Our focus in AI for Alzheimer’s is to go after one disease affecting many families where we believe AI can help scientists develop better treatments. Our focus in Public Data for Health is to enable progress across the life sciences, on many diseases, by funding the creation and preservation of high quality scientific datasets made broadly available to researchers.

Scientific data are observations about the world around us, the foundational input to research and discovery. In fields where breakthroughs are verifiable *without* the collection of new data, such as parts of mathematics, AI systems have recently started [contributing⁠](https://www.wsj.com/tech/ai/ai-math-riemann-hypothesis-anthropic-openai-22f98a87) [new⁠](https://openai.com/index/ten-advances-in-mathematics/) [knowledge⁠](https://openai.com/index/navier-stokes-solution/). In biology, meanwhile, AI systems are increasingly able to analyze biological information at scale and recover hidden structure even from incomplete evidence, sometimes with astonishing efficiency.

However, we expect many remaining breakthroughs in preventing and treating disease to come from pairing the intelligence of new models with more observations of the world—in other words, more data.

Some datasets with enormous public value may never be created or shared because no individual institution has enough incentive or capacity to fund them. That makes the support of public data for health a strong fit for the OpenAI Foundation.

## Our initial grants

We are starting by supporting more than **$125 million in grants** across an initial tranche of nonprofits and universities, spanning many layers of data: from molecules, to epidemiology, to regulatory knowledge.

Here are a few examples of the projects we are supporting:

1. [**OpenADMET**⁠](https://openadmet.org/) will create open datasets, benchmarks, and blinded competitions to test whether AI models can be trained to predict how small molecules are absorbed and distributed across the body, to make drug development more predictable and reduce the failure rate of new drugs.

   90% of drug candidates [fail in clinical trials⁠](https://www.science.org/content/blog-post/clinical-failure-rates-over-decades-yikes). That is often due to the difficulty of predicting how they will be absorbed and move around the body—their [“ADMET” properties⁠](https://nigms.nih.gov/biobeat/2023/09/what-happens-to-medicine-in-your-body). Unsolved prediction challenges like this can be a good fit for AI, when paired with high quality data to ground the accuracy of predictions from different models. For example, AlphaFold2 transformed protein structure prediction using data from the [Protein Data Bank⁠](https://www.rcsb.org/), in a competition against other modeling approaches run by [CASP⁠](https://predictioncenter.org/). Protein structure prediction is now integrated into many drug discovery programs that will likely go on to benefit patients.

   To better predict ADMET properties of drug candidates, the OpenADMET team will develop high quality datasets to ground new predictive models, and run open challenges that researchers around the world can enter.

   ![Speakers present OpenADMET’s ADMET prediction challenges to an audience at UCSF.](/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fotoa9rt8o2ha%2F7BsMVHV0yaOuSVOtWuyIOQ%2Fbf70f9f37cde6423852420e6c9728886%2Fpublic-data-for-health-openadmet.jpg&w=3840&q=75)

   *Presentation at a recent OpenADMET event held for participants in ADMET prediction challenges. Credit: Naomi Handly.*

   “Drug discovery is filled with universal problems that no individual company or academic lab interested in curing a specific disease can solve alone,” said James Fraser, PhD, OpenADMET Governing Board member and Professor and Chair of Bioengineering and Therapeutic Sciences at UCSF. “OpenADMET was built to address these problems in an open and machine learning-ready manner. We are excited to be able to build the fundamental layer that will enable AI to greatly accelerate the development of new treatments.”
2. [**CTD Commons**⁠](https://www.ctdcommons.org/) will preserve and publish regulatory knowledge from failed drug development programs so future teams can learn from precedent that is usually locked away, to help uncover effective treatments for patients faster.

   A CTD, or Common Technical Document, is a document that compiles the full journey of an investigational drug—everything from animal toxicology, manufacturing details, and, perhaps most usefully, correspondence with the FDA. Yet only a small fraction of that work appears in published papers.

   CTD Commons will test the possibility of acquiring CTDs from failed or shelved drug programs, and make them openly available for research and analysis, for everyone to use.

   “Every FDA submission represents hard work and sacrifices made by researchers, reviewers, and study participants. Even when these efforts fail, the valuable information they generate should not go to waste,” according to Josh Morrison, leading organizer of CTD Commons and President of 1Day Sooner. “CTD Commons will reduce duplication and cost, and maximize the impact of clinical research.”
3. [**UNC**⁠](https://www.unc.edu/)will establish the Initiative for Generative Immunotherapy, creating public, multimodal data, to help reach a future where cancer patients can get rapid personalized cancer vaccines when they are diagnosed.

   Today’s “neoantigen” cancer vaccines are one of the few medicines designed computationally for each patient, by sequencing a tumor cell to predict which tumor-specific targets are presented on its surface. But that sequencing is itself a proxy of reality, because it is difficult and expensive to measure the cell’s surface targets *directly*, and furthermore to check how strongly a patient’s immune system reacts to each of those proteins.

   UNC will generate those missing links across hundreds of tumors and multiple different types of cancer, creating one of the first training and evaluation datasets in this field, with de-identified public data for researchers around the world to build on.

   “Personalized cancer vaccines are finally starting to show signs of clinical efficacy, but still have gaps which might take decades to fill under the traditional model of therapeutic development. High-quality data can help us close those gaps faster,” said Alex Rubinsteyn, PhD, Assistant Professor of Genetics, UNC School of Medicine. “We are excited to compress this timeline and help make generally effective personalized immunotherapies a reality.”

   ![University of North Carolina research team gathered outdoors.](/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fotoa9rt8o2ha%2F3VVaZ40EC1Bt4yKlT05lpZ%2Ff588f959bca105f533613d9df5307468%2Fpublic-data-for-health-unc.jpg&w=3840&q=75)

   *Lab members working on personalized cancer vaccines at the University of North Carolina. Credit: UNC.*

## Our initial strategy

***We expect this section to be particularly relevant to researchers interested in future OpenAI Foundation grant opportunities.***

There are considerably more scientific data that would be valuable to collect than any one funder can support. So, we wanted to share more here with the research community about the types of data where we believe OpenAI Foundation support can be most useful.

Our starting hypotheses for data to focus on are: ***connected*** data, ***scarce*** data, and ***direct***data. Datasets we fund will usually have one or two of these properties, described in more detail below, and in rare cases will share all three properties.

Across all datasets, we believe making data broadly ***accessible***, while ensuring privacy whenever that relates to patient data,will become increasingly important. This will allow researchers to build on each other’s work, and scientific progress to emerge from unexpected places.

1. ### Connected data: Following biology across multiple steps

   Biology unfolds at different scales, but most life science datasets capture only one part of reality. A cell atlas may measure molecules across thousands of cells, while single-molecule imaging follows one cell only. Both views are valuable, but because such datasets are usually created independently, it can take years of follow-on work to determine how scientific results relate to each other. We want to support individual research teams to move deliberately between these scales and to create rich, connected datasets whose different layers reinforce one another.

   For example, our grant to UCSF will allow the OpenADMET team to measure key molecular properties and interactions for tens of thousands of compounds. The team will then connect this broad profiling to two views of drug transport: experimentally determined structures of transporter proteins with selected molecules bound, and assays measuring how these proteins functionally interact with the molecules. Finally, they will test a subset of these compounds in models of the human blood-brain barrier, comparing those results with in vivo animal measurements.

   This approach to data collection will create an unusually complete account of what determines a drug’s movement through the body—one that enables better prediction from AI models at the level we humans care about.
2. ### Scarce data:Saving what cannot be recreated

   No future AI, however capable, can go back and observe biological events occurring at particular, unique moments in time—such as causes of death and ill-health in countries without reliable vital statistics, or the contents of biological samples from patients at particular moments now past. Biology is filled with these one-way doors, and future modelers may find uses for such evidence that researchers cannot anticipate today. Therefore, we are especially interested in proposals that collect or preserve valuable data before the opportunity disappears, or make existing private datasets that will never be recreated broadly available, while respecting privacy and individual consent.

   For example, our grant to CTD Commons will investigate whether the records of failed drug development programs can be saved before companies shut down and those records disappear. In the short term, these documents may help early-stage drug development teams understand what regulators have required from similar products, rather than learning through expensive trial and error. In the long term, the documents may serve as resources for machine learning systems to discover patterns in why drugs fail or succeed, helping usher in improvements in regulation or trial strategies, allowing patients to benefit from new treatments sooner.
3. ### Direct data: Measuring biological and clinical states closest to what matters

   Biology has spent much of its history measuring what was easy or cheap to measure. For instance: measuring individual cell data over human clinical data, or RNA expression rather than proteins. These proxies have been enormously useful, but they can also become detached from the goals of understanding biology, and of preventing and treating disease. In cases like this, we want to give researchers the resources they need to assemble datasets that measure what matters most. It may also be the case that the necessary instruments to measure “biological truth” do not yet exist, or are prohibitively expensive to use at scale. Within this program, we hope to support both initiatives—new data, and new tools.

   For example, our grant to UNC to establish the Initiative for Generative Immunotherapy will allow the team at UNC Lineberger and UNC Health to produce the human-grounded data necessary to improve the next generation of cancer vaccines. That means measuring tumor cells’ surface proteins *directly*, as well as patients’ T cell responses, rather than “only” sequencing the tumor. This data is expensive to create; by doing it comprehensively this time, and making the results open, we hope all future cancer vaccine efforts will be able to benefit. In particular, if this project is successful, future vaccine candidates will be able to enter human dosing with a stronger set of targets. That should improve their chances of working, and increase what can be learned when they do not.

## Making sure data is accessible to researchers

Finally, across all of our grants, we are ensuring the resulting datasets are as accessible as possible to researchers around the world.

For much of scientific history, testing hypotheses was a primary bottleneck on discovery. There was only so much “intelligence” available to throw at problems—a set number of graduate students and career scientists, who generated data and analyzed that data around a problem. AI’s continuing progress in coding and data analysis breaks that assumption. Analyzing data may become vastly more scalable, with insights emerging from collaborations that are hard to foresee at the time the data are generated.

Our mission is to ensure that artificial general intelligence benefits all of humanity. Scientific data created with our support should be made broadly available, while maintaining individual privacy and consent wherever human data are involved. But accessibility goes beyond just the raw release of the data. We encourage grantees to publish their analyses via preprints, share data regularly rather than only at the end, and, if a grantee’s data is not “connected”, work in tandem with users of the data to assess its utility on biologically valuable problems.

## Iterative learning

This post outlines our initial orientation in Public Data for Health. We are actively updating our views as the science and AI progress, and from conversations with others in the research community.

If you have ideas for Public Data for Health, we encourage you to get in touch at [[email protected]⁠](/cdn-cgi/l/email-protection#2e5d4d474b404d4b6e415e4b404f4748415b404a4f5a47414000415c49). You can subscribe to our newsletter [here⁠](/#sign-up-to-stay-updated), for future updates about our programs and funding.

If you find problems like the ones discussed in this post interesting to think about full-time, we are currently hiring for [four open roles⁠](/careers) on the Life Sciences and Curing Diseases team.

### More news

* [September 21, 2026

  Broadening the benefits of AI, starting with voice→](/news/broadening-the-benefits-of-ai-starting-with-voice)
* [September 10, 2026

  AI forecasting for smallholder farmers→](/news/ai-forecasting-for-smallholder-farmers)
* [September 9, 2026

  Paul Christiano joins OpenAI Foundation Board→](/news/paul-christiano-joins-openai-foundation-board)
* [August 20, 2026

  Come build the OpenAI Foundation→](/news/come-build-the-openai-foundation)
* [August 13, 2026

  AI for Civil Society and Philanthropy→](/news/civil-society-and-philanthropy)

EnglishUnited States
