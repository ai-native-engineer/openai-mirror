<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/api-integration-migrations -->

## Introduction

À mesure que nous publions de nouveaux modèles et de nouvelles fonctionnalités d’API, nous vous recommandons de mettre à niveau votre intégration afin de profiter des dernières améliorations.
Passer d’un modèle à un autre ne se résume souvent pas à modifier le nom du modèle.

L’API peut avoir évolué. Par exemple, pour le modèle GPT-5.4, nous avons ajouté au message de l’assistant un nouveau paramètre `phase` qu’il est important d’inclure dans votre intégration. Mais surtout, le comportement du modèle peut différer et nécessiter de modifier vos prompts existants.

Lors d’une migration vers un nouveau modèle, veillez non seulement à apporter les modifications nécessaires au code, mais aussi à évaluer les répercussions sur vos flux de travail.

## Utilisez le skill OpenAI Docs

La page [Recommandations sur les modèles](/api/docs/guides/latest-model) regroupe, pour chaque génération de modèles, les recommandations concernant les fonctionnalités de l’API, le comportement des modèles, la migration et la conception de prompts.

Le skill OpenAI Docs inclut également des [recommandations spécifiques](https://github.com/openai/codex/blob/6323f0104d17d211029faab149231ba787f7da37/codex-rs/skills/src/assets/samples/openai-docs/references/upgrading-to-gpt-5p4.md) qui servent de référence concrète pour la migration. Pour connaître le modèle actuellement recommandé pour la mise à niveau, consultez la page [Recommandations sur les modèles](/api/docs/guides/latest-model).

Codex intègre désormais par défaut le skill OpenAI Docs. Veillez donc à le mentionner dans votre prompt pour accéder à toute la documentation à jour et aux recommandations les plus récentes lorsque vous développez avec l’API OpenAI.

## Mettez en place un pipeline d’évaluation robuste

Codex peut mettre automatiquement à jour vos prompts d’après les dernières recommandations de conception de prompts, mais vous devriez disposer d’un moyen de vérifier automatiquement que votre intégration fonctionne comme prévu.

Veillez à mettre en place un pipeline d’évaluation que vous pourrez exécuter chaque fois que vous modifierez votre intégration, afin de vérifier l’absence de régression du comportement.

Ce [guide du Cookbook](/cookbook/examples/evaluation/building_resilient_prompts_using_an_evaluation_flywheel) explique en détail comment procéder à l’aide de notre [API Evals](/api/docs/guides/evals).
