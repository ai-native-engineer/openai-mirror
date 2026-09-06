<!-- source: https://learn.chatgpt.com/fr-FR/docs/computer-use -->

Dans les régions prises en charge, la fonctionnalité Utilisation de l’ordinateur est disponible dans l’application de bureau ChatGPT sur
macOS et Windows avec ChatGPT Work et Codex. Installez le plugin Utilisation de l’ordinateur.
Sur macOS, accordez les autorisations Enregistrement de l’écran et Accessibilité lorsque
le système vous y invite.

Avec la fonctionnalité Utilisation de l’ordinateur, ChatGPT peut voir et utiliser des interfaces graphiques sur macOS
ou Windows. Utilisez-la pour les tâches où les outils en ligne de commande ou les intégrations structurées
ne suffisent pas, par exemple pour vérifier une application de bureau, utiliser un navigateur, modifier les
paramètres d’une application, exploiter une source de données qui n’est pas disponible sous forme de plugin ou
reproduire un bug qui ne se produit que dans une interface graphique.

Comme la fonctionnalité Utilisation de l’ordinateur peut modifier l’état des applications et du système en dehors de l’espace de travail de votre projet,
réservez-la à des tâches bien délimitées et examinez les demandes d’autorisation avant de
continuer.

## Configurez la fonctionnalité Utilisation de l’ordinateur

Dans l’application de bureau ChatGPT, sélectionnez ChatGPT et passez à Work dans le sélecteur, ou sélectionnez
Codex. Ouvrez **Plugins \> Utilisation de
l’ordinateur** et sélectionnez **Installer le plugin** si vous y êtes invité. Si ChatGPT affiche **Activer**,
sélectionnez cette option. Activez les interrupteurs du serveur et du skill Utilisation de l’ordinateur, puis sélectionnez **Essayer
maintenant** pour commencer.

  

Ouvrez ensuite **Paramètres \> Utilisation de l’ordinateur** pour vérifier l’accès aux applications. Les contrôles du navigateur
connecté affichent l’action **Gérer** . Les applications que vous autorisez pour les tâches futures apparaissent dans
la section **Applications toujours autorisées** .

  

Sur Windows, laissez l’application cible visible sur le bureau actif pendant l’exécution de la
tâche. Sur macOS, accordez les autorisations Enregistrement de l’écran et Accessibilité lorsque
le système vous y invite afin que ChatGPT puisse voir l’application cible et interagir avec elle.

Sur macOS, accordez :

- l’autorisation **Enregistrement de l’écran** pour que ChatGPT puisse voir l’application cible.
- l’autorisation **Accessibilité** pour que ChatGPT puisse cliquer, saisir du texte et naviguer.

## Quand utiliser la fonctionnalité Utilisation de l’ordinateur

