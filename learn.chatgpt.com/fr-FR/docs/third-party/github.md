<!-- source: https://learn.chatgpt.com/fr-FR/docs/third-party/github -->

Utilisez la revue de code de Codex pour obtenir un second avis pertinent sur les pull
requests GitHub. Codex examine le diff de la pull request, suit les consignes de votre dépôt,
et publie une revue de code GitHub standard axée sur les problèmes graves. La révision de
sécurité, disponible en version préliminaire de recherche, analyse plus en profondeur les
problèmes de sécurité potentiels dans une pull request.

<br />

## Avant de commencer

Assurez-vous de disposer des éléments suivants :

- Une configuration de [Codex Cloud](/fr-FR/codex/cloud) pour le dépôt que vous souhaitez examiner.
- Un accès aux [paramètres de la revue de code de Codex](https://chatgpt.com/codex/settings/code-review).
- Un fichier `AGENTS.md` si vous souhaitez que Codex suive des consignes de revue propres au dépôt.

## Configurez la revue de code de Codex

Pour configurer les revues automatiques, vous devez disposer d’un dépôt GitHub connecté et
de droits de push ou d’administration GitHub sur les paramètres de ce dépôt.

1. Configurez [Codex Cloud](/fr-FR/codex/cloud).
2. Accédez aux [paramètres de Codex](https://chatgpt.com/codex/settings/code-review).
3. Activez **Revue de code** pour votre dépôt.

<div class="not-prose max-w-3xl mr-auto">
  
    
      
    
  
</div>
<br />

## Demandez une revue à Codex

1. Dans un commentaire de pull request, mentionnez `@codex review`.
2. Attendez que Codex réagisse (👀) et publie une revue.

<div class="not-prose max-w-xl mr-auto">
  
    
      
    
  
</div>
<br />

Codex publie une revue sur la pull request, comme le ferait un membre de l’équipe. Sur
GitHub, Codex signale uniquement les problèmes P0 et P1 afin que les commentaires de revue restent axés sur
les risques prioritaires.

<div class="not-prose max-w-3xl mr-auto">
  
    
      
    
  
</div>
<br />

## Activez les revues automatiques

Si vous souhaitez que Codex examine automatiquement chaque pull request, activez
**Revues automatiques** dans les [paramètres de Codex](https://chatgpt.com/codex/settings/code-review).
Codex publiera une revue chaque fois qu’une nouvelle PR sera ouverte pour revue, sans
qu’un commentaire `@codex review` soit nécessaire.

## Personnalisez ce que Codex examine

Codex recherche les fichiers `AGENTS.md` dans votre dépôt et suit les règles
de revue de code applicables. Ajoutez une section `## Code Review Rules` au fichier le plus proche
du code régi par ces règles. Utilisez des titres `###` pour regrouper les vérifications associées lorsque
cela est utile.

Par exemple, un service de reporting d’expériences peut empêcher qu’un comportement
postérieur à l’exposition modifie une cohorte de comparaison :

```md
## Code Review Rules

### Experiment cohorts

- Do not filter treatment comparisons on post-exposure behavior, including conversion or retention.
  Safe path: build cohorts from assignment or exposure; report conversion as an outcome.

Placez les règles valables pour tout le dépôt dans le fichier `AGENTS.md` à la racine, et les règles propres au service
dans un fichier imbriqué, tel que `services/experiment_reporting/AGENTS.md`. Codex
applique les consignes du fichier racine et les consignes plus spécifiques qui couvrent chaque fichier modifié, afin que
les modifications sans rapport n’aient pas à intégrer de contexte propre au service.

Commencez par deux ou trois règles concises qui formalisent des vérifications souvent explicitées lors des revues. Exemples de règles utiles :

- **Concentrez-vous sur les comportements importants propres au dépôt.** Décrivez la
  contrainte de compatibilité, le périmètre des données ou l’effet secondaire dangereux à signaler, et
  expliquez pourquoi c’est important.
- **Indiquez l’approche sûre ou l’exception.** Donnez à Codex suffisamment de contexte pour distinguer
  un véritable problème d’un comportement attendu.
- **Définissez des règles ciblées et pérennes.** Privilégiez les résultats attendus aux noms de fonctions qui
  peuvent changer, et placez les consignes près du code auquel elles s’appliquent.
- **Confiez les vérifications mécaniques à la CI.** N’incluez pas le formatage, le lint ni les autres
  vérifications déterministes dans les règles de revue.

Ouvrez une pull request représentative et demandez une revue avec `@codex review`.
Affinez les règles en fonction des problèmes détectés et des retours que vous recevez, puis réduisez la portée ou
supprimez les consignes qui génèrent du bruit.

Les règles de revue de code guident Codex ; elles ne remplacent ni les tests, ni les protections de branche, ni
les approbations requises.

Pour cibler ponctuellement un point précis, ajoutez-le à votre commentaire de pull request :

`@codex review for issues in the database migration`

## Révision de sécurité

La révision de sécurité est une revue supplémentaire destinée aux clients qui souhaitent
accorder une attention particulière aux problèmes de sécurité dans les pull requests. Elle analyse
les risques propres à la sécurité plus en profondeur que la revue de code, en examinant le diff de la pull request,
le contexte pertinent du dépôt ainsi que les modèles de menaces ou les consignes de
sécurité configurés.

La revue de code peut également repérer des problèmes liés à la sécurité dans le cadre de sa revue
générale. Certains constats de la revue de code et de la révision de
sécurité peuvent donc parfois se recouper.

### Configurez la révision de sécurité

Pour obtenir des instructions de configuration et des options plus détaillées, consultez la [révision de
sécurité](/fr-FR/codex/security/security-review).

1. Configurez [Codex Cloud](/fr-FR/codex/cloud).
2. Accédez aux [paramètres de Codex](https://chatgpt.com/codex/settings/code-review).
3. Dans **Préférences du dépôt**, choisissez les pull requests qui feront l’objet d’une révision de
   sécurité et le moment de son exécution. Sélectionnez **À chaque exécution de la revue de code** pour l’exécuter
   en même temps que la revue de code.

### Demandez une révision de sécurité

Pour demander manuellement une révision de sécurité, ajoutez ce commentaire à une pull request :

`@codex security review`

Codex réagit pendant l’exécution de la revue, puis publie directement les problèmes de sécurité détectés
sur la pull request. Ouvrez la tâche Codex associée et sélectionnez l’onglet **Rapport de
sécurité** pour afficher le rapport complet.

## Donnez suite aux constats de la revue

Une fois la revue publiée par Codex, vous pouvez lui demander de corriger les problèmes dans la même pull
request en ajoutant un autre commentaire :

```md
@codex fix the P1 issue

Codex démarre une discussion dans le cloud en utilisant la pull request comme contexte et peut pousser un correctif
sur la branche s’il dispose de l’autorisation nécessaire.

## Confiez d’autres tâches à Codex

Si vous mentionnez `@codex` dans un commentaire contenant autre chose que `review`, Codex démarre une [discussion dans le cloud](/fr-FR/codex/cloud) en utilisant votre pull request comme contexte.

```md
@codex fix the CI failures

## Résolvez les problèmes de revue de code

Si Codex ne réagit pas ou ne publie pas de revue :

- Vérifiez que vous avez activé **Revue de code** pour le dépôt dans les [paramètres de Codex](https://chatgpt.com/codex/settings/code-review).
- Vérifiez que la pull request appartient à un dépôt sur lequel [Codex Cloud](/fr-FR/codex/cloud) est configuré.
- Utilisez exactement le déclencheur `@codex review` dans un commentaire de pull request.
- Pour les revues automatiques, vérifiez que vous avez activé **Revues automatiques** et que
  l’événement de la pull request correspond à vos paramètres de déclenchement de revue.
