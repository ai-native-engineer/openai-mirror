<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/draft-prds-from-sources -->

## Introduction

Avant de travailler sur un nouveau produit ou une nouvelle fonctionnalité, il est courant de rédiger un document d’exigences produit (PRD) pour s’accorder sur le périmètre et les exigences. Dans la plupart des cas, le contexte nécessaire à la rédaction de ce PRD est déjà disponible dans les systèmes internes de l’équipe : tickets dans Linear, discussions sur Slack, brouillons dans Notion ou Google Drive, etc. ChatGPT peut rassembler ce contexte et rédiger un PRD que vous pourrez réviser et affiner, tout en conservant une traçabilité claire des sources.

## Choisir les sources

Commencez par indiquer les sources que ChatGPT doit utiliser : le projet Linear, le canal ou le fil de discussion Slack consacré à la planification, ainsi que tous les documents Drive, pages Notion, notes de réunion ou fichiers locaux à citer dans le PRD.
Précisez également les sections que doit comporter le PRD, par exemple le problème, les utilisateurs, les exigences, l’UX, les aspects techniques, le plan de lancement, le calendrier ou les décisions.

1. Commencez par `$documents` si le résultat doit prendre la forme d’un véritable fichier DOCX.
2. Mentionnez explicitement les sources : le projet ou le jalon Linear, le canal ou le fil de discussion Slack, ainsi que les documents ou les notes que ChatGPT doit citer.
3. Indiquez à ChatGPT les sections que le PRD doit contenir.
4. Examinez d’abord l’annexe des sources, puis les exigences et les questions en suspens.
5. Utilisez la même discussion pour combler les lacunes, resserrer le périmètre et préparer le passage de relais.

<a id="refine-in-the-same-chat"></a>
<a id="refine-in-the-same-task"></a>

## Affiner le PRD dans la même discussion

Utilisez le prompt de démarrage de cette page pour produire le premier brouillon. S’il manque un élément, indiquez à ChatGPT la source manquante plutôt que de recommencer.

## Vérifier la traçabilité des sources

Avant de partager le PRD, demandez à ChatGPT de répertorier les affirmations qui sont peu ou pas étayées, les questions non résolues et les décisions qu’il a considérées comme confirmées. Si l’annexe des sources ne permet pas de vérifier facilement ces éléments, continuez à affiner le PRD dans la même discussion avant d’exporter ou de publier quoi que ce soit.

### Prompt suggéré

**Vérifier la traçabilité des sources**
