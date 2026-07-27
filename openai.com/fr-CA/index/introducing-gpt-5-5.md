<!-- source: https://openai.com/fr-CA/index/introducing-gpt-5-5/ -->

23 avril 2026

[Produit](/news/product-releases/)[Versions](/research/index/release/)

# Présentation de GPT‑5.5

Une nouvelle catégorie d'intelligence au service d'un travail concret

Chargement…

Partager

*Mise à jour du 24 avril 2026 : GPT‑5.5 et GPT‑5.5 Pro sont désormais disponibles dans l’API.* [*La fiche système*](/index/gpt-5-5-system-card/) *a également été mise à jour afin de décrire les garanties supplémentaires applicables.*

---

Nous lançons GPT‑5.5, notre modèle le plus intelligent et le plus intuitif à utiliser à ce jour, et la prochaine étape vers une nouvelle façon d'accomplir son travail sur ordinateur.

GPT‑5.5 comprend plus rapidement ce que vous essayez de faire et peut prendre davantage en charge lui-même. Il excelle dans l'écriture et le débogage de code, la recherche en ligne, l'analyse de données, la création de documents et de feuilles de calcul, l'utilisation de logiciels et le passage d'un outil à l'autre jusqu'à ce qu'une tâche soit terminée. Au lieu de gérer soigneusement chaque étape, vous pouvez confier à GPT‑5.5 une tâche désordonnée en plusieurs volets et lui faire confiance pour planifier, utiliser des outils, vérifier son travail, naviguer dans l'ambiguïté et persévérer.

Les gains sont particulièrement marqués dans le codage agentif, l'utilisation de l'ordinateur, le travail intellectuel et la recherche scientifique à un stade précoce — des domaines où les progrès dépendent du raisonnement sur l'ensemble du contexte et de la capacité à agir dans la durée. GPT‑5.5 offre ce gain d'intelligence sans compromis sur la vitesse : les modèles plus grands et plus performants sont souvent plus lents à servir, mais GPT‑5.5 égale la latence par token de GPT‑5.4 dans des conditions réelles d'inférence, tout en offrant un niveau d'intelligence nettement supérieur. Il utilise également nettement moins de tokens pour accomplir les mêmes tâches Codex, ce qui le rend à la fois plus efficace et plus performant.

Nous lançons GPT‑5.5 avec notre ensemble de protections les plus robustes à ce jour, conçu pour limiter les abus tout en préservant l'accès aux usages bénéfiques. Nous avons évalué ce modèle au regard de l'ensemble complet de nos cadres de sécurité et de préparation, travaillé avec des équipes rouges internes et externes, ajouté des tests ciblés pour les capacités avancées en cybersécurité et en biologie, et recueilli des retours sur des cas d'usage réels auprès de près de 200 partenaires de confiance bénéficiant d'un accès anticipé avant le lancement.

Dès aujourd'hui, GPT‑5.5 est disponible pour les utilisateurs Plus, Pro, Business et Enterprise dans ChatGPT et Codex, et GPT‑5.5 Pro est disponible pour les utilisateurs Pro, Business et Enterprise dans ChatGPT. Les déploiements d'API nécessitent des mesures de protection variées. Nous collaborons étroitement avec nos partenaires et clients pour répondre aux exigences de sûreté et de sécurité nécessaires à une mise en œuvre à grande échelle. Nous ajouterons GPT‑5.5 et GPT‑5.5 Pro à l'API très prochainement.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | **GPT‑5.5** | **GPT‑5.4** | **GPT‑5.5 Pro** | **GPT‑5.4 Pro** | **Claude Opus 4.7** | **Gemini 3.1 Pro** |
| Terminal-Bench 2.0 | **82,7 %** | 75,1 % | - | - | 69,4 % | 68,5 % |
| Expert-SWE (Interne) | **73,1 %** | 68,5 % | - | - | - | - |
| GDPval (victoires ou ex æquo) | **84,9 %** | 83,0 % | 82,3 % | 82 % | 80,3 % | 67,3 % |
| OSWorld-Verified | **78,7 %** | 75,0 % | - | - | 78,0 % | - |
| Toolathlon | **55,6 %** | 54,6 % | - | - | - | 48,8 % |
| BrowseComp | 84,4 % | 82,7 % | **90,1 %** | 89,3 % | 79,3 % | 85,9 % |
| FrontierMath niveaux 1 à 3 | 51,7 % | 47,6 % | **52,4 %** | 50 % | 43,8 % | 36,9 % |
| FrontierMath niveau 4 | 35,4 % | 27,1 % | **39,6 %** | 38,0 % | 22,9 % | 16,7 % |
| CyberGym | **81,8 %** | 79,0 % | - | - | 73,1 % | - |

## Fonctionnalités du modèle

OpenAI construit l'infrastructure mondiale de l'IA agentive, permettant aux personnes et aux entreprises du monde entier d'accomplir leur travail grâce à l'IA. Au cours de l'année écoulée, nous avons vu l'IA accélérer considérablement l'ingénierie logicielle. Avec GPT‑5.5 dans Codex et ChatGPT, cette même transformation commence à s'étendre à la recherche scientifique et aux tâches plus larges que les gens accomplissent sur ordinateur.

Dans l’ensemble de ces domaines, GPT‑5.5 n’est pas seulement plus intelligent; il est aussi plus efficace dans sa manière de résoudre les problèmes, parvenant souvent à des résultats de meilleure qualité avec moins de tokens et moins de nouvelles tentatives. Sur l’indice de codage d’Artificial Analysis, GPT‑5.5 offre une intelligence de pointe pour moitié moins cher que les modèles concurrents de codage de pointe.

