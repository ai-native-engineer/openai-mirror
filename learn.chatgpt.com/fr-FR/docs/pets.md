<!-- source: https://learn.chatgpt.com/fr-FR/docs/pets -->

Les Compagnons sont des personnages animés facultatifs qui vous aident à suivre le travail en cours. L’endroit où un compagnon apparaît
et ce qu’il affiche dépendent de l’interface utilisée. Le choix d’un compagnon modifie son
apparence, mais pas la façon dont ChatGPT effectue les tâches.

<div class="flow-root">
  <div class="w-full md:float-right md:ml-6 md:w-64 xl:w-72">
    
  </div>

## Utilisez un compagnon flottant

Dans l’application de bureau ChatGPT, un compagnon peut flotter au-dessus des fenêtres des autres applications et vous aider
à suivre l’activité de vos différentes discussions.

### Choisissez et réveillez un compagnon

1. Ouvrez le menu de profil en bas de l’application et sélectionnez **Compagnons**. Vous pouvez
   aussi ouvrir les [**Paramètres**](codex://settings), puis accéder à **Compagnons**.
2. Choisissez un compagnon intégré ou personnalisé.
3. Saisissez `/pet` ou ouvrez le menu des commandes et sélectionnez **Réveiller le compagnon**.

Pour masquer le compagnon, sélectionnez **Ranger le compagnon** dans **Paramètres \> Compagnons** ou dans le menu des commandes ; vous pouvez aussi saisir
`/pet` de nouveau. Votre sélection et la position du compagnon sont conservées
lorsque vous rouvrez l’application.

Lorsque vous sélectionnez un compagnon personnalisé, il apparaît également dans votre vue **Profil**.

### États du compagnon

| État          | Signification                                                  |
| --------------- | -------------------------------------------------------- |
| **En cours**     | Une tâche est en cours dans une discussion.                              |
| **Intervention requise** | Une discussion attend votre approbation, votre réponse ou une autre décision. |
| **Prêt**       | Une discussion est terminée et comporte une activité non lue.            |
| **Bloqué**     | Une discussion a échoué ou rencontré une erreur système.             |

Lorsque plusieurs discussions présentent une activité, le compagnon donne la priorité à celles qui nécessitent
votre intervention, puis aux discussions bloquées, prêtes et en cours. Ouvrez le volet d’activité pour
choisir une discussion.

Sélectionnez le compagnon pour revenir à ChatGPT ou sélectionnez une activité pour ouvrir sa discussion.
Le volet d’activité est distinct des [notifications
système](/fr-FR/codex/notifications?surface=app).

### Suivez l’Utilisation de l’ordinateur

Sur macOS, la fenêtre d’incrustation de la fonction [Utilisation de l’ordinateur](/fr-FR/codex/computer-use) peut
se fixer à un compagnon réveillé. Déplacez le compagnon et la fenêtre le suit.

### Créez un compagnon personnalisé

1. Ouvrez **Paramètres \> Compagnons** et sélectionnez **Créer votre propre compagnon**.
2. L’application installe le skill `hatch-pet` fourni, recharge les Skills et ouvre une
   nouvelle discussion.
3. Décrivez le compagnon souhaité et envoyez le prompt.
4. Une fois la tâche terminée, revenez dans **Paramètres \> Compagnons**, sélectionnez **Actualiser**,
   puis choisissez votre nouveau compagnon.

Les compagnons personnalisés créés dans l’application de bureau sont stockés localement sur votre ordinateur.
Ils ne sont pas automatiquement synchronisés avec ChatGPT sur le Web.

### Réduisez les animations

Les Compagnons respectent le réglage de réduction des animations de votre système d’exploitation. Lorsque l’option de réduction
des animations est activée, le compagnon affiche une image fixe au lieu d’une animation de sprites.

## Choisissez un compagnon sur le Web

Si les Compagnons sont disponibles pour votre compte et votre espace de travail, ouvrez **Paramètres \>
Personnalisation \> Compagnon \> Sélectionner un compagnon**. Choisissez un compagnon intégré ou sélectionnez
**Par défaut** pour utiliser ChatGPT sans compagnon.

Un compagnon Web apparaît dans les discussions ChatGPT Work compatibles. Il ne propose pas la
superposition flottante de l’application de bureau, ni son volet d’activité, ni sa commande `/pet`.

### Importez un compagnon personnalisé

Sélectionnez **Importer un compagnon** pour ajouter une feuille de sprites personnalisée. Le fichier doit être une
image PNG ou WebP transparente, mesurer exactement 1536 × 1872 pixels et ne pas dépasser 20 MiB.
Vous pouvez modifier, télécharger, actualiser ou supprimer les compagnons importés depuis ce même paramètre.

## Choisissez un compagnon pour le Terminal

Dans une session interactive de Codex CLI :

- Saisissez `/pets` ou `/pet` pour ouvrir le sélecteur de compagnon.
- Saisissez `/pets <name>` pour choisir directement un compagnon.
- Saisissez `/pets off` pour désactiver les compagnons dans le Terminal.

Le sélecteur comprend les compagnons intégrés et les compagnons personnalisés compatibles installés sur votre
ordinateur. Un compagnon dans le Terminal indique l’activité de la session CLI en cours. Il utilise les états
**En cours**, **Intervention requise**, **Prêt** et **Bloqué**, mais, contrairement à l’application de bureau, il ne
propose pas de volet regroupant l’activité de plusieurs discussions.

Les compagnons dans le Terminal nécessitent iTerm2 3.6 ou une version ultérieure, ou un terminal prenant en charge les graphismes Kitty ou
Sixel. Ils ne sont pas disponibles dans tmux ni Zellij.

## Compagnons dans l’Extension IDE

L’Extension IDE Codex ne propose ni sélecteur de compagnon ni superposition flottante.
Pour utiliser votre propre compagnon, utilisez l’application de bureau ChatGPT ou Codex CLI.

</div>

## Documentation associée

- [Notifications](/fr-FR/codex/notifications)
- [Tâches de longue durée](/fr-FR/codex/long-running-work)
- [Paramètres de l’application de bureau ChatGPT](/codex/reference/settings#pets)
