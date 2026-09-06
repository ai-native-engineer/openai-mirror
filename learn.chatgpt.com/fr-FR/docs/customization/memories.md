<!-- source: https://learn.chatgpt.com/fr-FR/docs/customization/memories -->

Les mémoires permettent à ChatGPT et à Codex de réutiliser le contexte utile de travaux antérieurs dans
des travaux à venir.
La version Web de ChatGPT utilise la mémoire de ChatGPT, tandis que les clients Codex locaux disposent d’un stockage
et de contrôles distincts pour leurs mémoires locales.

Conservez les consignes obligatoires de l’équipe dans `AGENTS.md` ou dans la documentation versionnée. Considérez
les mémoires comme un complément utile pour retrouver le contexte, et non comme l’unique source des règles qui doivent
toujours s’appliquer.

Dans l’application de bureau ChatGPT, utilisez `/memories` pour choisir si une discussion peut utiliser
les mémoires locales ou contribuer à la génération de futures mémoires. Pour activer ou désactiver cette fonctionnalité, accédez à
**Paramètres \> Personnalisation** .

Gérez la mémoire de ChatGPT depuis **Paramètres \> Personnalisation**. ChatGPT Work utilise
les paramètres de mémoire disponibles pour votre compte et votre espace de travail ; il n’utilise
ni le stockage local des mémoires de Codex ni les contrôles locaux correspondants.

Dans Codex CLI, utilisez `/memories` dans une session interactive pour définir si la
discussion en cours peut utiliser les mémoires locales existantes ou servir d’entrée à la génération de
futures mémoires. Consultez [Configuration des mémoires locales](#configure-local-memories) si la
commande n’est pas disponible.

L’extension IDE utilise le stockage local des mémoires de l’hôte Codex connecté. Lorsque
les mémoires sont activées sur cet hôte, utilisez les mêmes contrôles par discussion que dans
Codex CLI.

[Historique de l’ordinateur](/fr-FR/codex/customization/computer-history) est une fonctionnalité de l’application de bureau sur macOS
qui transforme l’activité dans les applications et sur les sites web autorisés en mémoires et
en une chronologie que ChatGPT et Codex peuvent consulter.

<a id="how-memories-work"></a>
<a id="memory-storage"></a>
<a id="control-memories-per-thread"></a>
<a id="control-memories-per-chat"></a>
<a id="control-memories-per-task"></a>
<a id="review-memories"></a>

## Fonctionnement des mémoires locales de Codex

Une fois les mémoires activées, Codex peut transformer le contexte utile de discussions antérieures éligibles
en fichiers de mémoire locale. Codex ignore les sessions actives ou de courte durée,
masque les secrets dans les champs de mémoire générés et met à jour les mémoires en
arrière-plan, plutôt qu’immédiatement à la fin de chaque discussion.

Les mémoires peuvent ne pas être mises à jour dès la fin d’une discussion. Codex attend qu’une
discussion soit inactive suffisamment longtemps pour éviter de résumer un travail encore
en cours.

Codex peut également ne pas exécuter une passe de génération de mémoires en arrière-plan lorsque le pourcentage restant associé à votre limite de débit Codex
est inférieur au seuil configuré, afin que Codex ne consomme pas de quota
lorsque vous approchez d’une limite.

## Stockage des mémoires locales

Codex stocke les mémoires dans votre répertoire personnel Codex. Par défaut, il s’agit de
`~/.codex`. Consultez [Emplacements de configuration et d’état](/fr-FR/codex/config-file/config-advanced#config-and-state-locations)
pour savoir comment Codex utilise `CODEX_HOME`.

Les principaux fichiers de mémoire se trouvent dans `~/.codex/memories/` et comprennent des résumés,
des entrées persistantes, des entrées récentes et des éléments à l’appui issus de discussions antérieures.

Considérez ces fichiers comme des données d’état générées. Vous pouvez les inspecter à des fins de dépannage
ou avant de partager votre répertoire personnel Codex, mais leur modification
manuelle ne doit pas constituer votre principal moyen de contrôle.

<a id="control-local-memories-per-task"></a>

## Gestion des mémoires locales par discussion

Dans l’application de bureau ChatGPT et l’interface TUI de Codex, utilisez `/memories` pour gérer le fonctionnement des mémoires dans
la discussion en cours. Les options propres à la discussion vous permettent de décider si celle-ci
peut utiliser les mémoires existantes et si Codex peut l’utiliser pour
générer de futures mémoires.

Les choix effectués pour une discussion ne modifient pas vos paramètres globaux de mémoire.

## Examen des mémoires locales

Ne stockez aucun secret dans les mémoires. Codex masque les secrets dans les champs de mémoire
générés, mais examinez tout de même les fichiers de mémoire avant de partager votre répertoire
personnel Codex ou les artefacts de mémoire générés.

<a id="enable-memories"></a>
<a id="configuration"></a>

## Configuration des mémoires locales

Les mémoires locales de Codex sont désactivées par défaut. Dans l’application de bureau ChatGPT, ouvrez
**Paramètres \> Personnalisation** , puis activez **Activer les mémoires**.

Pour une configuration par fichier, ajoutez l’indicateur de fonctionnalité dans `config.toml` :

```toml
[features]
memories = true

Pour connaître l’emplacement des fichiers de configuration et la liste complète des paramètres relatifs aux mémoires, consultez
[Principes de configuration](/fr-FR/codex/config-file/config-basic) et la [référence de
configuration](/fr-FR/codex/config-file/config-reference).

Voici les principaux paramètres propres aux mémoires :

- `memories.generate_memories` : détermine si les discussions nouvellement créées peuvent être
  stockées comme entrées pour la génération de mémoires.
- `memories.use_memories` : détermine si Codex injecte les mémoires existantes dans
  les sessions futures.
- `memories.disable_on_external_context` : lorsque sa valeur est `true`, exclut de la génération de mémoires les discussions ayant utilisé
  un contexte externe, comme des appels d’outils MCP, la recherche web ou la recherche
  d’outils. L’ancienne clé `memories.no_memories_if_mcp_or_web_search`
  est toujours acceptée comme alias.
- `memories.min_rate_limit_remaining_percent` : définit le pourcentage minimal restant de la limite de débit
  Codex requis avant le lancement de la génération de mémoires.
- `memories.extract_model` : remplace le modèle utilisé pour extraire les mémoires de chaque
  discussion.
- `memories.consolidation_model` : remplace le modèle utilisé pour la consolidation globale des
  mémoires.
