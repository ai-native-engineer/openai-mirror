<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/deploy-app-or-website -->

## Commencez par le site et la cible de déploiement

Codex peut créer ou mettre à jour un site web ou une application, lancer les vérifications du projet, puis en effectuer le déploiement avec Vercel et renvoyer l’URL.

Pour bien démarrer, fournissez à Codex un point de départ concret : un dépôt, une capture d’écran, une carte, un brief de design, une note produit, une documentation d’API ou une source de données. Codex doit inspecter le projet avant de le modifier, puis utiliser le plugin Vercel afin de déployer un aperçu par défaut.

Utilisez `@build-web-apps` lorsque Codex doit créer ou peaufiner l’application. Utilisez `@vercel` lorsque Codex doit déployer l’application, inspecter le déploiement ou consulter les journaux de build Vercel.

## Vérifiez le résultat avant de le partager

Codex doit vous indiquer les modifications apportées et la commande utilisée pour effectuer le build du projet, puis préciser si le déploiement Vercel est prêt. Si le déploiement nécessite une variable d’environnement, le choix d’une équipe, la configuration d’un domaine ou une étape de connexion, Codex doit vous le signaler plutôt que de faire comme si le site était terminé.

Toute modification en production doit être demandée explicitement. Un déploiement d’aperçu est effectué par défaut ; ne demandez un déploiement en production que si c’est bien votre intention.

## Itérez à partir de l’URL en ligne

Une fois l’aperçu disponible, gardez la même discussion ouverte. Demandez à Codex d’ouvrir l’URL, de corriger les problèmes de mise en page, de mettre à jour les textes, d’intégrer les données manquantes ou de consulter les journaux Vercel si le déploiement échoue. La discussion contient déjà le contexte relatif au dépôt, au déploiement et au build.

Les demandes de suivi efficaces sont précises :

- "La mise en page est trop dense sur mobile. Corrigez-la et redéployez l’aperçu."
- "Utilisez le même projet et ajoutez les dernières données de \[source\]."
- "Consultez les journaux du build en échec et corrigez le déploiement."
