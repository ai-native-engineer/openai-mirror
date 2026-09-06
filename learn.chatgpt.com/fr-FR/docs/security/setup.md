<!-- source: https://learn.chatgpt.com/fr-FR/docs/security/setup -->

Cette page vous guide de l’accès initial jusqu’aux résultats examinés et aux
pull requests de correction dans Codex Security dans le cloud.

  Vérifiez d’abord que vous avez configuré Codex Cloud. Sinon, consultez [Codex
  Cloud](/fr-FR/codex/cloud) pour commencer.

## 1. Accès et environnement

Codex Security dans le cloud analyse les dépôts GitHub connectés via
[Codex Cloud](/fr-FR/codex/cloud).

- Vérifiez que votre espace de travail a accès à Codex Security dans le cloud.
- Vérifiez que le dépôt à analyser est disponible dans Codex Cloud.

Accédez à la page [Environnements Codex](https://chatgpt.com/codex/settings/environments) et vérifiez si le dépôt dispose déjà d’un environnement. Si ce n’est pas le cas, créez-en un avant de continuer.

<div class="not-prose my-8 max-w-6xl overflow-hidden rounded-xl border border-subtle bg-surface">
  
    
      
    
  
</div>

## 2. Nouvelle analyse de sécurité

Une fois l’environnement créé, accédez à la page [Créer une analyse de sécurité](https://chatgpt.com/codex/security/scans/new), puis choisissez le dépôt que vous venez de connecter.

Codex Security analyse d’abord les dépôts en remontant l’historique à partir des commits les plus récents. Cette méthode lui permet de constituer et d’actualiser le contexte d’analyse à mesure que de nouveaux commits sont ajoutés.

Pour configurer un dépôt :

1. Sélectionnez l’organisation GitHub.
2. Sélectionnez le dépôt.
3. Sélectionnez la branche à analyser.
4. Sélectionnez l’environnement.
5. Choisissez une **fenêtre d’historique**. Une fenêtre plus longue fournit davantage de contexte, mais l’analyse rétroactive prend plus de temps.
6. Cliquez sur **Créer**.

<div class="not-prose my-8 max-w-6xl overflow-hidden rounded-xl border border-subtle bg-surface">
  
    
      
    
  
</div>

## 3. Les analyses initiales peuvent prendre du temps

Lorsque vous créez l’analyse, Codex Security commence par effectuer une passe de sécurité au niveau des commits sur toute la fenêtre d’historique sélectionnée.
L’analyse rétroactive initiale peut prendre quelques heures, en particulier pour les dépôts volumineux ou les fenêtres d’historique longues.
Il est normal que les résultats n’apparaissent pas immédiatement. Attendez la fin de l’analyse initiale avant d’ouvrir un ticket ou de lancer un dépannage.

  La configuration de l’analyse initiale est automatique et complète. Elle peut prendre quelques heures. Ne
vous inquiétez pas si les premiers résultats tardent à apparaître.

## 4. Examinez les analyses et améliorez le modèle de menaces

<div class="not-prose my-8 max-w-6xl overflow-hidden rounded-xl border border-subtle bg-surface">
  
    
      
    
  
</div>

Une fois l’analyse initiale terminée, ouvrez-la et examinez le modèle de menaces généré.
Après l’apparition des premiers résultats, mettez à jour le modèle de menaces pour qu’il corresponde à votre architecture, à vos frontières de confiance et à votre contexte métier.
Codex Security peut ainsi hiérarchiser les problèmes pour votre équipe.

  Si vous souhaitez faire évoluer les résultats de l’analyse, vous pouvez modifier le modèle de menaces en fonction de votre
périmètre, de vos priorités et de vos hypothèses actualisés.

Après l’apparition des premiers résultats, réexaminez le modèle afin que les recommandations d’analyse restent en phase avec les priorités actuelles.
En le tenant à jour, vous aidez Codex Security à produire de meilleures suggestions.

Pour en savoir plus sur les modèles de menaces et leur influence sur la criticité et le triage, consultez [Améliorer le modèle de menaces](/fr-FR/codex/security/threat-model).

## 5. Examinez les résultats et appliquez des correctifs

Une fois l’analyse rétroactive initiale terminée, examinez les résultats dans la vue **Résultats** .

Vous pouvez utiliser deux vues :

- **Résultats recommandés** : une liste évolutive des 10 problèmes les plus critiques du dépôt
- **Tous les résultats** : un tableau triable et filtrable des résultats pour l’ensemble du dépôt

  
    
  

Cliquez sur un résultat pour ouvrir sa page de détails, qui contient :

- une description concise du problème
- les métadonnées clés, comme les détails du commit et les chemins de fichiers
- un raisonnement sur l’impact qui tient compte du contexte
- les extraits de code pertinents
- le contexte du chemin d’appel ou du flux de données, lorsqu’il est disponible
- les étapes de validation et leurs résultats

Vous pouvez examiner chaque résultat et créer une PR directement depuis sa page de détails.

## Documentation associée

- [Codex Security](/fr-FR/codex/security) présente une vue d’ensemble du produit.
- [FAQ sur Codex Security dans le cloud](/fr-FR/codex/security/faq) répond aux questions courantes sur le cloud.
- [Améliorer le modèle de menaces](/fr-FR/codex/security/threat-model) explique comment améliorer le contexte d’analyse et la hiérarchisation des résultats.
