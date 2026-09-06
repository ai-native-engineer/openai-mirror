<!-- source: https://learn.chatgpt.com/fr-FR/docs/browser -->

Le navigateur n’est disponible ni dans Codex CLI ni dans l’extension IDE Codex. Ouvrez
l’application de bureau ChatGPT pour utiliser le navigateur intégré.

Le navigateur permet à ChatGPT d’ouvrir des sites web, de recueillir des informations à jour et d’agir,
tandis que vous gardez le contrôle. Utilisez-le pour comparer des options, effectuer une tâche en plusieurs étapes
sur un site web ou examiner une page que vous développez.

Le navigateur est disponible dans ChatGPT sur le web et dans l’application de bureau ChatGPT.

[GPT-6 Astra](/fr-FR/codex/models#gpt-6-astra) améliore l’évaluation visuelle pour des tâches telles que
la comparaison d’une page avec une capture d’écran ou l’exécution d’un workflow sur plusieurs sites.
Choisissez-le lorsqu’il est disponible dans votre sélecteur de modèle et décrivez comment vérifier
le résultat final.

Dans les environnements de bureau gérés, les administrateurs peuvent restreindre les origines accessibles au navigateur,
les envois de fichiers, les téléchargements et l’accès développeur. Consultez les
[contrôles de gestion du navigateur](/fr-FR/codex/enterprise/managed-configuration#control-browser-and-computer-use).

Considérez le contenu des pages comme un contexte non fiable. Examinez le site et l’action proposée
avant de communiquer des informations sensibles ou d’autoriser ChatGPT à agir.

Dans l’application de bureau ChatGPT, le navigateur intégré vous offre, ainsi qu’à ChatGPT, une vue partagée
des sites web et des applications web locales au sein d’une discussion. Utilisez-le pour prévisualiser une page,
laisser des commentaires visuels ou permettre à ChatGPT d’interagir avec un site en votre nom.

Le navigateur intégré utilise un profil distinct de celui de votre navigateur
habituel. Il ne partage pas automatiquement vos onglets existants ni votre session de navigation.
Vous pouvez vous connecter directement lorsqu’une tâche nécessite un compte. Ouvrez **Paramètres \>
Navigateur** pour gérer les données du navigateur et les éventuelles fonctionnalités d’importation de profil disponibles sur
votre appareil.

Par défaut, les téléchargements du navigateur sont enregistrés dans le dossier Téléchargements de votre système. Dans **Paramètres \>
Navigateur**, vous pouvez choisir un autre emplacement de téléchargement, rétablir l’emplacement par défaut du système
ou activer **Demander où enregistrer les téléchargements**.

Utilisez plutôt l’[extension de navigateur](/fr-FR/codex/chrome-extension) lorsque ChatGPT doit
travailler dans un onglet existant de Chrome, Edge, Brave, Opera ou Vivaldi, ou utiliser le profil de
votre navigateur habituel.

Ouvrez le navigateur intégré depuis la barre d’outils, en cliquant sur une URL, en naviguant
manuellement ou en appuyant sur <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>B</kbd>
(<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>B</kbd> sur Windows).

  
    
  

## Recherchez depuis la barre d’adresse

Commencez à saisir du texte dans la barre d’adresse du navigateur intégré pour retrouver des pages dans son
historique de navigation. Sélectionnez une page correspondante pour la rouvrir, ou saisissez un terme de recherche
pour effectuer une recherche sur Google si aucun résultat de l’historique ne correspond.

Le navigateur intégré conserve son propre profil et son propre historique de navigation. Les résultats
n’incluent pas automatiquement les pages de votre profil Chrome habituel ni celles d’autres navigateurs.

## Gérez l’historique de navigation

Ouvrez **Paramètres \> Navigateur** pour effectuer une recherche dans l’historique du navigateur intégré, rouvrir une
page consultée ou supprimer des entrées de l’historique lorsque votre organisation l’autorise. Utilisez
**Effacer les données de navigation** pour choisir une période et les types de données de navigation
à supprimer.

Lorsque cette fonctionnalité est disponible, ChatGPT peut vous demander l’autorisation de rechercher dans votre historique de navigation une page
utile à la tâche en cours. Examinez la demande avant d’autoriser l’accès.
L’historique de navigation peut contenir des URL internes, des termes de recherche et d’autres informations
sensibles. N’autorisez donc cet accès que si la tâche nécessite ce contexte.

<a id="browser-use"></a>

## Utilisation de l’ordinateur dans le navigateur

Dans l’application de bureau, la fonctionnalité Utilisation de l’ordinateur permet à ChatGPT Work ou à Codex de contrôler directement le
navigateur intégré. L’outil choisi peut ouvrir des pages, cliquer, saisir du texte,
inspecter l’état affiché, effectuer des captures d’écran et vérifier le résultat de son travail sur
la page.

Le navigateur est inclus dans l’application de bureau et s’installe automatiquement. Demandez à ChatGPT
ou à Codex d’utiliser le navigateur intégré pour votre tâche, ou mentionnez-le directement avec
`@Browser`.

Par exemple :

```text
Use the browser to open http://localhost:3000/settings, reproduce the layout
bug, and fix only the overflowing controls.

ChatGPT demande votre autorisation avant d’utiliser un site web, sauf si vous avez déjà autorisé
ce site. Gérez les sites autorisés et bloqués dans **Paramètres \> Navigateur**. ChatGPT demande également
votre confirmation avant les actions sensibles, telles que l’envoi d’informations,
un achat, la modification d’autorisations ou la suppression de données. ChatGPT ne peut pas
automatiser l’envoi de fichiers dans le navigateur intégré.

  Les instructions d’une page peuvent être trompeuses ou malveillantes. Une autorisation d’accès à un site web
permet à ChatGPT d’interagir avec ce site ; elle ne rend pas son contenu
fiable et ne vaut pas approbation de toutes les actions.

## Prévisualisez une page

1. Démarrez le serveur de développement de votre application dans le [terminal intégré](/fr-FR/codex/integrated-terminal) ou à l’aide d’une [action de l’environnement local](/fr-FR/codex/environments/local-environment#actions).
2. Ouvrez la route locale, la page servie depuis un fichier ou la page publique en cliquant sur une URL ou
en accédant manuellement à son adresse dans le navigateur.
3. Examinez l’état affiché en parallèle du diff de code.
4. Ajoutez des commentaires dans le navigateur sur les éléments ou les zones à modifier.
5. Demandez à ChatGPT de traiter les commentaires en limitant la portée de la tâche.

Par exemple :

```text
I left comments on the pricing page in the built-in browser. Address the mobile
layout issues and keep the card structure unchanged.

## Commentez la page

Lorsqu’un bug n’est visible que dans le rendu de la page, utilisez les commentaires du navigateur pour fournir à
ChatGPT des indications précises.

1. Activez le **mode d’annotation**.
2. Cliquez sur un élément ou faites glisser le pointeur pour sélectionner une zone.
3. Rédigez et enregistrez votre commentaire.
4. Envoyez dans la discussion un message demandant à ChatGPT de traiter les commentaires.

Les commentaires sont plus efficaces si vous indiquez le problème et le résultat souhaité :

```text
This button overflows on mobile. Keep the label on one line if it fits,
otherwise wrap it without changing the card height.

```text
This tooltip covers the data point under the cursor. Reposition the tooltip so
it stays inside the chart bounds.

<section class="feature-grid">

<div>

### Commentaires sur le style

Lorsque vous ajoutez une annotation à une section de la page, sélectionnez **Ajuster** à côté du champ de saisie
pour transmettre à ChatGPT des indications plus précises sur le style. Vous pouvez modifier
des valeurs telles que la police, le texte, l’espacement et la couleur, prévisualiser le résultat sur la page,
puis envoyer l’annotation avec un objectif mieux défini.

</div>

  
    
  

</section>

## Limitez la portée des tâches dans le navigateur

Limitez la portée de chaque tâche dans le navigateur pour pouvoir l’examiner en une seule fois.

- Indiquez la page, la route ou l’URL concernée.
- Précisez l’état qui vous intéresse, par exemple : chargement, état vide, erreur ou réussite.
- Laissez des commentaires précisément sur les éléments ou les zones à modifier.
- Examinez de nouveau la page une fois que ChatGPT a terminé.
- Demandez à ChatGPT de démarrer ou de vérifier le serveur de développement avant qu’il n’ouvre une page
locale.

Pour les modifications apportées au dépôt, utilisez le [volet de révision](/fr-FR/codex/code-review?surface=app) afin
d’examiner les modifications et de laisser des commentaires.

<section class="feature-grid">

<div>

## Mode développeur

Le mode développeur fonctionne avec la fonctionnalité Utilisation de l’ordinateur dans Chrome et dans le navigateur intégré. Il
donne à ChatGPT un accès contrôlé au Chrome DevTools Protocol (CDP). Utilisez-le pour
profiler du code JavaScript, inspecter la sortie de la console et le trafic réseau, examiner le DOM
et les styles appliqués, ou diagnostiquer un problème directement dans le navigateur.

Pour l’activer, ouvrez [**Paramètres \> Navigateur**](codex://settings/browser-use) puis,
dans la section **Mode développeur**, activez l’option **Activer l’accès complet au CDP**. Si votre
organisation a désactivé ce paramètre, vous ne pouvez pas l’activer localement. Les administrateurs peuvent
définir `browser_use_full_cdp_access = false` dans la section `[features]` du fichier
[`requirements.toml`](/fr-FR/codex/enterprise/managed-configuration#pin-feature-flags)
pour désactiver l’accès complet au CDP et empêcher les utilisateurs d’activer le paramètre
correspondant dans l’application de bureau ChatGPT.

L’accès complet au CDP peut exposer des éléments internes sensibles du navigateur. ChatGPT demande une
approbation explicite avant d’utiliser l’accès complet au CDP pour inspecter un site web. Examinez le
site, la tâche et l’accès demandé avant de donner votre approbation.

Utilisez `@Browser` pour le navigateur intégré. Pour utiliser le mode développeur dans Chrome,
[configurez l’extension Chrome](/fr-FR/codex/chrome-extension) et invoquez `@Chrome`.

Par exemple :

```text
This app is slow. Use @Browser to capture a performance trace and inspect
network traffic, then identify the bottleneck.

</div>

  
    
  

</section>

## Utilisez ChatGPT Work pour accomplir des tâches sur le web

ChatGPT Work peut accomplir des tâches sur différents sites web, y compris ceux auxquels vous devez vous connecter.

Work utilise son propre navigateur, exécuté sur un ordinateur distinct dans le cloud, et non celui de votre téléphone ou de votre ordinateur portable.

Démarrez une tâche dans ChatGPT Work sur le web ou sur mobile, et ChatGPT pourra continuer à travailler même si vous vous absentez et fermez votre ordinateur. Grâce à son ordinateur, Work peut accomplir des tâches très variées sur Internet en lisant des pages web, en cliquant et en y saisissant du texte. Selon votre demande, il peut utiliser un plugin, son navigateur ou les deux.

Par exemple, ChatGPT peut vous aider à :

- Trouver un créneau et prendre rendez-vous au DMV.
- Vous connecter à votre compte auprès de votre fournisseur de services publics et comparer les offres.
- Trouver des appartements qui correspondent à vos critères et les enregistrer.
- Faire des recherches sur vos concurrents sur les réseaux sociaux.
- Clôturer les comptes dans votre logiciel comptable.

Vous contrôlez les sites web auxquels ChatGPT peut accéder. Il est entraîné à demander votre confirmation avant d’effectuer des actions aux conséquences importantes, comme finaliser une réservation ou un paiement. Si ChatGPT se retrouve bloqué pour une raison quelconque, vous pouvez prendre le contrôle de son ordinateur et l’utiliser vous-même, sur mobile comme sur ordinateur.

L’accès aux sites web nécessitant une authentification est disponible dans ChatGPT Work sur le web et sur mobile avec les offres Plus et Pro.

La disponibilité dépend du déploiement. La connexion aux sites web n’est pas disponible pour les espaces de travail Entreprise ou Edu.

## Fonctionnement de l’ordinateur de ChatGPT Work

Lorsque votre tâche nécessite un site web, ChatGPT utilise son propre navigateur pour parcourir les pages, recueillir des informations et effectuer les étapes en ligne.

Par défaut, ChatGPT vous demande votre accord avant d’accéder à un nouveau site web. Vous pouvez approuver chaque demande individuellement ou modifier vos paramètres pour laisser ChatGPT approuver automatiquement l’accès aux sites web pertinents pour votre tâche. ChatGPT Work vous demandera toujours confirmation avant d’effectuer des actions aux conséquences importantes, comme transmettre vos informations pour prendre rendez-vous ou effectuer un paiement.

## Connectez-vous à un site web

Si un site web exige une connexion, ChatGPT Work vous demandera de vous connecter. Une fois l’authentification effectuée, il poursuivra son travail sur le site avec votre session ouverte. Votre session restera active pour les prochaines tâches, ce qui vous évitera de vous reconnecter à chaque fois.

### Utilisez le formulaire de connexion sécurisé

ChatGPT ne peut pas voir votre nom d’utilisateur ni votre mot de passe. Ils ne sont jamais visibles par le modèle ni utilisés pour son entraînement. ChatGPT ne conserve ni votre nom d’utilisateur ni vos mots de passe. Vous pouvez à tout moment supprimer votre historique de navigation pour tous les sites ou pour un site en particulier depuis **Paramètres** \> **Navigateur cloud** \> **Données du navigateur**, ce qui vous déconnectera du site concerné.

Lorsqu’un écran de connexion s’affiche, ChatGPT met la tâche en pause et vous demande de saisir vos identifiants et, si nécessaire, vos codes d’authentification à deux facteurs. Sur iOS, vous pouvez utiliser un gestionnaire de mots de passe compatible pour vous connecter facilement.

Utilisez le formulaire de connexion fourni par ChatGPT. N’envoyez pas de mots de passe dans la discussion.

![ChatGPT Work sur iOS met en pause une tâche liée au DMV et affiche un formulaire de connexion sécurisé avec l’adresse du site web et un mot de passe masqué.](/images/codex/cloud-browser-auth/sign-in.webp)

### Connectez-vous sur la page web

Si cette option est proposée, sélectionnez **Se connecter plutôt sur la page web** pour vous connecter directement dans le navigateur cloud. La tâche est mise en pause pendant que vous vous connectez. Sélectionnez **J’ai terminé** pour redonner le contrôle à ChatGPT, ou ignorez ou annulez la demande.

<a id="start-a-browser-task"></a>
<a id="start-browser-work"></a>
<a id="web-start-browser-work"></a>

## Démarrez une tâche dans ChatGPT Work

1. Ouvrez ChatGPT sur le web ou sur mobile et démarrez une tâche dans Work.
2. Décrivez ce que vous souhaitez que ChatGPT fasse.
3. Approuvez l’accès au site web si cela vous est demandé.
4. Connectez-vous directement si un site web l’exige.
5. Suivez la progression de la tâche dans la conversation.
6. Vérifiez le résultat et approuvez les éventuelles actions aux conséquences importantes.

Vous n’avez pas besoin de sélectionner le navigateur séparément. ChatGPT décide quand l’utiliser en fonction de votre demande.

Certains sites web bloquent l’accès. Dans ce cas, ChatGPT vous en informera et, si possible, essaiera une autre méthode pour accomplir la tâche.

<a id="website-permissions-and-confirmations"></a>
<a id="web-website-permissions-and-confirmations"></a>

## Sécurité et options de contrôle pour l’utilisateur

Dans les paramètres de ChatGPT, ouvrez **Navigateur cloud** pour gérer les autorisations d’accès aux sites web. Vous disposez notamment des options suivantes :

- **Toujours demander** : Examinez manuellement chaque demande d’accès à un site web.
- **Approuver automatiquement** : Laissez ChatGPT approuver automatiquement l’accès une fois qu’il a vérifié que le site web est pertinent pour votre tâche.
- **Toujours autoriser** : Autorisez l’accès aux sites web sans cette étape de vérification supplémentaire. Nous proposons cette option pour simplifier l’utilisation au maximum, mais nous ne la recommandons pas.

![Paramètres du navigateur cloud présentant les options d’autorisation d’accès aux sites web Toujours demander, Approuver automatiquement et Toujours autoriser.](/images/codex/cloud-browser-auth/website-permissions.webp)

Vous pouvez également autoriser ou bloquer des sites web individuellement afin de définir des exceptions à vos autorisations par défaut.

Avant que ChatGPT vous demande de vous connecter à un site web, un modèle de vérification supplémentaire examine la demande de connexion et l’endroit où vos informations seront saisies pour détecter d’éventuels signes d’hameçonnage ou de tromperie. Nous testons l’agent face à des risques tels que les attaques par injection de prompt, l’hameçonnage et les actions involontaires.

Pour vous offrir une transparence totale, l’adresse du site web et un aperçu de son formulaire de connexion s’affichent, et vous pouvez examiner le site en direct avant de continuer. Les identifiants saisis dans le formulaire de connexion sécurisé sont transmis directement au navigateur et ne sont pas visibles par le modèle.

<a id="browser-data"></a>
<a id="web-browser-data"></a>

## Confidentialité et données du navigateur

L’ordinateur de ChatGPT Work fonctionne indépendamment du navigateur de votre appareil. Il conserve ses propres cookies, données de navigation et sessions connectées. Les informations utilisées par ChatGPT pour accomplir une tâche sont soumises aux paramètres de contrôle des données que vous choisissez dans ChatGPT. Vous pouvez consulter ces paramètres dans ChatGPT sur le web et sur mobile, sous **Paramètres** \> **Contrôles des données**.

Il n’utilise pas les onglets ouverts, l’historique de navigation, les mots de passe enregistrés, les cookies, les extensions ni les sessions déjà connectées de votre navigateur personnel.

Pour effacer les données du navigateur, accédez à **Paramètres** \> **Navigateur cloud** \> **Données du navigateur** \> **Tout effacer**. Cette action vous déconnecte des sites web dans le navigateur de ChatGPT Work ; vous devrez donc vous reconnecter pour les tâches à venir.

![Paramètres du navigateur cloud avec une section Données du navigateur et une option Cookies permettant de gérer les cookies enregistrés par le navigateur cloud.](/images/codex/cloud-browser-auth/browser-data.webp)

## Limitations

- La connexion aux sites web n’est pas disponible dans tous les espaces de travail ni à toutes les étapes du déploiement. Si une tâche nécessite une méthode de connexion qui n’est pas prise en charge, effectuez cette étape vous-même ou utilisez un autre outil disponible.
- Certains sites bloquent les navigateurs automatisés ou exigent un CAPTCHA. Il se peut que ChatGPT ne puisse pas y accomplir une tâche.
- La disponibilité de la navigation dans le cloud peut dépendre de votre offre, des paramètres de votre espace de travail et du déploiement. La navigation dans le cloud est disponible dans toutes les régions avec les offres payantes, à l’exception de Free et Go. Les administrateurs Entreprise doivent activer la navigation dans le cloud pour leur espace de travail.

Pendant le déploiement, le navigateur peut ne pas apparaître immédiatement, même si votre offre le prend en charge.
