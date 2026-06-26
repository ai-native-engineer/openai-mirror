<!-- source: https://academy.openai.com/public/resources/paris-sme-accelerator-2026-04-20 -->

# Paris SME Accelerator - un centre de ressources

![Paris SME Accelerator - un centre de ressources](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/Screenshot-2026-04-20-at-00-14-191174a2-a8cf-4171-a821-f8189ff0e31e-1776640527674.jpeg?fit=scale-down&width=1200)

# Workplace & Business

# Use Cases

## Un centre de ressources pour les participants à l’Accélérateur IA pour PME de Paris

June 3, 2026 · Last updated on June 7, 2026

![Paris SME Accelerator - un centre de ressources](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/Screenshot-2026-04-20-at-00-14-191174a2-a8cf-4171-a821-f8189ff0e31e-1776640527674.jpeg?fit=scale-down&width=1200)

## Bienvenue

Utilisez cette page comme ressource d’accompagnement pour l’Accélérateur IA pour PME. Vous y trouverez les supports de présentation, un bref récapitulatif des contenus abordés pendant la session, des amorces de prompts prêtes à l’emploi, ainsi que les ressources actuelles de l’OpenAI Academy pour continuer sur cette lancée après l’événement.

## **Liens rapides**

#### [Supports de présentation de l’Accélérateur IA pour PME](https://drive.google.com/file/d/19r5h5ybUQayOl6ZC2pKi1v5Tageh8OFt/view?usp=drive_link) [Fichiers d’exemple](https://drive.google.com/drive/folders/1MD5lqhdnPijiRI8AewTwKJm4QE2Os-0E)﻿

## Agenda

|  |
| --- |
| Bienvenue |
| Les bases de ChatGPT |
| Workflow I : démonstration et essai |
| Workflow II : démonstration et essai |
| Solution Studio I : créons ensemble |
| Déjeuner |
| Acteur local de référence |
| Solution Studio II  : créez le vôtre |
| Démonstration + conclusion |

## **Fichiers d’exemple**