L' [Artificial Analysis Intelligence Index⁠(s'ouvre dans une nouvelle fenêtre)](https://artificialanalysis.ai/methodology/intelligence-benchmarking) est une moyenne pondérée de 10 évaluations réalisées par une partie externe : AA-LCR, AA-Omniscience, CritPt, GDPval-AA, GPQA Diamond, Humanity's Last Exam, IFBench, SciCode, Terminal-Bench Hard, τ²-Bench Telecom.

### Codage agentif

GPT‑5.5 est à ce jour notre modèle de codage agentif le plus performant. Sur **Terminal-Bench 2.0,** qui teste des flux de travail complexes en ligne de commande nécessitant de la planification, de l'itération et une coordination entre outils, il atteint une précision de pointe de 82,7 %. Sur **SWE-Bench Pro**, qui évalue la résolution de demandes GitHub en conditions réelles, il atteint 58,6 %, en résolvant davantage de tâches de bout en bout en une seule passe que les modèles précédents. Sur **Expert-SWE**, notre évaluation interne de pointe pour les tâches de programmation à long horizon, dont le temps médian d'exécution estimé pour un humain est de 20 heures, GPT‑5.5 surpasse également GPT‑5.4.

Sur l'ensemble des trois évaluations, GPT‑5.5 améliore celles des scores de GPT‑5.4 tout en utilisant moins de tokens.

Les capacités en programmation du modèle se manifestent particulièrement clairement dans Codex, où il peut prendre en charge des tâches d'ingénierie allant de la mise en œuvre et des re-factorisations au débogage, aux tests et à la validation. Les premiers tests suggèrent que GPT‑5.5 maîtrise mieux les comportements dont dépend réellement le travail d'ingénierie, comme maintenir le contexte à l'échelle de systèmes complexes, le raisonnement face à des défaillances ambiguës, vérifier ses hypothèses à l'aide d'outils et répercuter des modifications dans l'ensemble de la base de code environnante.

La trajectoire rendue utilise les données vectorielles de NASA/JPL Horizons pour Orion, la Lune et le Soleil, avec une mise à l'échelle de l'affichage appliquée pour améliorer la lisibilité.

**Invite :** [attached image] Implement this as a new app using webgl and vite using real data from the Artemis II mission. Make sure to test the app thoroughly until it is fully functional and looks like the app in the picture. Pay close attention to the rendering of the planets and fly paths. I want to be able to interact with the 3D rendering. Ensure it has realistic orbital mechanics.

Au-delà des évaluations, les premiers testeurs ont indiqué que GPT‑5.5 montre une plus grande capacité à comprendre la structure d'un système : pourquoi quelque chose échoue, où la correction doit être apportée et quels autres éléments de la base de code seraient affectés.

![alternatif](https://images.ctfassets.net/kftzwdyauwt9/5A8f5mO7aKrwLH5ClDV0si/e49a0a3c56f63d9998dd338ce16d0dd6/Blog1.png?w=3840&q=90&fm=webp)

« Le premier modèle de codage que j'ai utilisé à avoir une véritable clarté conceptuelle. »

![alternatif](https://images.ctfassets.net/kftzwdyauwt9/6T4xNx8jzQOmohTbNFpbt3/e85b69bdc6d86366e17d48739be4232e/Blog1.png?w=3840&q=90&fm=webp)

« Le premier modèle de codage que j'ai utilisé à avoir une véritable clarté conceptuelle. »

Dan Shipper, fondateur et PDG de Every, a décrit GPT‑5.5 comme « le premier modèle de codage que j'ai utilisé à faire preuve d'une réelle clarté conceptuelle ».

Après avoir lancé une application, il a passé des jours à déboguer un problème post-lancement avant de faire appel à l’un de ses meilleurs ingénieurs pour réécrire une partie du système. Pour tester GPT‑5.5, il a en quelque sorte remonté le temps : le modèle pouvait-il analyser l’état défaillant et proposer le même type de réécriture que celle finalement retenue par l’ingénieur? GPT‑5.4 ne le pouvait pas. GPT‑5.5 le pouvait.

![alternatif](https://images.ctfassets.net/kftzwdyauwt9/1eFs7ss7lMxUlZlbCCd6mC/d62c48414621c37d251564b6880dccc0/Blog2.png?w=3840&q=90&fm=webp)

« J'ai vraiment l'impression de travailler avec une intelligence supérieure, et il y a presque une forme de respect. »

![alternatif](https://images.ctfassets.net/kftzwdyauwt9/72r6bw8GUc0qCr8fXs4Fnu/8fd4014193a371af2db5b30026ddc540/Blog2.png?w=3840&q=90&fm=webp)

« J'ai vraiment l'impression de travailler avec une intelligence supérieure, et il y a presque une forme de respect. »

Pietro Schirano, CEO de MagicPath, a constaté un changement de cap similaire lorsque GPT‑5.5 a fusionné une branche comportant des centaines de modifications du frontend et de refactor dans une branche principale qui avait elle aussi considérablement changé, en résolvant le travail en une seule étape en une vingtaine de minutes.

Des ingénieurs expérimentés ayant testé le modèle ont déclaré que GPT‑5.5 surpassait nettement GPT‑5.4 et Claude Opus 4.7 en termes de raisonnement et d'autonomie, détectant les problèmes à l'avance et anticipant les besoins en tests et révisions sans y être explicitement invité. Dans un cas, un ingénieur a demandé de réorganiser l'architecture d'un système de commentaires dans un éditeur collaboratif Markdown et, à son retour, il a trouvé une pile de 12 diffs presque terminée. D'autres ont déclaré avoir eu besoin d'étonnamment peu de corrections de mise en œuvre et avoir davantage confiance dans les plans de GPT‑5.5 par rapport à ceux de GPT‑5.4.

Un ingénieur de NVIDIA qui avait eu un accès anticipé au modèle est allé jusqu’à dire : « Perdre l’accès à GPT‑5.5, c’est comme perdre un membre. »

> « GPT-5.5 est nettement plus intelligent et plus persistant que GPT-5.4, avec des performances de codage renforcées et une utilisation plus fiable des outils. Il reste concentré sur la tâche beaucoup plus longtemps, sans s'arrêter prématurément, ce qui est particulièrement important pour les travaux complexes et de longue durée que nos utilisateurs confient à Cursor. »

— Michael Truell, cofondateur et PDG de Cursor

### Travail intellectuel

Les mêmes atouts qui rendent GPT‑5.5 excellent pour le codage en font aussi un outil puissant pour le travail quotidien sur ordinateur. Parce que le modèle comprend mieux l'intention, il peut parcourir plus naturellement l'ensemble du cycle du travail de la connaissance : trouver des informations, comprendre ce qui compte, utiliser des outils, vérifier le résultat et transformer une matière brute en quelque chose d'utile.

Dans Codex, GPT‑5.5 est plus performant que GPT‑5.4 pour générer des documents, des feuilles de calcul et des présentations. Les testeurs alpha ont indiqué qu'il surpassait les modèles précédents pour des tâches telles que la recherche opérationnelle, la modélisation sur feuille de calcul et la transformation de données métier brutes en plans d'action. Combiné aux capacités d'utilisation d'un ordinateur de Codex, GPT‑5.5 nous rapproche de l'impression que le modèle peut réellement utiliser l'ordinateur avec vous  : voir ce qui s'affiche à l'écran, cliquer, saisir du texte, naviguer dans les interfaces et passer d'un outil à l'autre avec précision.

Les équipes d'OpenAI utilisent déjà ces atouts dans des flux de travail concrets. Aujourd'hui, plus de 85 % de l'entreprise utilise Codex chaque semaine dans différentes fonctions, notamment l'ingénierie logicielle, la finance, la communication, le marketing, la science des données et la gestion de produit. Au sein de Comms, l'équipe a utilisé GPT‑5.5 dans Codex pour analyser six mois de données sur les demandes d'intervention, élaborer un cadre d'évaluation et de gestion des risques, et valider un agent Slack automatisé afin que les demandes à faible risque puissent être traitées automatiquement, tandis que les demandes à risque plus élevé continuent d'être soumises à une vérification humaine. Dans la finance, l'équipe a utilisé Codex pour examiner 24,771 formulaires fiscaux K-1 totalisant 71,637 pages, grâce à un flux de travail excluant les informations personnelles, ce qui a aidé l'équipe à réaliser cette tâche avec deux semaines d'avance par rapport à l'année précédente. Au sein de l'équipe chargée de la stratégie de mise sur le marché, un employé a automatisé la génération de rapports d'activité hebdomadaires, économisant 5 à 10 heures par semaine.

Dans ChatGPT, **GPT‑5.5 Thinking** offre une aide plus rapide face aux problèmes les plus complexes, avec des réponses plus pertinentes et plus concises pour vous aider à avancer plus efficacement dans les tâches complexes. Il excelle dans les tâches professionnelles comme le codage, la recherche, la synthèse et l'analyse d'informations, ainsi que les tâches impliquant de nombreux documents, en particulier avec l'utilisation de plugiciels.

Avec **GPT‑5.5 Pro**, les premiers testeurs constatent une nette amélioration de la complexité et de la qualité des tâches que ChatGPT peut prendre en charge, ainsi que des améliorations de latence qui le rendent bien plus pratique pour les tâches exigeantes. Par rapport à GPT‑5.4 Pro, les testeurs ont constaté que les réponses de GPT‑5.5 Pro étaient nettement plus complètes, mieux structurées, plus précises, plus pertinentes et plus utiles, avec des performances particulièrement solides dans les domaines du commerce, du droit, de l'éducation et de la science des données.

GPT‑5.5 atteint des performances de pointe sur plusieurs benchmarks qui reflètent ce type de travail. Sur [GDPval⁠⁠](/fr-CA/index/gdpval/), qui évalue la capacité des agents à produire un travail intellectuel bien défini dans 44 professions, GPT‑5.5 obtient un score de 84,9 %. Sur **OSWorld-Verified**, qui mesure si un modèle peut utiliser seul de véritables environnements informatiques, il atteint 78,7 %. Et sur **Tau2-bench Telecom**, qui teste des flux de travail complexes du service client, il atteint 98,0 % sans ajustement de l’invite. GPT‑5.5 affiche également des performances élevées sur d’autres benchmarks de travail de la connaissance : 60 % sur **FinanceAgent**, 88,5 % sur des **tâches internes de modélisation en banque d’investissement**, et 54,1 % sur **OfficeQA Pro**.

Tau2-bench Telecom a été exécuté sans ajustement de l'invite (et avec GPT‑4.1 comme modèle utilisateur). GPT‑5.5 comprend mieux l'intention de la tâche et est plus économe en tokens que ses prédécesseurs.

> « GPT-5.5 offre les performances soutenues requises pour les tâches fortement axées sur l'exécution. Conçu et déployé sur des systèmes NVIDIA GB200 NVL72, le modèle permet à nos équipes de livrer des fonctionnalités de bout en bout à partir d'invites en langage naturel, de réduire le temps de débogage de plusieurs jours à quelques heures et de transformer des semaines d'expérimentation en avancées obtenues du jour au lendemain dans des bases de code complexes. C'est plus qu'un simple codage plus rapide : c'est une nouvelle façon de travailler qui aide les gens à travailler à un rythme fondamentalement différent. »

— Justin Boitano, vice-président de l'IA d'entreprise chez NVIDIA

### Recherche scientifique

GPT‑5.5 affiche également des progrès dans les flux de travail de recherche scientifique et technique, qui nécessitent plus que de répondre à une question difficile. Les chercheurs doivent explorer une idée, rassembler des preuves, tester des hypothèses, interpréter les résultats et décider de ce qu'ils vont essayer ensuite. GPT‑5.5 parvient mieux à persister au fil de cette boucle que les autres modèles.

Fait notable, GPT‑5.5 montre une nette amélioration par rapport à GPT‑5.4 sur [**GeneBench**⁠(s'ouvre dans une nouvelle fenêtre)](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf), une nouvelle évaluation axée sur l’analyse scientifique de données en plusieurs étapes en génétique et en biologie quantitative. Ces problèmes exigent que les modèles raisonnent sur des données potentiellement ambiguës ou erronées avec un minimum de supervision, surmontent des obstacles réalistes tels que des facteurs de confusion cachés ou des échecs du contrôle qualité, et mettent en œuvre et interprètent correctement des méthodes statistiques modernes. Les performances du modèle sont remarquables compte tenu du fait que les tâches considérées ici correspondent souvent à des projets de plusieurs jours pour des experts scientifiques.

De même, sur [BixBench⁠(s'ouvre dans une nouvelle fenêtre)](https://arxiv.org/abs/2503.00096), un benchmark conçu autour de cas concrets en bio-informatique et en analyse de données, GPT‑5.5 a obtenu les meilleures performances parmi les modèles dont les résultats sont publiés. Les capacités scientifiques du modèle sont désormais suffisamment développées pour accélérer de manière significative les progrès de la recherche biomédicale de pointe en tant que véritable coscientifique.

Dans un autre exemple, une version interne de GPT‑5.5 dotée d’un banc d’essai personnalisé a aidé à découvrir une [nouvelle démonstration⁠(s'ouvre dans une nouvelle fenêtre)](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/Ramsey.pdf) concernant les nombres de Ramsey, l’un des objets centraux de la combinatoire. La combinatoire étudie la manière dont les objets discrets s’agencent : graphes, réseaux, ensembles et motifs. Les nombres de Ramsey s’intéressent, en gros, à la taille que doit avoir un réseau pour qu’une forme d’ordre apparaisse nécessairement. Les résultats dans ce domaine sont rares et souvent difficiles à obtenir sur le plan technique. Ici, GPT‑5.5 a trouvé une preuve d’un fait asymptotique établi de longue date concernant les nombres de Ramsey hors diagonale, ensuite vérifiée dans Lean. Le résultat est un exemple concret de GPT‑5.5 contribuant non seulement par du code ou des explications, mais aussi par un argument mathématique surprenant et utile dans un domaine central de la recherche.

Les premiers testeurs ont utilisé GPT‑5.5 Pro dans ChatGPT moins comme un moteur de réponses en une seule étape et davantage comme un partenaire de recherche : en critiquant des manuscrits au fil de plusieurs passes, en mettant à l'épreuve des arguments techniques, en proposant des analyses et en travaillant avec du code, des notes et le contexte de PDF. Le point commun, c'est que GPT‑5.5 aide les chercheurs à passer de la question à l'expérience, puis aux résultats.

![alternatif](https://images.ctfassets.net/kftzwdyauwt9/3tvjV3IAWoNm6kBwh6XjQB/5d2c1ca28e25d5ee015fd220b919d5b3/Blog3.png?w=3840&q=90&fm=webp)

![alternatif](https://images.ctfassets.net/kftzwdyauwt9/2xO4DFtGj9mgmlKpR2EgBR/c8102d3256edfb11b21a8297d0891424/Blog3.png?w=3840&q=90&fm=webp)

Derya Unutmaz, professeur d'immunologie et chercheur au Jackson Laboratory for Genomic Medicine, a utilisé GPT‑5.5 Pro pour analyser un jeu de données d'expression génique comprenant 62 échantillons et près de 28 000 gènes, générant un rapport de recherche détaillé qui non seulement résumait les résultats, mais faisait également ressortir des questions clés et des enseignements importants — un travail qui, selon lui, aurait pris des mois à son équipe.

![alternatif](https://images.ctfassets.net/kftzwdyauwt9/5kx7uMF0Iq0fRIluO7JgN1/1e899be5fe72247475ecd8dc9a3a0dd4/Blog5.png?w=3840&q=90&fm=webp)

![alternatif](https://images.ctfassets.net/kftzwdyauwt9/2cUS16rFVukXEvhllfm5A4/ace05408b550de68da57ff5fce5ede90/Blog5.png?w=3840&q=90&fm=webp)

Bartosz Naskręcki, professeur adjoint de mathématiques à l'université Adam Mickiewicz de Poznań, en Pologne, a utilisé GPT‑5.5 dans Codex pour créer une application de géométrie algébrique à partir d'une seule invite en 11 minutes, visualisant l'intersection de surfaces quadratiques et convertissant la courbe résultante en modèle de Weierstrass.

Il a ensuite enrichi l'application avec une visualisation des singularités plus stable et des coefficients exacts, réutilisables dans des travaux ultérieurs. Pour lui, le changement le plus important est que Codex peut désormais aider à mettre en œuvre des flux de travail personnalisés de visualisation mathématique et de calcul formel, qui nécessitaient auparavant des outils dédiés. Ensemble, ces exemples montrent comment GPT‑5.5 transforme l'intention des experts en outils de recherche et en analyses fonctionnelles.

![“”](https://images.ctfassets.net/kftzwdyauwt9/1WiRj8XUEoqruFEKNQJPRr/4063977e99833d7129b6a238b4d3d876/Bartosz_Visual.png?w=3840&q=90&fm=webp)

[Crédit : Bartosz Naskręcki⁠(s'ouvre dans une nouvelle fenêtre)](https://bnaskrecki.faculty.wmi.amu.edu.pl/quadr/)

**Invite :**# intersection de surfaces en géométrie algébrique

Make an app which draws two quadratic surfaces and colors in red the intersection curve. Use computational Riemann-Roch theorem to convert this into Weierstrass curve.

## Fenêtre principale

Two tinted surfaces with a slightly transparent shading, high quality rendering intersect along a red colored algebraic curve

Rotation with mouses in both directions, full pinch mechanism for zoom, haptic press to show the little menu with sliders for changing the coefficients of each surface; detection via Z-buffor level

## Fenêtre côté droit

Short Weierstrass equation (over Q or quadratic field extension) computed on the go via effective Riemann-Roch theorem formulas

## Ambient mode where all the controls are hidden and the user can admire the beauty of the shapes

## Spécs

App is running in the browser, light-weight implementation with full stack newest libraries, portable, deployable

## Documents

dépôt Git, journal, plan (fichiers Markdown)

> « C'est incroyablement stimulant d'utiliser le nouveau modèle GPT-5.5 d'OpenAI dans notre environnement de test, de le voir analyser d'immenses jeux de données biochimiques pour prédire les effets des médicaments chez l'humain, puis constater des gains de précision significatifs sur nos évaluations les plus difficiles en découverte de médicaments. Si OpenAI continue sur cette lancée, les fondements de la découverte de médicaments changeront d'ici la fin de l'année. »

— Brandon White, cofondateur et PDG d'Axiom Bio

## Efficacité de l'inférence de nouvelle génération

Faire fonctionner GPT‑5.5 avec la latence de GPT‑5.4 a nécessité de repenser l'inférence comme un système intégré, et non comme un ensemble d'optimisations isolées. GPT‑5.5 a été co-conçu, entraîné et déployé sur des systèmes NVIDIA GB200 et GB300 NVL72. Codex et GPT‑5.5 ont joué un rôle déterminant dans l'atteinte de nos objectifs de performance. Codex a aidé l'équipe à avancer plus vite, du concept à une mise en œuvre mesurable par des benchmarks, en esquissant des approches, en organisant des expérimentations et en aidant à identifier les optimisations méritant un investissement plus poussé. GPT‑5.5 a contribué à identifier et à mettre en œuvre des améliorations clés dans l'architecture elle-même. En termes simples, le modèle a contribué à améliorer l'infrastructure qui le prend en charge.

L'une de ces améliorations concernait l'équilibrage de charge et les heuristiques de partitionnement. Avant GPT‑5.5, nous divisions les requêtes sur un accélérateur en un nombre fixe de segments pour équilibrer la charge de travail entre les cœurs de calcul, permettant ainsi aux requêtes volumineuses et aux plus petites de s'exécuter sur le même GPU. Cependant, un nombre prédéfini de segments statiques n'est pas optimal pour tous les profils de trafic. Pour mieux exploiter les GPU, Codex a analysé plusieurs semaines de modèles de trafic en production et a conçu des algorithmes heuristiques personnalisés pour répartir et équilibrer la charge de travail de manière optimale. Cet effort a eu un impact considérable, augmentant la vitesse de génération des tokens de plus de 20 %.

## Faire progresser la cybersécurité pour la sécurité de tous

Préparer le monde à des modèles très performants pour détecter et corriger les vulnérabilités de sécurité est un effort collectif et exigera que l’ensemble de l’écosystème travaille dur pour renforcer sa résilience, grâce à un accès démocratisé aux modèles et à un déploiement itératif pour la [prochaine ère de la cyberdéfense⁠](https://openai.com/index/scaling-trusted-access-for-cyber-defense/).

Les modèles de pointe deviennent de plus en plus performants en cybersécurité. Ces capacités seront largement diffusées, et nous pensons que la meilleure voie à suivre consiste à veiller à ce qu'elles puissent être mises à profit pour accélérer la cyberdéfense et renforcer l'écosystème.

GPT‑5.5 constitue une étape importante vers une IA capable de relever certains des défis les plus difficiles au monde, comme la cybersécurité. Avec GPT‑5.2 en décembre, nous avons déployé de manière proactive les [mesures de protection nécessaires⁠](https://openai.com/index/strengthening-cyber-resilience/) pour limiter les usages abusifs en cybersécurité. Avec GPT‑5.5, nous introduisons des classificateurs plus stricts pour les risques potentiels en cybersécurité, que certains utilisateurs pourront trouver contraignants dans un premier temps, le temps de les affiner.

Nous avons depuis des années identifié la cybersécurité comme une catégorie dans notre [cadre de préparation⁠(s'ouvre dans une nouvelle fenêtre)](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf), à mesure que nos modèles se sont progressivement améliorés et que nous avons développé et calibré de manière itérative des mesures d’atténuation, afin de pouvoir déployer de manière responsable des modèles dotés de capacités significatives en cybersécurité.

* **Nous déployons des mesures de protection de premier plan pour ce niveau de capacités en cybersécurité.** Nous avons d’abord introduit des [mesures de protection spécifiques à la cybersécurité avec GPT‑5.2⁠(s'ouvre dans une nouvelle fenêtre)](https://deploymentsafety.openai.com/gpt-5-2/deception) l’année dernière, que nous avons continué à tester, à affiner et à développer dans les déploiements ultérieurs. Pour GPT‑5.5, nous avons conçu des contrôles plus stricts autour des activités à plus haut risque, des demandes sensibles en cybersécurité, et ajouté des protections contre les usages abusifs répétés. Un large accès est rendu possible grâce à nos investissements dans la sécurité des modèles, l’utilisation authentifiée et la surveillance des utilisations non autorisées. Nous travaillons avec des experts externes depuis des mois afin de développer, tester et améliorer continuellement la fiabilité de ces garde-fous. Avec GPT‑5.5, nous veillons à ce que les développeurs puissent sécuriser leur code en toute simplicité, tout en mettant en place des contrôles plus stricts sur les flux de travail de cybersécurité les plus susceptibles de causer des dommages s’ils sont exploités par des acteurs malveillants.
* **Nous élargissons l’accès afin d’accélérer la cyberdéfense à tous les niveaux.** Nous mettons nos modèles plus permissifs en matière de cybersécurité à disposition via [Trusted Access for Cyber⁠](https://openai.com/index/scaling-trusted-access-for-cyber-defense/), en commençant par Codex, qui inclut un accès élargi aux capacités avancées en cybersécurité de GPT‑5.5 avec moins de restrictions pour les utilisateurs vérifiés répondant à certains [critères de confiance⁠(s'ouvre dans une nouvelle fenêtre)](https://developers.openai.com/codex/concepts/cyber-safety) dès le lancement. Les organisations chargées de [défendre les infrastructures critiques⁠](https://openai.com/index/accelerating-cyber-defense-ecosystem/) peuvent demander à accéder à des modèles permissifs en matière de cybersécurité comme GPT‑5.4‑Cyber, à condition de respecter des exigences de sécurité strictes pour utiliser ces modèles afin de sécuriser leurs systèmes internes. Cela permet à un large éventail de défenseurs vérifiés de disposer d’outils plus performants pour mener des activités de sécurité légitimes avec moins de frictions inutiles, afin de démocratiser l’accès à des capacités défensives essentielles. Les utilisateurs peuvent faire une demande d’accès de confiance sur [chatgpt.com/cyber⁠(s'ouvre dans une nouvelle fenêtre)](http://chatgpt.com/cyber) afin de réduire les refus inutiles lorsqu’ils utilisent GPT‑5.5 pour des activités défensives vérifiées.
* **Nous collaborons avec des partenaires gouvernementaux pour contribuer à protéger les infrastructures critiques au bénéfice du public.** Ensemble, nous explorons comment l'IA avancée peut soutenir le travail de défense de responsables de confiance chargés de systèmes dont les citoyens dépendent, qu'il s'agisse des systèmes numériques qui protègent d'importantes données fiscales, du réseau électrique ou de l'approvisionnement en eau des collectivités locales.

Nous considérons les capacités biologiques/chimiques et de cybersécurité de GPT‑5.5 comme étant de niveau High dans le cadre de notre [cadre de préparation⁠(s'ouvre dans une nouvelle fenêtre)](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf). Bien que GPT‑5.5 n’ait pas atteint le niveau de capacité critique en cybersécurité, nos évaluations et nos tests ont montré que ses capacités en cybersécurité marquent une progression par rapport à GPT‑5.4.

En outre, GPT‑5.5 a suivi l’intégralité de notre processus de sécurité et de gouvernance avant son lancement, y compris des évaluations de préparation, des tests spécifiques à certains domaines, de nouvelles évaluations ciblées pour les capacités avancées en biologie et en cybersécurité, ainsi que des tests approfondis menés avec des experts externes. Nous partageons davantage de détails dans la [fiche système de GPT‑5.5⁠(s'ouvre dans une nouvelle fenêtre)](https://deploymentsafety.openai.com/gpt-5-5).

Ce travail reflète notre approche plus large de la résilience de l'IA, qui, selon nous, est nécessaire à mesure que les capacités des modèles progressent. Nous voulons qu'une IA puissante soit mise à la disposition des personnes qui l'utilisent pour défendre les systèmes, les institutions et le public. La voie viable consiste en un accès de confiance, des garanties solides qui évoluent avec les capacités, et la capacité opérationnelle à détecter les utilisations abusives graves et à y répondre.

## Disponibilité et tarification

Dès aujourd'hui, GPT‑5.5 est disponible pour les utilisateurs Plus, Pro, Business et Enterprise dans ChatGPT et Codex, et GPT‑5.5 Pro est disponible pour les utilisateurs Pro, Business et Enterprise dans ChatGPT. Nous ajouterons GPT‑5.5 et GPT‑5.5 Pro à l'API très prochainement.

Dans ChatGPT, GPT‑5.5 Thinking est disponible pour les utilisateurs de Plus, Pro, Business et Enterprise. GPT‑5.5 Pro, conçu pour répondre à des questions encore plus difficiles et effectuer un travail de plus grande précision, est disponible pour les utilisateurs Pro, Business et Enterprise.

Dans Codex, GPT‑5.5 est disponible avec les forfaits Plus, Pro, Business, Enterprise, Edu et Go, avec une fenêtre de contexte de 400K. GPT‑5.5 est également disponible en mode Fast, générant des tokens 1,5 fois plus rapidement pour un coût 2,5 fois plus élevé.

Pour les développeurs d’API, gpt-5.5 sera bientôt disponible dans les API Responses et API Chat Completions, au tarif de 5 $ par million de tokens d’entrée et 30 $ par million de tokens de sortie, avec une fenêtre de contexte de 1M. Les tarifs Batch et Flex sont disponibles à la moitié du tarif standard de l’API, tandis que le traitement prioritaire est disponible à 2,5 fois le tarif standard de l’API. Nous lancerons également gpt-5.5-pro dans l'API pour une précision encore supérieure, au tarif de 30 dollars par million de tokens en entrée et de 180 dollars par million de tokens en sortie. Consultez la [page de tarification⁠](/fr-CA/api/pricing/) pour plus de détails.

Alors que GPT‑5.5 est facturé plus cher que GPT‑5.4, il est à la fois plus intelligent et bien plus efficace en termes de tokens. Dans Codex, nous avons soigneusement optimisé l'expérience afin que GPT‑5.5 offre de meilleurs résultats avec moins de tokens que GPT‑5.4 pour la plupart des utilisateurs, tout en continuant à offrir une utilisation généreuse selon les niveaux d'abonnement.

## Évaluations

### Codage

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Évaluation** | **GPT‑5.5** | **GPT‑5.4** | **GPT‑5.5 Pro** | **GPT‑5.4 Pro** | **Claude Opus 4.7** | **Gemini 3.1 Pro** |
| SWE-Bench Pro (Public) \* | 58,6 % | 57,7 % | - | - | 64,3 % | 54,2 % |
| Terminal-Bench 2.0 | 82,7 % | 75,1 % | - | - | 69,4 % | 68,5 % |
| Expert-SWE (Interne) | 73,1 % | 68,5 % | - | - | - | - |

\*Les laboratoires ont relevé des [signes de mémorisation⁠(s'ouvre dans une nouvelle fenêtre)](https://www.anthropic.com/news/claude-opus-4-7) sur cette évaluation

### Professionnel

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Évaluation** | **GPT‑5.5** | **GPT‑5.4** | **GPT‑5.5 Pro** | **GPT‑5.4 Pro** | **Claude** **Opus 4.7** | **Gemini 3.1 Pro** |
| GDPval (victoires ou ex æquo) | 84,9 % | 83,0 % | 82,3 % | 82 % | 80,3 % | 67,3 % |
| FinanceAgent v1.1 | 60,0 % | 56 % | - | 61,5 % | 64,4 % | 59,7 % |
| Tâches de modélisation en banque d’investissement (interne) | 88,5 % | 87,3 % | 88,6 % | 83,6 % | - | - |
| OfficeQA Pro | 54,1 % | 53,2 % | - | - | 43,6 % | 18,1 % |

### Utilisation d’ordinateur et vision

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Évaluation** | **GPT‑5.5** | **GPT‑5.4** | **GPT‑5.5 Pro** | **GPT‑5.4 Pro** | **Claude** **Opus 4.7** | **Gemini 3.1 Pro** |
| OSWorld-Verified | 78,7 % | 75,0 % | - | - | 78,0 % | - |
| MMMU Pro (sans outils) | 81,2 % | 81,2 % | - | - | - | 80,5 % |
| MMMU Pro (avec outils) | 83,2 % | 82,1 % | - | - | - | - |

### Utilisation d’outils

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Évaluation** | **GPT‑5.5** | **GPT‑5.4** | **GPT‑5.5 Pro** | **GPT‑5.4 Pro** | **Claude** **Opus 4.7** | **Gemini 3.1 Pro** |
| BrowseComp | 84,4 % | 82,7 % | 90,1 % | 89,3 % | 79,3 % | 85,9 % |
| MCP Atlas \*\* | 75,3 % | 70,6 % | - | - | 79,1 % | 78,2 % |
| Toolathlon | 55,6 % | 54,6 % | - | - | - | 48,8 % |
| Tau2-bench Telecom \*\*\* (invites originales) | 98,0 % | 92,8 % | - | - | - | - |

\*\* MCP Atlas : résultats de Scale AI après la dernière mise à jour d'avril 2026.   
\*\*\* Tau2-bench Telecom : résultats pour 5.5 et 5.4 avec les invites d'origine, c'est-à-dire sans ajustement de l'invite. Cela n'inclut pas les résultats d'autres laboratoires qui ont été évalués avec des ajustements de l'invite.

### Académique

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Évaluation** | **GPT‑5.5** | **GPT‑5.4** | **GPT‑5.5 Pro** | **GPT‑5.4 Pro** | **Claude** **Opus 4.7** | **Gemini 3.1 Pro** |
| GeneBench | 25,0 % | 19,0 % | 33,2 % | 25,6 % | - | - |
| FrontierMath niveaux 1 à 3 | 51,7 % | 47,6 % | 52,4 % | 50 % | 43,8 % | 36,9 % |
| FrontierMath niveau 4 | 35,4 % | 27,1 % | 39,6 % | 38,0 % | 22,9 % | 16,7 % |
| BixBench | 80,5 % | 74,0 % | - | - | - | - |
| GPQA Diamond | 93,6 % | 92,8 % | - | 94,4 % | 94,2 % | 94,3 % |
| Le dernier examen de l’humanité (sans outils) | 41,4 % | 39,8 % | 43,1 % | 42,7 % | 46,9 % | 44,4 % |
| Le dernier examen de l’humanité (avec outils) | 52,2 % | 52,1 % | 57,2 % | 58,7 % | 54,7 % | 51,4 % |

### Cybersécurité

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Évaluation** | **GPT‑5.5** | **GPT‑5.4** | **GPT‑5.5 Pro** | **GPT‑5.4 Pro** | **Claude** **Opus 4.7** | **Gemini 3.1 Pro** |
| Tâches de défis Capture-the-Flag (interne) \*\*\*\* | 88,10% | 83,7 % | - | - | - | - |
| CyberGym | 81,8 % | 79,0 % | - | - | 73,1 % | - |

\*\*\*\* Une extension des CTF les plus difficiles utilisés dans les fiches système, avec des défis supplémentaires complexes.

### Contexte étendu

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Évaluation** | **GPT‑5.5** | **GPT‑5.4** | **GPT‑5.5 Pro** | **GPT‑5.4 Pro** | **Claude** **Opus 4.7** | **Gemini 3.1 Pro** |
| Graphwalks BFS 256k f1 | 73,7% | 62,5 % | - | - | 76,9 % | - |
| Graphwalks BFS 1M f1 | 45,4 % | 9,4 % | - | - | 41,2 % (Opus 4.6) | - |
| Graphwalks parents 256k f1 | 90,1 % | 82,8 % | - | - | 93,6 % | - |
| Graphwalks parents 1M f1 | 58,5 % | 44,4 % | - | - | 72,0 % (Opus 4.6) | - |
| OpenAI MRCR v2 8-needle 4K-8K | 98,1 % | 97,3 % | - | - | - | - |
| OpenAI MRCR v2 8-needle 8K-16K | 93 % | 91,4 % | - | - | - | - |
| OpenAI MRCR v2 8-needle 16K-32K | 96,5 % | 97,2 % | - | - | - | - |
| OpenAI MRCR v2 8-needle 32K-64K | 90,00% | 90,5 % | - | - | - | - |
| OpenAI MRCR v2 8-needle 64K-128K | 83,1 % | 86 % | - | - | - | - |
| OpenAI MRCR v2 8-needle 128K-256K | 87,5 % | 79,3 % | - | - | 59,2 % | - |
| OpenAI MRCR v2 8-needle 256K-512K | 81,5 % | 57,5 % | - | - | - | - |
| OpenAI MRCR v2 8-needle 512K-1M | 74,0 % | 36,6 % | - | - | 32,2 % | - |

### Raisonnement abstrait

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Évaluation** | **GPT‑5.5** | **GPT‑5.4** | **GPT‑5.5 Pro** | **GPT‑5.4 Pro** | **Claude Opus 4.7** | **Gemini 3.1 Pro** |
| ARC-AGI-1 (Verified) | 95,0 % | 93,7 % | - | 94,5 % | 93,5 % | 98,0 % |
| ARC-AGI-2 (Verified) | 85,0 % | 73,3 % | - | 83,3 % | 75,8 % | 77,1 % |

Les évaluations de GPT ont été réalisées avec un niveau de raisonnement défini sur « xhigh » dans un environnement de recherche, ce qui peut produire des résultats légèrement différents de ceux de ChatGPT en production.

* [2026](/news/?tags=2026)

## Auteur

## Poursuivez votre lecture

[Afficher tout](/news/)

![Health in ChatGPT > Cover Image](https://images.ctfassets.net/kftzwdyauwt9/48aIp3cQOKJ57vpQeqOb8y/2e8732bcad5ceea1c7b20cf001bd2823/1_1_Art_Card.png?w=3840&q=90&fm=webp)

[Launching Health in ChatGPT

Produit23 juill. 2026](/index/health-in-chatgpt/)

![OpenAI Presence 1x1](https://images.ctfassets.net/kftzwdyauwt9/5JBDenSGI6wx5CMPPlaM5J/da9d8e27a0bd70d845a816b28ac641a9/OpenAI_Presence_1x1.png?w=3840&q=90&fm=webp)

[Présentation d’OpenAI Presence

Produit22 juill. 2026](/index/introducing-openai-presence/)

![GPT-5.6 is now the preferred model in Microsoft 365 Copilot > Cover image](https://images.ctfassets.net/kftzwdyauwt9/3MPipvFMxS8m3kTyCtwFgj/015747dcd34cb667a221688cfca64e0f/Frame.png?w=3840&q=90&fm=webp)

[GPT-5.6 est maintenant le modèle privilégié dans Microsoft 365 Copilot

Produit9 juill. 2026](/index/gpt-5-6-preferred-model-microsoft-365-copilot/)
