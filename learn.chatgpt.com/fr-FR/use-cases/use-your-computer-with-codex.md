<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/use-your-computer-with-codex -->

## Introduction

Utilisez [Utilisation de l’ordinateur](/fr-FR/docs/computer-use) lorsqu’une tâche nécessite de passer par plusieurs applications de bureau, fenêtres ou fichiers locaux. ChatGPT peut cliquer, saisir du texte et naviguer dans les applications auxquelles vous lui donnez accès, puis vous présenter le résultat pour que vous puissiez l’examiner. Pour un site web ou une session de navigateur où vous êtes connecté, lancez une tâche de navigation distincte avec `@Chrome`.

**La fonctionnalité Utilisation de l’ordinateur nécessite l’application de bureau ChatGPT.** Dans les régions prises en charge, Utilisation de l’ordinateur est disponible sur macOS et Windows dans ChatGPT Work et Codex. Les tâches Work exécutées dans le cloud sur le Web ou sur mobile ne peuvent pas accéder directement à vos applications et fichiers locaux ni aux sessions ouvertes dans votre navigateur de bureau. Vous pouvez lancer ou piloter une tâche de bureau depuis [À distance sur mobile](/fr-FR/codex/remote-connections) lorsque vous connectez un hôte Mac ou Windows.

Par exemple, vous pouvez transférer des notes dans un système de référence, consulter des informations dans quelques applications avant de rédiger une réponse ou copier des données approuvées entre des outils dépourvus de plugin dédié.

Voici un exemple de délégation sécurisée d’une tâche de bureau lorsque vos projets de week-end dans un chalet se trouvent dans Messages et Notes :

<div data-use-case-export-only>

**Tâche de bureau :** Rassemblez des idées pour un week-end dans un chalet à partir de Messages et d’une sélection dans Notes, créez une note locale et rédigez un brouillon de réponse.

**Résultat :** Pine Lodge est accessible sans marches, se trouve à moins de deux heures et coûte 690 $ au total. Lake House pourrait convenir, mais il faut encore confirmer le temps de trajet et l’accessibilité. Cedar Ridge est exclu en raison de ses escaliers. Le nombre de participants est inconnu, le tarif par personne reste donc conditionnel.

La note locale et le brouillon de réponse sont prêts à être examinés. Aucune réservation n’a été effectuée et rien n’a été envoyé.

</div>

## Comment l’utiliser

1. Ouvrez l’application de bureau ChatGPT et installez le [plugin Utilisation de l’ordinateur](/fr-FR/docs/computer-use).
2. Commencez votre demande par `@Computer` pour les applications de bureau ou par `@Chrome` pour les tâches dans le navigateur.
3. Décrivez la tâche, les applications ou fichiers concernés et le résultat souhaité.
4. Examinez les demandes d’accès et mettez la tâche en pause avant toute action consistant à envoyer ou soumettre des informations, ou à modifier des données importantes.
5. Sur Windows, gardez l’application cible visible pendant l’exécution de la fonctionnalité Utilisation de l’ordinateur.

Si une application dispose d’un plugin, ChatGPT peut l’utiliser pour exécuter l’action structurée. La fonctionnalité Utilisation de l’ordinateur est utile lorsque la tâche dépend de l’interface de l’application ou qu’aucun plugin n’est disponible.

## À essayer

Commencez par un seul outil : utilisez `@Computer` pour les applications de bureau et les fichiers locaux, ou `@Chrome` pour votre navigateur. ChatGPT peut sélectionner d’autres outils si nécessaire.

**Transformez des messages en plan**

**Trouvez un hébergement**

**Faites le point sur un projet**

**Mettez à jour un outil de suivi à partir de notes de réunion**

**Travaillez dans le navigateur où vous êtes connecté**

**Testez un site web**

**Mettez de l’ordre dans les fichiers locaux**

**Montrez-lui ce que vous avez à l’écran**

Sur macOS, utilisez un [appshot](/fr-FR/codex/appshots) pour partager la fenêtre d’application au premier plan. Les Appshots fournissent un contexte visuel ; la fonctionnalité Utilisation de l’ordinateur peut ensuite ouvrir et examiner l’application, puis interagir avec elle si vous l’y autorisez.

## Conseils pratiques

### Comprenez comment la tâche s’exécute sur chaque ordinateur

Sur macOS, l’Utilisation de l’ordinateur peut s’exécuter en arrière-plan pendant que vous utilisez d’autres applications. Un aperçu en incrustation affiche l’application active ; ouvrez-le pour suivre la tâche ou déplacez-le pour qu’il ne vous gêne pas. Si vous utilisez un compagnon, vous pouvez y placer l’aperçu.

Sur Windows, l’Utilisation de l’ordinateur s’exécute sur le bureau actif et prend le contrôle au premier plan. Attendez-vous à ce que le pointeur se déplace et que des saisies soient effectuées au clavier pendant l’exécution de la tâche. Laissez l’appareil déverrouillé et connecté, ou exécutez l’application de bureau dans une machine virtuelle Windows si vous devez continuer à utiliser votre bureau principal.

### Choisissez le navigateur adapté

Les tâches effectuées dans le navigateur font souvent partie de l’Utilisation de l’ordinateur. Choisissez le navigateur qui offre le contexte dont vous avez besoin :

- **[Extension Chrome](/fr-FR/codex/chrome-extension) :** Utilisez `@Chrome` pour les tâches dans le navigateur, notamment pour rechercher des annonces, consulter des sites web ou accéder à votre profil Chrome existant auquel vous êtes connecté, à ses onglets ou à ses extensions.
- **[Navigateur intégré](/fr-FR/codex/browser?surface=app) :** Utilisez-le lorsque vous souhaitez disposer d’une session de navigation distincte pour localhost ou des sites publics. Il possède son propre état de navigation et peut patienter pendant que vous vous connectez.
- **Navigateur cloud de ChatGPT Work sur le web ou sur mobile :** Utilisez-le pour les sites publics compatibles accessibles sans connexion. Il ne peut ni accéder aux fichiers locaux, aux onglets ouverts, aux extensions ou aux mots de passe enregistrés, ni se connecter à des sites ou effectuer des paiements.

Lorsque le choix du navigateur est important, indiquez dans le prompt celui à utiliser et servez-vous de la [personnalisation](/fr-FR/docs/customization/overview) pour définir une préférence récurrente sur ordinateur.

### Évitez d’exécuter des tâches en parallèle dans la même application

N’exécutez pas simultanément deux tâches d’Utilisation de l’ordinateur dans la même application. Leurs actions concurrentes peuvent modifier la fenêtre ou l’état actuel et rendre le résultat peu fiable.

### Préparez les applications auxquelles vous êtes connecté et l’utilisation avec écran verrouillé

Avant de démarrer une tâche sur ordinateur, connectez-vous aux applications et aux services dont elle a besoin. Sur macOS, si l’[utilisation avec écran verrouillé](/fr-FR/docs/computer-use#locked-use) n’est pas activée, l’Utilisation de l’ordinateur s’arrête lorsque le Mac se verrouille ; son activation permet aux tâches compatibles de se poursuivre. Cette fonctionnalité n’est pas disponible pour l’Utilisation de l’ordinateur sous Windows.
