<!-- source: https://learn.chatgpt.com/fr-FR/docs/security/security-review -->

La revue Codex Security est disponible en préversion de recherche.
Elle est proposée aux clients ChatGPT Enterprise, Business, Edu et Pro ; elle n’est
pas disponible avec Plus. Pendant la période de lancement, la revue Codex Security ne
consomme pas de crédits ChatGPT. Des limites d’utilisation peuvent s’appliquer.

La revue Codex Security est une revue complémentaire destinée aux clients qui souhaitent
accorder une attention particulière aux problèmes de sécurité dans les pull requests.

La revue Codex Security examine les risques propres à la sécurité plus en profondeur que [la revue de
code](/fr-FR/codex/third-party/github), en analysant le
diff de la pull request, les éléments de contexte pertinents du dépôt et les modèles de menaces configurés
ou les directives de sécurité configurées. La revue de code peut également détecter des problèmes liés à la sécurité
dans le cadre de sa revue générale ; il peut donc arriver que certains constats se recoupent.

## Avant de commencer

Pour configurer l’exécution automatique de la revue Codex Security, vous devez disposer des éléments suivants :

- L’accès de votre espace de travail à la préversion de recherche de la revue Codex Security
- [Codex Cloud](/fr-FR/codex/cloud) configuré avec un dépôt GitHub connecté
- Des droits GitHub de push ou d’administration dans les paramètres du dépôt

Une analyse Codex Security existante est facultative.

<a id="configure-security-review"></a>

## Configurer la revue Codex Security

1. Accédez aux [paramètres de Codex](https://chatgpt.com/codex/settings/code-review).
2. Dans **Préférences du dépôt**, choisissez les pull requests pour lesquelles lancer une revue Codex
   Security :
   - L’option **Suivre les préférences personnelles** permet à chaque contributeur de choisir d’activer la revue dans ses paramètres personnels
     de revue Codex Security.
   - L’option **Examiner toutes les PRs** s’applique à toutes les pull requests du dépôt.
   - L’option **Examiner les PRs de l’équipe**, lorsqu’elle est disponible, s’applique aux pull requests ouvertes par
     des membres de votre espace de travail ChatGPT, et non par les membres d’une équipe GitHub.
3. Choisissez quand exécuter la revue Codex Security :
   - L’option **À l’ouverture d’une PR** lance une revue indépendante lorsqu’une pull request est ouverte.
   - L’option **À chaque push** lance une revue indépendante après le push de nouveaux commits.
   - L’option **À chaque exécution de la revue de code** nécessite l’activation de la revue de code et lance la revue Codex Security
     en parallèle.

## Ajouter le contexte du modèle de menaces

Vous pouvez configurer un modèle de menaces afin de renseigner Codex sur les
actifs de votre application, les frontières de confiance, les hypothèses de sécurité et les risques propres au dépôt.
Si le dépôt dispose déjà d’une configuration d’analyse Codex Security, vous pouvez utiliser
son modèle de menaces. Sinon, indiquez le chemin d’un fichier de modèle de menaces versionné
dans le dépôt. Si vous ne précisez aucune source, Codex régénère le
modèle de menaces à chaque revue.

## Définir les seuils de signalement

Par défaut, les revues Codex Security automatiques signalent uniquement les constats de gravité **Élevée** ou **Critique**.
Les revues demandées manuellement signalent, quant à elles, les constats de gravité **Moyenne**, **Élevée** ou
**Critique**. Vous pouvez définir séparément le niveau de gravité minimal pour les revues
automatiques et manuelles, et ajouter des exceptions pour certains chemins.

Les constats publiés sur une pull request ont la même visibilité sur GitHub
que cette pull request. Toute personne qui peut consulter la pull request peut aussi voir ces constats,
y compris dans les dépôts publics ou les pull requests de contributeurs externes à
votre espace de travail. Choisissez avec soin les seuils de signalement pour les dépôts où
les commentaires sur les pull requests peuvent être visibles par un large public. Le seuil de signalement détermine
ce que Codex publie sur GitHub ; le rapport complet de la revue Codex Security reste dans
Codex.

<a id="request-a-security-review"></a>

## Demander une revue Codex Security

Pour demander manuellement une revue Codex Security, ajoutez ce commentaire à une pull request :

`@codex security review`

Codex ajoute une réaction pendant l’exécution de la revue, puis publie directement sur la pull request les constats qui atteignent votre
seuil de signalement pour les revues manuelles. Ouvrez la tâche associée
dans Codex et sélectionnez l’onglet **Rapport de sécurité** pour consulter le rapport complet,
notamment le niveau de gravité, le chemin d’attaque, les éléments de preuve, la validation et les
recommandations de remédiation. Si aucun problème n’atteint le seuil de signalement, Codex ne publie
aucun constat sur la pull request.

## Documentation connexe

- La page [Examiner les pull requests GitHub avec Codex](/fr-FR/codex/third-party/github) explique le fonctionnement de la revue de code et de l’intégration GitHub.
- La page [Codex Security](/fr-FR/codex/security) présente une vue d’ensemble du produit.
- La page [Configuration de Codex Security dans le cloud](/fr-FR/codex/security/setup) explique les analyses de dépôts et l’examen des constats.
- La page [Améliorer le modèle de menaces](/fr-FR/codex/security/threat-model) explique comment affiner le contexte du dépôt.
