<!-- source: https://learn.chatgpt.com/fr-FR/docs/security/threat-model -->

Découvrez ce qu’est un modèle de menaces et comment sa modification améliore les suggestions de Codex Security.

## Définition d’un modèle de menaces

Un modèle de menaces résume brièvement le fonctionnement de votre dépôt sous l’angle de la sécurité. Dans Codex Security, vous le modifiez sous la forme d’un `project overview`, et le système s’en sert de contexte pour les analyses futures, ainsi que pour la hiérarchisation et l’examen des résultats.

Codex Security génère une première ébauche à partir du code source. Si les résultats semblent peu pertinents, commencez par modifier le modèle de menaces.

Un modèle de menaces pertinent précise :

- les points d’entrée et les données d’entrée non fiables
- les frontières de confiance et les hypothèses d’authentification
- les flux de données sensibles ou les actions privilégiées
- les zones que votre équipe souhaite examiner en priorité

Par exemple :

> API publique de modification des comptes. Elle accepte les requêtes JSON et le chargement de fichiers. Elle utilise un service d’authentification interne pour effectuer les contrôles d’identité et enregistre les modifications de facturation via un service interne. Lors de la revue, concentrez-vous sur les contrôles d’authentification, l’analyse des fichiers chargés et les frontières de confiance entre services.

Codex Security dispose ainsi d’un meilleur point de départ pour les analyses futures et la hiérarchisation des résultats.

## Améliorer et réexaminer le modèle de menaces

Si vous souhaitez améliorer les résultats, commencez par modifier le modèle de menaces. Modifiez-le lorsque les résultats ne portent pas sur les zones qui vous intéressent ou apparaissent là où vous ne les attendez pas. Toute modification du modèle de menaces change le contexte des analyses futures.

  Certains utilisateurs copient le modèle de menaces actuel dans Codex et utilisent une discussion pour l’améliorer
en fonction des zones qu’ils souhaitent voir examinées plus attentivement, puis recollent la version
mise à jour dans l’interface Web.

### Où le modifier

Pour examiner ou mettre à jour le modèle de menaces, accédez aux [analyses de Codex Security](https://chatgpt.com/codex/security/scans), ouvrez le dépôt, puis cliquez sur **Modifier**.

## Documentation connexe

- [Configuration de Codex Security dans le cloud](/fr-FR/codex/security/setup) explique comment configurer le dépôt et examiner les résultats.
- [Codex Security](/fr-FR/codex/security) présente une vue d’ensemble du produit.
- [FAQ sur Codex Security dans le cloud](/fr-FR/codex/security/faq) aborde les questions courantes sur le cloud.
