<!-- source: https://learn.chatgpt.com/fr-FR/docs/enterprise/manage-app-updates -->

L’application de bureau ChatGPT recherche et installe normalement elle-même les mises à jour. Si
votre organisation doit examiner les nouvelles versions avant que les utilisateurs ne les reçoivent, vous
pouvez désactiver son programme de mise à jour intégré et déployer les versions approuvées via
votre plateforme de gestion des appareils.

Le programme de mise à jour de l’application reste activé par défaut. Sa désactivation n’empêche pas
le Microsoft Store, Microsoft Intune, la gestion des appareils mobiles (MDM), les gestionnaires de
paquets ou d’autres outils de déploiement externes d’installer des mises à jour.

## Avant de commencer

Vérifiez que vous disposez des éléments suivants :

- Un accès à
[Configuration gérée](https://chatgpt.com/codex/settings/managed-configs)
  en tant qu’administrateur Codex de votre espace de travail.
- Une version de l’application de bureau ChatGPT pour macOS ou Windows qui prend en charge
les mises à jour gérées par l’organisation.
- Une plateforme MDM ou de déploiement logiciel capable d’installer les paquets d’application approuvés
sur vos appareils gérés.
- Un processus permettant de tester les nouvelles versions, de déployer les mises à jour de sécurité et de suivre
les versions installées de l’application.

Si vous n’avez pas déployé l’application sur Windows, commencez par
[Déployer l’application Windows](/fr-FR/codex/enterprise/windows-deployment).

## Désactiver les mises à jour dans l’application

  Lorsque vous désactivez les mises à jour dans l’application, votre organisation doit
déployer rapidement les nouvelles versions de l’application et les correctifs de sécurité. Retarder les mises à jour peut
exposer l’application et les composants qu’elle inclut à des vulnérabilités de sécurité
connues. Les anciennes versions de l’application ne bénéficient pas de correctifs de sécurité distincts ni
d’une prise en charge étendue.

Créez une stratégie gérée qui désactive le programme de mise à jour intégré à l’application de bureau :

1. Ouvrez
[Configuration gérée](https://chatgpt.com/codex/settings/managed-configs).
2. Sélectionnez **Ajouter une stratégie**, ou ouvrez une stratégie existante pour les utilisateurs, groupes ou
   plateformes que vous souhaitez gérer.
3. Sous **Cibles**, sélectionnez **Ajouter une cible** pour attribuer la stratégie à des
**Groupes**, **Utilisateurs** ou **Plateformes** spécifiques. Commencez par un petit groupe pilote lorsque cela est
   possible.
4. Ouvrez **TOML brut** et repérez l’éditeur **requirements.toml**.
5. Ajoutez la stratégie suivante :

   ```toml
   [features]
   in_app_updates = false

   Si votre stratégie contient déjà une table `[features]`, ajoutez
`in_app_updates = false` à cette table. N’ajoutez pas de seconde table `[features]`
   et ne placez pas le paramètre dans **config.toml**.

6. Sélectionnez **Enregistrer les modifications**.
7. Demandez aux utilisateurs concernés de quitter complètement l’application de bureau ChatGPT, puis de la rouvrir. Fermer
la fenêtre de l’application ne suffit pas toujours à la redémarrer.

Certains espaces de travail affichent un éditeur de liste de stratégies au lieu de l’onglet **TOML brut**. Dans
cette interface, ajoutez le même bloc TOML directement à la stratégie concernée, utilisez
**Groupes** pour l’attribuer lorsque cette option est disponible, puis sélectionnez **Enregistrer**.

Pour en savoir plus sur la distribution et l’ordre de priorité des stratégies gérées, consultez
[Configuration gérée](/fr-FR/codex/enterprise/managed-configuration).

## Vérifier le paramètre géré

Après le redémarrage de l’application, vérifiez la stratégie depuis l’appareil d’un utilisateur concerné :

1. Connectez-vous à l’application de bureau ChatGPT avec un compte auquel s’applique la stratégie.
2. Ouvrez **Paramètres** \> **Général**.
3. Repérez **Mises à jour dans l’application** et vérifiez que l’indicateur **Géré** s’affiche avec le message
   « Votre organisation a désactivé les mises à jour dans l’application. »
4. Vérifiez que votre plateforme de gestion des appareils peut toujours déployer une version approuvée de
l’application.

L’option de menu **Rechercher les mises à jour** peut rester visible même lorsque la stratégie
bloque les mises à jour dans l’application. Pour vérifier la stratégie, utilisez l’indicateur **Géré**
plutôt que de vérifier si cette option de menu s’affiche.

Si l’indicateur ne s’affiche pas après le premier redémarrage, l’application utilise peut-être encore
une stratégie mise en cache. Attendez que la stratégie s’actualise, puis quittez complètement l’application et
rouvrez-la. Ne vous fiez pas à la restriction des mises à jour tant que **Géré** ne s’affiche pas.

## Déployer les versions approuvées de l’application

Après avoir désactivé les mises à jour dans l’application, utilisez votre processus actuel de gestion des appareils
pour distribuer les nouvelles versions :

1. Choisissez une version de l’application que votre organisation prévoit de déployer.
2. Procurez-vous le paquet d’installation pris en charge pour chaque système d’exploitation et
chaque architecture d’appareil de votre parc.
3. Testez la version auprès d’un petit groupe représentatif d’utilisateurs.
4. Déployez le paquet approuvé avec Microsoft Intune, votre plateforme MDM ou
un autre outil de déploiement logiciel.
5. Consultez l’inventaire des appareils pour vérifier que votre plateforme a installé la version
prévue, puis étendez le déploiement à d’autres groupes.

Votre plateforme de gestion détermine comment échelonner les déploiements, sélectionner les versions
et gérer un déploiement qui n’aboutit pas. Si votre plateforme permet
le retour à une version antérieure, celui-ci ne prolonge pas la prise en charge et ne garantit pas
la compatibilité avec le service.

Pour macOS, téléchargez le
[programme d’installation de l’application de bureau ChatGPT](https://persistent.oaistatic.com/codex-app-prod/ChatGPT.dmg).
Pour connaître les méthodes d’installation sous Windows et obtenir les paquets propres à chaque architecture, consultez
[Déployer l’application Windows](/fr-FR/codex/enterprise/windows-deployment).

## Réactiver les mises à jour dans l’application

Pour rétablir le comportement normal des mises à jour de l’application :

1. Identifiez les stratégies gérées, les fichiers `requirements.toml` du système et les profils MDM
   qui désactivent les mises à jour pour les utilisateurs concernés.
2. Supprimez `in_app_updates = false` de chaque table `[features]` concernée.
3. Enregistrez les modifications des stratégies et redéployez toutes les exigences mises à jour via votre solution de gestion des appareils.
4. Demandez aux utilisateurs concernés de quitter complètement l’application de bureau ChatGPT, puis de la rouvrir.
5. Dans **Paramètres** \> **Général**, vérifiez que la ligne **Mises à jour dans l’application**
   signalée comme gérée ne s’affiche plus.

Lorsqu’aucune stratégie applicable ne définit `in_app_updates = false`, le programme de mise à jour
intégré à l’application reprend son fonctionnement normal. Si l’indicateur **Géré**
s’affiche toujours, examinez les autres stratégies de l’espace de travail, les profils MDM et les fichiers du système nommés
`requirements.toml`. Consultez
[Emplacements et ordre de priorité](/fr-FR/codex/enterprise/managed-configuration#locations-and-precedence)
pour connaître l’ordre d’application des sources gérées.

## Comprendre les responsabilités relatives à la sécurité et à la prise en charge

Une fois reçue et appliquée par l’application, la stratégie de mise à jour gérée :

- Empêche l’application de bureau de rechercher, télécharger ou installer des mises à jour
à l’aide de son propre programme de mise à jour.
- Ne propose ni épinglage de version géré par OpenAI, ni canal de diffusion distinct,
ni garantie de compatibilité des anciennes versions avec le service.
- S’applique aux versions prises en charge de l’application de bureau ChatGPT pour macOS et Windows. Elle
ne gère pas les mises à jour des applications mobiles, de Codex CLI ni de l’extension IDE.

## Résoudre les problèmes courants

Si un problème d’authentification ou de connexion, ou un dépassement de délai, empêche l’application
de récupérer ou d’appliquer la stratégie gérée, son programme de mise à jour intégré peut
rester activé. Ne supposez pas que l’application bloque les mises à jour tant que **Géré** ne s’affiche pas.

Si l’indicateur **Géré** ne s’affiche pas, vérifiez les points suivants :

- L’utilisateur concerné a sélectionné l’espace de travail voulu.
- La stratégie cible cet utilisateur, ce groupe ou cette plateforme.
- L’appareil exécute une version prise en charge de l’application.
- L’application peut se connecter au service qui distribue les stratégies gérées.
- Le paramètre se trouve dans **requirements.toml**, et non dans **config.toml**.
- L’utilisateur a complètement quitté puis rouvert l’application après que vous avez enregistré la stratégie.

Si vous ne pouvez pas ouvrir Configuration gérée ou enregistrer une stratégie, vérifiez que vous disposez
d’un accès administrateur Codex pour l’espace de travail.

Si la version de l’application change après la désactivation des mises à jour intégrées, vérifiez si
Microsoft Store, Intune, MDM, un gestionnaire de paquets ou un autre système de déploiement
a installé la mise à jour. La stratégie contrôle uniquement le programme de mise à jour intégré à l’application.

## Documentation associée

- [Configuration gérée](/fr-FR/codex/enterprise/managed-configuration)
- [Déployer l’application Windows](/fr-FR/codex/enterprise/windows-deployment)
- [Référence de configuration de `requirements.toml`](/fr-FR/codex/config-file/config-reference#requirementstoml)
- [Guide de déploiement pour les administrateurs](/fr-FR/codex/enterprise/admin-setup)
