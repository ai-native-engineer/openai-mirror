<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/build-an-ai-tour-guide -->

## Introduction

Certains workflows sont plus faciles à apprendre quand quelqu’un vous montre où aller et quoi sélectionner. Utilisez Codex pour créer un parcours qui guide les utilisateurs dans votre application web tout en les laissant effectuer eux-mêmes les actions.

Grâce aux outils WebMCP donnant accès aux commandes, à l’état et à la documentation de votre application, Codex peut choisir l’instruction suivante en fonction de ce que voit l’utilisateur. Un utilisateur qui n’a pas encore connecté de service doit commencer par une étape différente de celui qui a déjà terminé la configuration.

## Mode d’emploi

1. Ouvrez le dépôt de votre application dans Codex et choisissez un workflow pour lequel guider les utilisateurs, comme la connexion d’un service ou l’ajout d’un dossier.
2. Fournissez la documentation pertinente et décrivez les états initiaux que le parcours doit prendre en charge.
3. Exécutez le prompt de démarrage de cette page pour ajouter les cibles du parcours, les outils de lecture de l’état de l’interface et l’accès aux instructions de l’application.
4. Testez le parcours dans un environnement de navigateur où Codex peut appeler les outils WebMCP de votre application. Demandez à Codex de vous guider, puis réalisez chaque étape vous-même.

Limitez la portée du premier parcours guidé. Vérifiez qu’il peut guider un utilisateur de la configuration jusqu’à la fin du workflow avant d’en ajouter d’autres.

## Exemple : ajoutez un dossier Google Drive dans Runme

Dans <a href="https://web.runme.dev" target="_blank" rel="noopener noreferrer">Runme</a>, les utilisateurs modifient des notebooks et utilisent un explorateur de fichiers pour ajouter des dossiers Google Drive et parcourir leurs fichiers. Le parcours guidé aide un nouvel utilisateur à trouver ces commandes et à apprendre la marche à suivre.

Pour en savoir plus sur Runme, vous pouvez lire <a href="https://developers.openai.com/blog/automating-repetitive-work-at-openai-with-codex" target="_blank" rel="noopener noreferrer">Automatiser les tâches répétitives chez OpenAI avec Codex</a>.

Regardez Codex mettre en évidence les commandes de Runme et expliquer leur rôle. Les captures d’écran ci-dessous montrent un parcours guidé distinct, consacré à l’ajout d’un dossier Google Drive.

<figure class="not-prose my-4">
  <video
    class="w-full rounded-lg border border-default"
    controls
    muted
    playsinline
    preload="metadata"
    poster="https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/tour-demo-poster.webp"
    aria-label="Codex demonstrates an AI tour of Runme's controls"
  >
    <source
      src="https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/runme-ai-tour-demo.webm"
      type="video/webm"
    />
    Votre navigateur ne prend pas en charge la balise vidéo.
  </video>
</figure>

Le parcours guidé Google Drive commence par une demande :

### Connectez Google Drive

Codex vérifie si Google Drive est connecté. Si ce n’est pas le cas, Codex met en évidence **Connecter Google Drive** et demande à l’utilisateur de sélectionner cette commande et de terminer la connexion.

![Codex met en évidence la commande « Connecter Google Drive » dans Runme et explique comment commencer.](https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/connect-google-drive.webp)

### Ouvrez l’explorateur de fichiers

Une fois la connexion terminée, Codex guide l’utilisateur vers l’explorateur de fichiers. L’instruction suivante tient compte de l’état mis à jour de l’application.

![Codex met en évidence la commande permettant d’ouvrir l’explorateur de fichiers de Runme.](https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/open-file-explorer.webp)

### Ajoutez le dossier

Une fois que l’utilisateur déploie la barre d’outils, Codex met en évidence la commande permettant d’ajouter un dossier Google Drive. L’utilisateur garde la maîtrise de l’interaction et apprend où retrouver cette commande la prochaine fois.

![Codex met en évidence la commande permettant d’ajouter un dossier Google Drive dans Runme.](https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/add-google-drive-folder.webp)

## Donnez à Codex le contexte nécessaire pour guider les utilisateurs

L’implémentation de Runme fournit trois types de contexte : les cibles du parcours guidé, l’état de l’application et la documentation. Les noms d’outils ci-dessous sont ceux de Runme ; adaptez ces mêmes fonctions à votre application.

### Rendez les commandes repérables

Attribuez aux cibles du parcours des valeurs `data-tour-id` stables et sémantiques, avec un libellé et une description pour chacune. Runme expose ces commandes via trois outils WebMCP :

- `listTargets` répertorie les cibles enregistrées, leurs identifiants, leurs libellés et leurs descriptions.
- `showTourStep({ target, title?, message, placement? })` met une cible en évidence et affiche une explication.
- `dismiss` retire la mise en évidence.

Codex peut ainsi identifier une commande et expliquer son rôle sans exécuter l’action à la place de l’utilisateur.

### Lisez l’état et attendez que l’utilisateur agisse

Runme conserve l’état lié au parcours guidé en dehors de React et l’expose via un contrôleur. Son outil `getUiSnapshot` fournit l’état actuel de l’interface, y compris le statut de connexion. `waitForUiChange(...)` permet à Codex d’attendre un changement, par exemple que l’utilisateur sélectionne la commande mise en évidence.

Demandez à Codex de relire l’état après chaque interaction. La progression du parcours doit dépendre de ce qui s’est passé dans l’application, et non du fait que Codex a déjà affiché une instruction.

### Conservez les instructions avec l’application

Runme inclut une documentation Markdown dans l’application et la rend accessible via WebMCP :

- `readInstructionsForAIAgents` explique comment Codex doit interagir avec l’application et ses outils.
- `listDocumentation()` répertorie les pages disponibles et leurs descriptions.
- `getDocumentation({ name })` renvoie la page sélectionnée au format Markdown.

Les instructions et les outils du parcours guidé peuvent être livrés avec l’application, sans plugin Codex distinct pour ce parcours.

## Passez le parcours guidé en revue

Essayez la même demande à partir de différents états initiaux. Vérifiez que le parcours saute les étapes de configuration déjà terminées, attend que l’utilisateur agisse et adapte ses instructions lorsque l’interface change.

Testez aussi une étape annulée et une commande qui n’est pas encore visible. Codex doit expliquer ce qui manque ou choisir une étape suivante valide. Il ne doit pas affirmer qu’une action a réussi simplement parce qu’il a mis un bouton en évidence.

Conservez l’authentification, les vérifications des permissions et les actions de l’utilisateur dans le parcours existant de l’application. Le parcours guidé doit aider les utilisateurs à comprendre l’interface sans contourner ces contrôles.

## Pour aller plus loin

Une fois que le premier parcours fonctionne, poursuivez dans la même discussion :

- « Testez cette visite guidée lorsque Google Drive est déjà connecté et que l’explorateur de fichiers est fermé. »
- « Gérez le cas où un utilisateur annule une étape, puis demande à reprendre la visite guidée. »
- « Ajoutez une visite guidée pour \[next workflow\], en réutilisant les cibles et les outils de lecture de l’état existants. »
