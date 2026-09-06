<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/github-code-reviews -->

## Comment l’utiliser

Commencez par ajouter la revue de code Codex à votre organisation ou à votre dépôt GitHub.
Pour en savoir plus, consultez [la revue de code Codex dans GitHub](/fr-FR/codex/third-party/github).

Vous pouvez configurer Codex pour qu’il effectue automatiquement la revue de chaque pull request, ou demander une revue avec `@codex review` dans un commentaire de la pull request.

Si Codex signale une régression ou un problème potentiel, vous pouvez lui demander d’y remédier en ajoutant à la pull request un commentaire contenant un prompt de suivi tel que `@codex fix it`.

Cela lancera une nouvelle discussion dans le cloud pour corriger le problème et mettre à jour la pull request.

## Définissez les consignes de revue

Pour personnaliser ce que Codex examine, ajoutez une section `## Code Review Rules` dans le fichier
`AGENTS.md` le plus proche du code auquel s’appliquent ces règles. Par exemple :

```md
## Code Review Rules

### Experiment cohorts

- Do not filter treatment comparisons on post-exposure behavior, including conversion or retention.
  Safe path: build cohorts from assignment or exposure; report conversion as an outcome.

Placez les règles communes à tout le dépôt dans le fichier `AGENTS.md` à la racine, et celles propres à un service
dans un fichier situé plus bas dans l’arborescence. Rédigez des règles concises : décrivez le comportement à signaler ainsi que toute
alternative sûre ou exception, et réservez à la CI les vérifications de mise en forme et de lint. Consultez
[Personnaliser ce que Codex examine](/fr-FR/codex/third-party/github#customize-what-codex-reviews)
pour obtenir des conseils sur la configuration et la rédaction des règles.
