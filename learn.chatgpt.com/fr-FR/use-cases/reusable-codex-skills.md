<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/reusable-codex-skills -->

## Créez un skill que Codex pourra garder à disposition

Utilisez les skills pour fournir à Codex des instructions, des ressources et des scripts réutilisables pour vos tâches récurrentes. Un [skill](/fr-FR/codex/build-skills) permet de conserver la tâche, la documentation, la commande ou l’exemple qui a rendu Codex utile la première fois.

Commencez par un exemple qui fonctionne : une discussion dans laquelle Codex a appliqué une PR par cherry-pick, une checklist de publication issue de Notion, une série de commentaires de PR utiles ou un fil Slack décrivant un processus de lancement.

## Mode d’emploi

1. Ajoutez le contexte que vous souhaitez faire utiliser par Codex.

   Restez dans la discussion Codex que vous souhaitez conserver, collez le fil Slack ou le lien vers la documentation, puis ajoutez la règle, la commande ou l’exemple que Codex doit retenir.

2. Exécutez le prompt de démarrage.

   Le prompt indique le nom du skill à créer, puis transmet à `$skill-creator` la tâche, la documentation, la PR, la commande ou le résultat à conserver.

3. Laissez Codex créer et valider le skill.

   Le résultat doit définir `$skill-name`, préciser quand le skill doit se déclencher et placer les instructions réutilisables au bon endroit.

   Les skills placés dans `~/.codex/skills` sont disponibles depuis n’importe quel dépôt. Ceux du dépôt actuel peuvent être ajoutés à un commit afin que les autres membres de l’équipe puissent également les utiliser.

4. Utilisez le skill, puis mettez-le à jour depuis la discussion.

   Faites appel au nouveau `$skill-name` pour la prochaine PR, alerte, revue, note de version ou tâche de design. S’il utilise la mauvaise commande de test, omet une règle de revue ou une étape du runbook, ou produit un brouillon que vous n’enverriez pas, demandez à Codex d’intégrer cette correction au skill.

## Fournissez des éléments de référence

Fournissez à `$skill-creator` les éléments qui expliquent comment le skill doit fonctionner.

| Ce dont vous disposez                                              | Éléments à ajouter                                                                                                                                                             |
| ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Un flux de travail que vous souhaitez conserver, issu d’une discussion Codex** | Restez dans cette discussion et saisissez `use this chat`. Codex peut prendre comme point de départ le contexte de la discussion, les commandes, les modifications et les retours.                                         |
| **Documentation ou runbook**                                      | Collez la checklist de publication, ajoutez un lien vers le runbook de réponse aux incidents, joignez le PDF de l’API ou indiquez à Codex le guide Markdown de votre dépôt.                                 |
| **Conversation d’équipe**                                      | Collez le fil Slack dans lequel une alerte a été expliquée, ajoutez un lien vers la revue de PR contenant les règles frontend ou joignez la conversation avec le support qui décrit le problème rencontré par le client. |
| **Scripts ou commandes que le skill doit réutiliser**             | Ajoutez la commande de test, la commande de prévisualisation, le script de publication, le script de récupération des journaux ou la commande utilitaire locale que vous souhaitez voir Codex exécuter lors de ses prochaines tâches.                                    |
| **Un résultat satisfaisant**                                          | Ajoutez la PR fusionnée, l’entrée finale du journal des modifications, la note de lancement validée, le ticket résolu, la capture d’écran avant/après ou la réponse finale de Codex qui doit servir de référence pour les prochaines tâches.         |

Si la source se trouve dans Slack, Linear, GitHub, Notion ou Sentry, connectez cet outil à Codex à l’aide d’un [plugin](/fr-FR/codex/plugins), mentionnez-le dans le prompt de démarrage ou collez la partie pertinente dans la discussion.

## Ce que crée Codex

La plupart des skills commencent par un fichier `SKILL.md`. `$skill-creator` peut ajouter des documents de référence plus détaillés, des scripts ou des ressources si le flux de travail l’exige.

## Skills que vous pourriez créer

Utilisez la même méthode lorsque les tâches futures doivent consulter le même runbook, exécuter la même CLI, suivre la même grille de revue, rédiger le même compte rendu pour l’équipe ou contrôler la qualité du même parcours dans le navigateur. Par exemple :

- **`$buildkite-fix-ci`** télécharge les journaux des jobs ayant échoué, diagnostique l’erreur et propose le correctif de code minimal.
- **`$fix-merge-conflicts`** récupère localement une PR GitHub, la met à jour à partir de la branche de base, résout les conflits et renvoie la commande de push exacte.
- **`$frontend-skill`** aide Codex à respecter vos préférences d’interface et les composants existants, à suivre votre cycle de contrôle qualité par captures d’écran, à reprendre vos choix de ressources et à effectuer les finitions dans le navigateur.
- **`$pr-review-comments`** transforme les notes de revue en commentaires en ligne concis, au ton approprié et accompagnés de liens GitHub.
- **`$web-game-prototyper`** définit une première boucle jouable, choisit les ressources, ajuste les sensations de jeu, prend des captures d’écran et peaufine le résultat dans le navigateur.
