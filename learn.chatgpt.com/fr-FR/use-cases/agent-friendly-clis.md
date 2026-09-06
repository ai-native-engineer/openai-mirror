<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/agent-friendly-clis -->

## Introduction

Lorsque Codex utilise régulièrement la même API, la même source de journaux, la même boîte de réception exportée, la même base de données locale ou le même script d’équipe, fournissez-lui une interface composable pour ce travail : une commande qu’il peut exécuter depuis n’importe quel dossier, dont il peut examiner et affiner les résultats, et qu’il peut combiner avec `git`, `gh`, `rg`, des tests et les scripts du dépôt.

Ajoutez un skill associé qui indique quand Codex doit utiliser la CLI, quoi exécuter en premier, comment limiter la taille des sorties, où sont enregistrés les fichiers téléchargés et quelles commandes d’écriture nécessitent une approbation.

Dans ce workflow, `$cli-creator` aide Codex à créer la commande. `$skill-creator` aide Codex à enregistrer un skill réutilisable tel que `$ci-logs`, que les tâches ultérieures pourront invoquer par son nom.

## Mode d’emploi

1. [Déterminez si la tâche nécessite une CLI](#choose-what-the-cli-should-do)
2. [Fournissez à Codex la source à étudier](#share-the-docs-files-or-commands)
3. [Exécutez `$cli-creator`](#ask-codex-to-build-the-cli-and-skill)
4. [Testez la commande installée](#verify-the-command-works-from-any-folder)
5. [Invoquez plus tard le skill enregistré](#use-the-skill-later)

## Choisissez ce que doit faire la CLI

Commencez par définir ce que vous voulez que Codex fasse, et non la technologie que vous voulez lui faire développer. Une bonne CLI transforme toute opération récurrente de lecture, de recherche, de téléchargement, d’exportation, de création de brouillon, de téléversement, d’interrogation de l’état ou d’écriture sécurisée en une commande que Codex peut exécuter depuis n’importe quel dépôt.

| Situation                                              | Ce que Codex peut faire avec la CLI                                                                                              |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------- |
| **Les journaux de CI ne sont accessibles que depuis une page de build.**                  | À partir d’une URL de build, téléchargez les journaux des jobs en échec dans `./logs`, puis renvoyez les chemins des fichiers ainsi que de courts extraits.                          |
| **Les tickets d’assistance sont fournis sous forme d’export hebdomadaire.**         | Indexez le dernier export CSV ou JSON, effectuez une recherche par client ou par expression, puis lisez un ticket à partir de son ID stable.                        |
| **Une réponse d’API est trop volumineuse pour tenir dans le contexte.**          | Ne listez que les champs nécessaires, lisez l’objet complet à partir de son ID et exportez la réponse intégrale dans un fichier.                      |
| **Un export Slack contient de longs fils de discussion.**                   | Effectuez une recherche avec `--limit`, lisez un seul fil de discussion et renvoyez le contexte environnant plutôt que l’intégralité de l’archive.                             |
| **Un script d’équipe exécute quatre étapes différentes.**           | Répartissez la configuration, la découverte, le téléchargement, la création de brouillon, le téléversement, l’interrogation de l’état et l’écriture en production entre des commandes distinctes.                               |
| **Un plugin trouve l’enregistrement, mais Codex a besoin d’un fichier.** | Conservez le plugin dans la discussion ; utilisez une CLI pour télécharger la pièce jointe, la trace, le rapport, la vidéo ou le lot de journaux, puis renvoyez le chemin. |

## Fournissez la documentation, les fichiers ou les commandes

Codex a besoin d’un élément concret à étudier : de la documentation ou une spécification OpenAPI, une commande curl dont les données sensibles ont été masquées, un chemin vers un export ou une base de données, un dossier de journaux ou un script existant. Si vous souhaitez que la CLI suive un style familier, collez une sortie `--help` concise provenant de `gh`, de `kubectl` ou de l’outil de votre équipe.

Si la commande nécessite une authentification, indiquez à Codex le nom de la variable d’environnement, le chemin du fichier de configuration ou le parcours de connexion à prendre en charge. Définissez vous-même le secret dans votre shell ou votre fichier de configuration. Ne collez aucun secret dans la discussion. Demandez à Codex de faire échouer explicitement la vérification de configuration de la CLI lorsque les informations d’authentification manquent.

## Demandez à Codex de créer la CLI et le skill

Utilisez le prompt de démarrage de cette page. Indiquez la source que Codex doit étudier et la première tâche que la CLI doit prendre en charge.

Avant que Codex n’écrive du code, il doit présenter l’interface de commande proposée et ne demander que les informations manquantes sans lesquelles le développement serait bloqué.

## Vérifiez que la commande fonctionne depuis n’importe quel dossier

Codex ne doit pas s’arrêter après avoir exécuté `cargo run`, `python path/to/script.py` ou une commande de paquet sans installation préalable. Demandez-lui de tester la commande installée depuis un autre dépôt ou un dossier temporaire, comme une tâche ultérieure l’utilisera.

**Testez la CLI comme le ferait un futur agent**

Si Codex renvoie un énorme bloc JSON, demandez-lui de limiter le contenu de la réponse par défaut et d’ajouter un export dans un fichier pour les charges utiles complètes. S’il oublie la règle d’approbation, demandez-lui de mettre à jour le skill associé avant de l’utiliser dans une autre tâche.

## Réutilisez le skill ultérieurement

Lorsque vous avez de nouveau besoin de la CLI, invoquez le skill au lieu de recoller la documentation :

Pour les tâches récurrentes, testez une fois le skill dans une discussion, puis demandez à Codex de [planifier une tâche pour cette même invocation depuis la discussion](/fr-FR/codex/automations#schedule-a-task-inside-a-chat).
