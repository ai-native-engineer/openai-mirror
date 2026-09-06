<!-- source: https://learn.chatgpt.com/fr-FR/docs/integrated-terminal -->

Chaque discussion de l’application de bureau ChatGPT comprend un terminal associé à son projet ou
à son arbre de travail en cours. Ouvrez-le à l’aide de l’icône du terminal située en haut à droite de l’application, ou
appuyez sur <kbd>Ctrl</kbd>+<kbd>\`</kbd>.

  
    
  

## Exécutez et validez votre projet

Utilisez le terminal pour valider vos modifications, exécuter des scripts et effectuer des opérations Git
sans changer d’application. ChatGPT peut lire la sortie actuelle du terminal. Il peut donc
vérifier un serveur de développement en cours d’exécution ou consulter un build ayant échoué pendant qu’il travaille
avec vous.

Voici quelques commandes courantes :

- `git status`
- `git pull --rebase`
- `pnpm test` ou `npm test`
- `pnpm run lint` ou une autre vérification spécifique au projet

## Créez des actions réutilisables

Si vous exécutez régulièrement une commande, définissez une action dans votre [environnement local](/fr-FR/codex/environments/local-environment#actions).
Les actions s’affichent sous forme de raccourcis dans l’application de bureau ChatGPT et s’exécutent dans le terminal
intégré.

<kbd>Cmd</kbd>+<kbd>K</kbd> ouvre la palette de commandes de l’application ; ce raccourci n’efface pas le contenu du
terminal. Pour effacer le contenu du terminal, appuyez sur <kbd>Ctrl</kbd>+<kbd>L</kbd>.