Tout au long de la journée, vous pouvez suivre ce lien pour accéder aux [**fichiers d’exemple pour les exercices pratiques.**](https://drive.google.com/drive/folders/1MD5lqhdnPijiRI8AewTwKJm4QE2Os-0E)﻿

## Bases du prompting

* Tâche : ce que vous voulez que ChatGPT fasse.

* Contexte : ce qu’il doit savoir sur votre public, vos contraintes ou vos fichiers.

* Attendu : à quoi doit ressembler le résultat final - format, ton, longueur et sections requises.

# **Activité d’échauffement**

Travaillez en binôme. Prenez un prompt vague et rendez-le suffisamment précis pour pouvoir le réutiliser. Puis partagez la meilleure « amélioration de prompt ».

* Rédige du contenu marketing pour mon entreprise.

* Crée-moi un flyer pour cette promotion.

* Réponds à cet avis négatif.

* Élabore un plan pour améliorer mon entreprise.

## **Flux de travail du jour (Regarder** → **Essayer** → **Partager)**

### **Flux de travail 1 : campagne de vente de fleurs de printemps**

**Ce que cela permet de faire :** transformer une offre en contenus prêts à l’emploi pour les clients, que vous pouvez réutiliser. Outil utile : Projects.

**Fichiers d’exemple à importer :**

* ﻿[WF1\_Harbour\_Bloom\_Business\_Profile.txt](https://drive.google.com/file/d/1bUUUp3D8R2C8nxCjy7N7bdn-1W3hbFzC/view?usp=drive_link)﻿

* ﻿[WF1\_Harbour\_Bloom\_Brand\_Voice.txt](https://drive.google.com/file/d/10cupCAWLDh5ohKeH7wmIpMNzFBU8riRK/view?usp=drive_link)﻿

Instructions du projet

```
Tu es l’assistant de campagne de Harbour Bloom Florist.

Aide à créer des supports marketing et de communication destinés aux clients pour les promotions, les campagnes saisonnières et les opportunités de vente du quotidien.

Utilise d’abord les fichiers importés.

Entreprise : fleuriste indépendant de quartier à Londres.

Public : habitants locaux, professionnels pressés et petites entreprises à proximité.

Ton : chaleureux, moderne, utile, local, jamais mièvre.

Toujours :

produire des contenus clairs, courts et directement utilisables

mentionner la livraison ou le retrait en boutique lorsque c’est pertinent

éviter de promettre des variétés de fleurs ou des stocks précis, sauf si l’utilisateur les fournit

poser une courte question de clarification si les dates, les canaux ou les détails de l’offre sont manquants

privilégier par défaut un langage soigné et pratique plutôt qu’un ton trop promotionnel
```

Prompt de départ

```
Crée une mini-campagne pour l’offre de bouquets de printemps de Harbour Bloom Florist.

Offre :

15 % de réduction sur les bouquets de printemps de ce vendredi à dimanche.

La livraison locale le jour même est disponible pour les commandes passées avant 13 h, dans la limite des stocks disponibles.

Public :

Habitants locaux achetant des cadeaux, professionnels pressés commandant à la dernière minute, et petites entreprises à proximité.

Réponds avec :

Un message central en 2 phrases

Trois options de titres

Une légende Instagram

Un court e-mail promotionnel

Un court SMS ou message privé

Une affiche simple en boutique
```

### **Flux de travail 2 : retours clients → plan d’action**

**Ce que cela permet de faire** : transformer des avis clients et un simple aperçu des ventes en grands thèmes, pistes d’amélioration, brouillons de réponses et checklist hebdomadaire. Outil utile : Analyse de données.

**Fichiers d’exemple :**

* ﻿[WF2\_Harbour\_Bloom\_Sales\_Snapshot.csv](https://drive.google.com/file/d/1Q6yZifYBwq-uhDyHCzdRi9y-e1PC8x57/view?usp=drive_link)﻿

* ﻿[WF2\_Harbour\_Bloom\_Customer\_Reviews.csv](https://drive.google.com/file/d/1WDIZva-Hkx90SBcqNOo-ETtRpW73V_wG/view?usp=drive_link)﻿

Exemple de séquence de prompts

```
Parle-moi de ce fichier. Selon toi, que signifie chaque colonne ? Quel contexte t’aiderait à bien l’analyser ?
```

```
Il s’agit de données de ventes hebdomadaires pour Harbour Bloom Florist à Londres. Nous voulons comprendre les tendances des ventes, le poids des remboursements et les aspects de l’activité qui méritent notre attention.
```

```
Qu’est-ce qui ressort ? Résume les principales tendances en termes simples. Puis dis-moi à quoi cette entreprise devrait prêter attention au cours des deux prochaines semaines.
```

```
Crée un graphique simple des transactions hebdomadaires et superpose les remboursements sur le même graphique.
```

```
À présent, examine ce fichier d’avis clients. Identifie :

(1) les principaux thèmes, avec des citations d’exemple ;

(2) les 3 principales améliorations opérationnelles que nous pourrions mettre en place cette semaine ;

(3) deux brouillons de réponses calmes et utiles à des avis négatifs ;

(4) une checklist hebdomadaire pour le personnel.
```

**Options avancées facultatives**

Effectuez une recherche sur le web et trouvez des sources avec [**Deep Research**](https://academy.openai.com/home/clubs/work-users-ynjqu/resources/deep-research)

Récupérez des informations en direct depuis Google Drive ou SharePoint avec [**Apps**](https://academy.openai.com/public/clubs/work-users-ynjqu/resources/connectors)﻿

## ﻿

## **Créateur d’offres / de propositions**

**Idéal pour :** transformer un service, une formule ou une promotion en textes soignés destinés aux clients, ainsi qu’en messages de suivi.

**Fichier de connaissances d’exemple :** [GPT2\_Offer\_Proposal\_Builder\_Knowledge.txt](https://drive.google.com/file/d/1CQ0tNiyPhp3_l8Xr1_QcuXuEqgSXIm4a/view?usp=drive_link)﻿

```
Tu es le créateur d’offres / de propositions de Harbour Bloom Florist.

Objectif

Transformer une opportunité commerciale, une demande client ou une promotion encore approximative en texte clair, prêt à être envoyé au client.

Utilise d’abord le fichier de connaissances importé. Si l’utilisateur n’a pas fourni les éléments essentiels, demande-les avant de rédiger.

Un bon résultat doit être :

précis

facile à envoyer ou à copier dans un e-mail

réaliste pour une petite entreprise

clair sur les prochaines étapes

N’invente jamais de prix, de disponibilité ou de détails de formule qui ne figurent pas dans le fichier de connaissances.

S’il manque des informations clés, pose d’abord 3 courtes questions.

Lorsque l’utilisateur partage une demande, réponds avec :

Un résumé en une ligne de l’opportunité

Les questions sur les informations manquantes, si nécessaire

Un brouillon d’e-mail de réponse ou de proposition

Un court SMS ou message privé de suivi facultatif

Les prochaines étapes internes pour l’équipe

Ton

Chaleureux, soigné, pratique, sans exagération.
```

## **Coach d’intégration et de formation**

**Idéal pour :** transformer des notes de processus et des politiques internes en checklists, supports d’intégration et conseils pour l’équipe.

**Fichier de connaissances d’exemple :** [GPT3\_Onboarding\_Training\_Coach\_Knowledge.txt](https://drive.google.com/file/d/1p4fCT6lyCbIC2lAeleT4bVWnqk06QL3G/view?usp=drive_link)﻿

**GPT instructions**

```
Tu es le coach d’intégration et de formation de Harbour Bloom Florist.

Objectif

Aider les managers à transformer les processus internes en checklists simples, modes opératoires, plans d’intégration, notes de coaching et réponses aux questions fréquentes du personnel.

Utilise d’abord le fichier de connaissances importé.

N’invente pas de politique RH, de conseil juridique ni de consignes disciplinaires.

Si une politique est manquante, indique à l’utilisateur ce qu’il doit confirmer avec un manager.

Formats recommandés

checklist étape par étape

plan d’intégration jour par jour

FAQ de référence rapide

scénario de formation ou court quiz

étape de vérification pour le manager

Style

Français simple, pratique, calme et facile à parcourir.

Lorsque tu réponds :

Commence par le format le plus utile pour la demande

Garde les listes courtes et actionnables

Signale tout élément qu’un manager devrait vérifier

Si la demande est vague, demande le rôle, le créneau de travail et la tâche pour laquelle le membre du personnel a besoin d’aide
```

## **Solution Studio II : Créez le vôtre**

Choisissez le format le plus simple adapté à votre problème :

* **Chat / pack de prompts** — le plus rapide lorsque vous êtes encore en phase d’exploration.

* **Projet** — idéal lorsque vous avez besoin des mêmes fichiers et instructions pour plusieurs tâches liées.

* **GPT personnalisé** — idéal pour une tâche répétable, avec des connaissances stables et un format de réponse cohérent.

* **Flux de travail de données** — idéal pour les feuilles de calcul, les rapports, les avis clients et l’analyse des tendances.

## **Méthode de création en 5 étapes**

1. Définissez la tâche à accomplir en une phrase.

2. Ajoutez le contexte et les connaissances : de quels fichiers, exemples, politiques ou notes a-t-il besoin ?

3. Précisez le résultat attendu : format, longueur, ton et éléments à inclure obligatoirement.

4. Ajoutez des garde-fous : ce qu’il ne doit jamais faire et les situations dans lesquelles il doit demander des précisions.

5. Testez sa fiabilité : 3 cas normaux, 1 cas limite, 1 cas avec informations manquantes.

## **Critères de finalisation**

Cochez ces étapes pour savoir si votre solution est prête.

* Fonctionne de bout en bout avec un exemple d’entrée.

* Enregistrée dans le format que vous avez choisi.

* Le résultat est utilisable ou exportable.

* Inclut une étape rapide de vérification humaine.

## **Continuez à apprendre**

Envie d’aller plus loin après l’événement ? Consultez ces ressources pour poursuivre votre apprentissage de l’IA :

﻿[**Codex pour les débutants**](https://academy.openai.com/public/videos/codex-for-beginners-2026-04-22) — Codex est un agent IA auquel vous pouvez déléguer de vraies tâches. Découvrez comment démarrer avec ce webinaire.

Merci de vous être joints à nous aujourd’hui !

Table Of Contents

[ChatGPT for any role](/en/public/clubs/work-users-ynjqu/resources/chatgpt-for-any-role)

[5:52](/en/public/videos/introduction-to-prompt-engineering-2025-02-13)

Video

[Introduction to Prompt Engineering](/en/public/videos/introduction-to-prompt-engineering-2025-02-13)

[Prompting](/en/public/clubs/work-users-ynjqu/resources/prompting)

[Munich SME AI Accelerator - Resource Hub](/en/public/resources/munich-sme-ai-accelerator-resource-hub-2026-04-20)

May 1st, 2026 • Views 606

[10:00](/en/public/videos/josh-de-leeuw-cognitive-science-2025-09-08)

Video

[Josh de Leeuw (Cognitive Science)](/en/public/videos/josh-de-leeuw-cognitive-science-2025-09-08)

Aug 1st, 2025 • Views 89

[London SME AI Accelerator - Resource Hub](/en/public/resources/london-sme-ai-accelerator-resource-hub-2026-04-15)

Apr 27th, 2026 • Views 913

[Dublin SME AI Accelerator - Resource Hub](/en/public/resources/dublin-sme-ai-accelerator-resource-hub-2026-03-18)

Mar 18th, 2026 • Views 969

[Munich SME AI Accelerator - Resource Hub](/en/public/resources/munich-sme-ai-accelerator-resource-hub-2026-04-20)

May 1st, 2026 • Views 606

[London SME AI Accelerator - Resource Hub](/en/public/resources/london-sme-ai-accelerator-resource-hub-2026-04-15)

Apr 27th, 2026 • Views 913

[Dublin SME AI Accelerator - Resource Hub](/en/public/resources/dublin-sme-ai-accelerator-resource-hub-2026-03-18)

Mar 18th, 2026 • Views 969

[10:00](/en/public/videos/josh-de-leeuw-cognitive-science-2025-09-08)

Video

[Josh de Leeuw (Cognitive Science)](/en/public/videos/josh-de-leeuw-cognitive-science-2025-09-08)

Aug 1st, 2025 • Views 89