Pour les tâches difficiles qui reposent sur des captures d’écran ou une appréciation visuelle, choisissez
[GPT-6 Astra](/fr-FR/codex/models#gpt-6-astra) lorsqu’il est disponible dans votre sélecteur de
modèles. La configuration du plugin, les autorisations du système d’exploitation et les contrôles d’accès
aux applications restent les mêmes.

Choisissez la fonctionnalité Utilisation de l’ordinateur lorsque la tâche dépend d’une interface graphique qu’il est
difficile de vérifier uniquement à partir de fichiers ou de sorties de commande.

Cette fonctionnalité convient notamment aux cas suivants :

- Tester une application macOS, une application Windows, un parcours dans le simulateur iOS ou une autre application de bureau
que ChatGPT développe.
- Effectuer une tâche nécessitant votre navigateur web.
- Reproduire un bug qui ne se manifeste que dans une interface graphique.
- Modifier des paramètres d’application qui nécessitent de cliquer dans une interface utilisateur.
- Examiner des informations dans une application ou une source de données qui n’est pas accessible via un
plugin.
- Sur macOS, exécuter en arrière-plan une tâche bien délimitée pendant que vous continuez à travailler
ailleurs.
- Exécuter un workflow faisant intervenir plusieurs applications.

Pour les applications web que vous développez localement, utilisez d’abord le
[navigateur intégré](/fr-FR/codex/browser?surface=app).

### Utilisation au premier plan sur Windows

Sur Windows, la fonctionnalité Utilisation de l’ordinateur s’exécute sur le bureau actif. Elle ne peut pas fonctionner en
arrière-plan pendant que vous continuez à utiliser la même session Windows. Attendez-vous donc à ce que ChatGPT
déplace le pointeur, saisisse du texte et prenne le contrôle au premier plan pendant l’exécution de la tâche.

Pour que les tâches Windows puissent continuer pendant votre absence, laissez l’appareil Windows
déverrouillé et connecté à Internet. Utilisez le
[contrôle à distance](/fr-FR/codex/remote-connections) depuis votre téléphone pour vérifier la progression
ou envoyer des instructions complémentaires, ou exécutez l’application de bureau ChatGPT dans une machine virtuelle
Windows afin que la fonctionnalité Utilisation de l’ordinateur prenne le contrôle de la VM plutôt que de votre bureau principal.

## Démarrez une tâche avec la fonctionnalité Utilisation de l’ordinateur

Mentionnez `@Computer` ou `@AppName` dans votre prompt, ou demandez à ChatGPT d’utiliser la fonctionnalité Utilisation de
l’ordinateur. Indiquez précisément l’application, la fenêtre ou le parcours que ChatGPT doit contrôler.

```text
Open the app with Computer Use, reproduce the onboarding bug, and fix the
smallest code path that causes it. After each change, run the same UI flow
again.

```text
Open @Chrome and verify the checkout page still works after the latest changes.

Si l’application cible propose un plugin ou un serveur MCP dédié, privilégiez cette
intégration structurée pour accéder aux données et effectuer des opérations reproductibles. Choisissez
la fonctionnalité Utilisation de l’ordinateur lorsque ChatGPT doit examiner ou manipuler visuellement l’application.

## Autorisations et approbations

Les administrateurs de l’espace de travail peuvent limiter les applications accessibles à la fonctionnalité Utilisation de l’ordinateur et
déterminer si les approbations peuvent être enregistrées. Consultez les
[contrôles administrés du navigateur et de la fonctionnalité Utilisation de l’ordinateur](/fr-FR/codex/enterprise/managed-configuration#control-browser-and-computer-use).

Les autorisations système de la fonctionnalité Utilisation de l’ordinateur sont distinctes des approbations d’applications dans ChatGPT.
Sur macOS, les autorisations Enregistrement de l’écran et Accessibilité permettent à ChatGPT de voir et de
contrôler les applications. Les approbations déterminent les applications que vous autorisez ChatGPT à utiliser. La
lecture et la modification de fichiers ainsi que les commandes shell restent soumises aux paramètres de bac à sable et d’approbation
de la tâche.

Avec la fonctionnalité Utilisation de l’ordinateur, ChatGPT ne peut voir et agir que dans les applications que vous autorisez.
Pendant une tâche, ChatGPT vous demande votre autorisation avant de pouvoir utiliser une application sur votre
ordinateur. Vous pouvez choisir **Toujours autoriser** pour que ChatGPT puisse utiliser cette application à l’avenir
sans vous le redemander. Vous pouvez retirer des applications de la liste **Toujours autoriser** dans la
section **Utilisation de l’ordinateur** des paramètres de l’application de bureau ChatGPT.

  
    
  

ChatGPT peut également demander votre autorisation avant d’effectuer des actions sensibles ou perturbatrices.

Si ChatGPT ne peut pas voir ou contrôler une application, ouvrez **Réglages Système \> Confidentialité et
sécurité** et vérifiez les autorisations **Enregistrement de l’écran** et **Accessibilité** pour **Utilisation de l’ordinateur
de Codex** sur macOS. Sur Windows, assurez-vous que l’application cible est visible dans la
session de bureau active.

Sur Windows, la fonctionnalité Utilisation de l’ordinateur conserve les décisions relatives aux applications dans
`$CODEX_HOME/config.toml`. Répertoriez les applications qu’elle peut ouvrir sans
demander d’autorisation :

```toml
[computer_use.windows]
always_allowed_app_ids = ["mspaint.exe"]

Utilisez l’identifiant d’application indiqué par la fonctionnalité Utilisation de l’ordinateur sur Windows, par exemple le nom
de l’exécutable d’une application de bureau ou un ID de modèle utilisateur d’application pour une application empaquetée. ChatGPT
demande une autorisation pour les applications absentes de la liste. Pour révoquer une décision enregistrée, retirez
l’application de **Paramètres \> Utilisation de l’ordinateur \> Toujours autoriser**.

Cette table consigne les décisions locales relatives à la fonctionnalité Utilisation de l’ordinateur. Elle est distincte du fichier
`requirements.toml` imposé par les administrateurs, dans lequel ceux-ci peuvent désactiver la fonctionnalité Utilisation de
l’ordinateur avec `[features].computer_use = false`. Les anciennes entrées de la liste d’autorisation de
`$CODEX_HOME/computer-use/config.toml` sont migrées vers le paramètre
actuel ; la liste `denied` de cet ancien fichier ne fait pas partie du schéma de stratégie actuel.

## Utilisation avec écran verrouillé

  L’utilisation avec écran verrouillé est réservée à macOS. Sur Windows, la fonctionnalité Utilisation de l’ordinateur fonctionne au premier plan.

L’utilisation avec écran verrouillé permet à ChatGPT de recourir à la fonctionnalité Utilisation de l’ordinateur après le verrouillage de votre Mac, mais seulement si
vous l’avez activée. Utilisez-la lorsqu’une tâche ChatGPT doit utiliser des applications de bureau depuis un
appareil connecté après le verrouillage du Mac.

Lorsque vous activez l’utilisation avec écran verrouillé, ChatGPT installe un
[module d’autorisation](https://developer.apple.com/documentation/security/authorization-plug-ins) Apple
qui intervient dans le processus de déverrouillage de macOS.

L’utilisation avec écran verrouillé est volontairement limitée. Elle ne constitue pas un moyen général de déverrouiller
votre Mac à distance et ne permet pas à d’autres applications ou processus locaux de déverrouiller
l’ordinateur.

Pour utiliser cette fonctionnalité avec l’écran verrouillé :

1. Dans l’application, ouvrez **Paramètres \> Utilisation de l’ordinateur** .
2. Activez l’utilisation avec écran verrouillé.
3. Après le verrouillage de l’écran de votre Mac, lancez depuis un appareil connecté une tâche qui utilise la fonctionnalité Utilisation de
l’ordinateur.

Lorsqu’une tâche ChatGPT accède à une application via la fonctionnalité Utilisation de l’ordinateur après le verrouillage de votre Mac, ChatGPT
déverrouille temporairement le Mac tout en bloquant l’utilisation locale et en préservant les protections de l’écran
verrouillé. Avant le déverrouillage, ChatGPT vérifie que la tentative concerne
une interaction active et reconnue comme fiable avec la fonctionnalité Utilisation de l’ordinateur. En dehors de cette courte fenêtre, ChatGPT
refuse le déverrouillage et vous demande de déverrouiller le Mac manuellement si nécessaire.

L’utilisation avec écran verrouillé comprend les mesures de protection suivantes :

- La fenêtre d’autorisation est de courte durée et limitée à la tentative de déverrouillage
en cours.
- Le déverrouillage automatique est réservé à ChatGPT pendant les interactions actives avec la fonctionnalité Utilisation de l’ordinateur.
- ChatGPT masque tous les écrans pendant que le bureau est temporairement déverrouillé.
- Si ChatGPT détecte une interaction locale au clavier ou avec le pointeur, il reverrouille le Mac et
suspend le déverrouillage automatique jusqu’à ce que vous le déverrouilliez manuellement.

## Consignes de sécurité

Avec la fonctionnalité Utilisation de l’ordinateur, ChatGPT peut voir le contenu de l’écran, prendre des captures d’écran et interagir
avec les fenêtres, les menus, la saisie au clavier et l’état du presse-papiers dans l’application cible.
Considérez que le contenu visible des applications, les pages du navigateur, les captures d’écran et les fichiers ouverts dans
l’application cible font partie du contexte que ChatGPT peut traiter pendant l’exécution de la tâche.

Limitez la portée des tâches et restez présent pendant les opérations sensibles :

- Indiquez à ChatGPT une seule application cible ou un seul parcours clairement défini à la fois.
- Vous pouvez arrêter la tâche ou reprendre le contrôle de votre ordinateur à tout moment.
- Gardez les applications sensibles fermées, sauf si elles sont nécessaires à la tâche.
- Sur Windows, attendez-vous à ce que ChatGPT prenne le contrôle des interactions au premier plan pendant qu’il travaille ; utilisez un appareil secondaire, une machine virtuelle ou arrêtez la tâche avant d’utiliser vous-même ce bureau.
- Évitez les tâches qui nécessitent des secrets, sauf si vous êtes présent et pouvez approuver chaque étape.
- Examinez les demandes d’autorisation des applications avant d’autoriser ChatGPT à utiliser une application.
- Utilisez **Toujours autoriser** uniquement pour les applications dont vous autorisez en toute confiance l’utilisation automatique par ChatGPT lors de
  futures tâches.
- Restez présent lorsque la tâche concerne des paramètres liés aux comptes, à la sécurité, à la confidentialité, au réseau, aux paiements ou aux informations d’identification.
- Annulez la tâche si ChatGPT commence à interagir avec la mauvaise fenêtre.

Si ChatGPT utilise votre navigateur, il peut interagir avec des pages sur lesquelles vous êtes déjà connecté. Examinez les actions sur les sites web comme si vous les effectuiez vous-même : les pages web peuvent contenir des contenus malveillants ou trompeurs, et les sites peuvent attribuer à votre compte les clics approuvés, les formulaires envoyés et les actions effectuées après connexion. Pour continuer à utiliser votre navigateur pendant que ChatGPT travaille, demandez-lui d’en utiliser un autre.

Cette fonctionnalité ne peut pas automatiser les applications de terminal ni ChatGPT lui-même, car leur automatisation pourrait contourner les politiques de sécurité de ChatGPT. Elle ne peut pas non plus s’authentifier en tant qu’administrateur ni approuver les demandes d’autorisation relatives à la sécurité et à la confidentialité sur votre ordinateur.

Les modifications de fichiers et les commandes shell restent soumises aux paramètres d’approbation et de bac à sable de ChatGPT lorsqu’ils s’appliquent. Les modifications effectuées dans des applications de bureau peuvent n’apparaître dans le volet de révision qu’après avoir été enregistrées sur le disque et suivies dans le projet. Vos paramètres de contrôle des données ChatGPT s’appliquent au contenu traité par ChatGPT, y compris aux captures d’écran réalisées avec Utilisation de l’ordinateur.
