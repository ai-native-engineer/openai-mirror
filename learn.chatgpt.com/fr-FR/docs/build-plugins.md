<!-- source: https://learn.chatgpt.com/fr-FR/docs/build-plugins -->

Pour créer ou soumettre un plugin, consultez la
[documentation complète sur la création de plugins disponible sur developers.openai.com](/plugins).

<div className="not-prose my-6">
  
    Créer et soumettre un plugin
  
</div>

Cette page propose une brève introduction. Un plugin est un package installable
qui peut inclure des skills, un serveur MCP ou les deux. Un serveur MCP peut également renvoyer
une interface utilisateur facultative.

ChatGPT et Codex partagent un catalogue universel de plugins. Publiez une seule fois un plugin public
pour que la même fiche soit visible dans les interfaces prises en charge des deux
produits. Pendant le développement, utilisez une marketplace locale pour tester le package
avant de le soumettre au catalogue universel.

Pour distribuer des plugins dans un espace de travail via GitHub, consultez
[Gestion des plugins](/fr-FR/codex/enterprise/plugin-management).

Commencez par un skill tant que vous faites encore évoluer un workflow personnel.
Créez un plugin lorsque vous souhaitez partager ce workflow, regrouper des skills associés,
vous connecter à un service externe ou mettre une capacité stable à la disposition d’une équipe.

## Créer un plugin avec `@plugin-creator`

Pour une configuration aussi rapide que possible, utilisez le skill intégré `@plugin-creator` dans le mode Work
de ChatGPT ou `$plugin-creator` dans Codex.

  
    
  

Décrivez le résultat attendu, les skills ou le serveur MCP à inclure, et précisez si vous souhaitez
ajouter une entrée à une marketplace locale pour les tests. Par exemple :

```text
@plugin-creator Create a plugin named meeting-follow-up.
Include a skill that turns meeting notes into decisions, owners, and next steps.
Add it to a personal marketplace so I can test it locally.

Le skill crée le manifeste requis `.codex-plugin/plugin.json`, organise
le dossier du plugin et peut ajouter le plugin à une marketplace locale.

  
    
  

Une fois l’opération terminée :

1. Passez en revue `.codex-plugin/plugin.json`.
2. Vérifiez chaque skill inclus dans `skills/`.
3. Actualisez ChatGPT ou Codex, puis installez le plugin depuis sa source dans la marketplace
locale.
4. Testez le plugin dans une nouvelle conversation avec des requêtes représentatives.

Si le plugin inclut un serveur MCP, commencez par créer et tester ce serveur, puis
fournissez à `@plugin-creator` les informations de la connexion enregistrée. Suivez le
[workflow complet de création d’un serveur MCP](https://developers.openai.com/plugins/build/mcp-server)
pour les outils, l’authentification, le déploiement et les tests.

## Créer manuellement un plugin composé uniquement de skills

Un plugin minimal contient un manifeste et au moins un skill :

```text
meeting-follow-up/
├── .codex-plugin/
│   └── plugin.json
└── skills/
    └── meeting-follow-up/
        └── SKILL.md

Créez `.codex-plugin/plugin.json` :

```json
{
  "name": "meeting-follow-up",
  "version": "1.0.0",
  "description": "Turn meeting notes into decisions and next steps",
  "skills": "./skills/"
}

Ajoutez ensuite `skills/meeting-follow-up/SKILL.md` :

```md
---
name: meeting-follow-up
description: Extract decisions, owners, and next steps from meeting notes.
---

Review the meeting notes. Return:

1. Decisions
2. Action items with owners
3. Open questions

Utilisez un nom de plugin stable au format kebab case. Veillez à ce que la description du skill soit suffisamment
précise pour que ChatGPT et Codex puissent déterminer dans quels cas le workflow s’applique.

Utilisez `@plugin-creator` pour ajouter le dossier à une marketplace locale, puis installez et
testez le plugin avant de le partager.

## Poursuivre avec la documentation sur la création de plugins

Pour accéder à la documentation complète sur la création de plugins, consultez la
[documentation sur les plugins](https://developers.openai.com/plugins/). Elle couvre les sujets suivants :

- [Architecture des plugins](https://developers.openai.com/plugins/concepts/plugins)
- [Création de skills](https://developers.openai.com/plugins/build/skills)
- [Création d’un serveur MCP](https://developers.openai.com/plugins/build/mcp-server)
- [Ajout d’une interface utilisateur facultative](https://developers.openai.com/plugins/build/chatgpt-ui)
- [Mise en package d’un plugin](https://developers.openai.com/plugins/build/plugins)
- [Test d’un plugin](https://developers.openai.com/plugins/deploy/connect-chatgpt)
- [Soumission et publication](https://developers.openai.com/plugins/deploy/submission)

Pour parcourir les plugins, les installer, les activer ou les supprimer, consultez [Utiliser
des plugins](/fr-FR/codex/plugins).
