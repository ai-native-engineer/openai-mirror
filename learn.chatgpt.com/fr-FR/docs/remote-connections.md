<!-- source: https://learn.chatgpt.com/fr-FR/docs/remote-connections -->

Desktop,
  Storage,
  Terminal,
} from "@components/react/oai/platform/ui/Icon.react";

Les connexions distantes permettent d’accéder aux tâches en cours d’exécution sur un autre appareil ou une autre machine.
Dans l’application mobile ChatGPT, ouvrez **À distance** pour travailler dans des discussions ChatGPT ou Codex sur
un appareil Mac ou Windows connecté. Vous pouvez également poursuivre votre travail depuis un autre
appareil compatible exécutant l’application de bureau ChatGPT, ou connecter l’application à des projets
sur un hôte SSH.

L’accès à distance utilise les projets, les discussions, les fichiers, les identifiants,
les autorisations, les plugins, l’Utilisation de l’ordinateur, la configuration du navigateur et les outils locaux de l’hôte connecté.

## Ce que vous pouvez faire à distance

- Lancez de nouvelles discussions dans les projets de l’hôte ou poursuivez des discussions existantes.
- Envoyez des instructions complémentaires, répondez aux questions et orientez le travail en cours.
- Approuvez les commandes et les autres actions.
- Examinez les sorties, les diffs, les résultats des tests, la sortie du terminal et les captures d’écran.
- Recevez une notification lorsque ChatGPT termine une tâche ou requiert votre attention.
- Passez d’un hôte connecté à l’autre et d’une discussion à l’autre.

Les sections suivantes expliquent comment ouvrir **À distance** dans l’application mobile ChatGPT afin d’accéder à un
ordinateur hôte. Pour connecter Codex à un projet sur un hôte SSH, consultez
[Connexion à un hôte SSH](#connect-to-an-ssh-host).

<div class="not-prose my-6 max-w-4xl rounded-xl bg-[url('/images/codex/codex-wallpaper-1.webp')] bg-cover bg-center p-4 md:p-8">
  
    
      
    
  
</div>

<a id="before-you-set-up-mobile-access"></a>

## Avant de configurer la fonctionnalité À distance

  La fonctionnalité À distance prend en charge les hôtes exécutant l’application de bureau ChatGPT sur macOS et Windows.
  Vous pouvez contrôler un hôte depuis ChatGPT sur iOS ou Android, ou depuis un autre Mac ou un appareil
  Windows lorsque l’option **Contrôler d’autres appareils** est disponible. Sa disponibilité peut
  varier selon le déploiement.

Vérifiez que vous disposez des éléments suivants :

- Un accès à Codex dans le compte et l’espace de travail ChatGPT que vous souhaitez utiliser.
- La dernière version de l’application mobile ChatGPT sur un appareil iOS ou Android. Si **À distance**
  n’apparaît pas dans l’application, mettez d’abord ChatGPT à jour.
- La dernière version de l’application de bureau ChatGPT pour macOS ou Windows, exécutée sur un hôte actif,
en ligne et connecté au même compte et au même espace de travail. La configuration mobile commence
dans l’application ; vous ne pouvez pas l’effectuer depuis Codex CLI ni depuis l’extension IDE.
- Toute configuration requise d’authentification multifacteur, de SSO ou de clé d’accès pour
ce compte ou cet espace de travail.

Si vous utilisez Codex via un espace de travail ChatGPT, votre administrateur devra peut-être activer
l’accès au Contrôle à distance avant que vous puissiez vous connecter depuis votre téléphone.

<a id="set-up-mobile-access"></a>

## Configuration de la fonctionnalité À distance

Commencez dans l’application de bureau ChatGPT sur l’hôte que vous souhaitez connecter. Le parcours de configuration
active l’accès à distance pour cet hôte, puis affiche un code QR que vous pouvez scanner avec votre
téléphone.
Ce code QR associe ce téléphone à cet hôte. Associez chaque téléphone ou appareil compatible exécutant l’application
de bureau à chaque hôte que vous souhaitez lui permettre de contrôler.

  Les connexions existantes utilisées depuis le 8 juin 2026 restent associées. Si vous n’avez pas
utilisé une connexion existante depuis le 8 juin 2026, mettez les deux applications à jour et associez de nouveau les
appareils.

1. Lancez la configuration de la fonctionnalité À distance.

   Ouvrez l’application de bureau ChatGPT sur l’hôte. Accédez à **Paramètres** \>
**Connexions** \> **Contrôler ce Mac ou ce PC**, puis sélectionnez **Configurer** ou
**Ajouter**. Approuvez l’accès à distance et effectuez toutes les vérifications demandées.

2. Scannez le code QR.

   Utilisez votre téléphone pour scanner le code QR affiché par l’application. Ce code ouvre ChatGPT
pour vous permettre de terminer la connexion de l’application mobile à l’hôte.

3. Terminez la configuration dans ChatGPT.

   ChatGPT ouvre le parcours de configuration de la fonctionnalité À distance. Confirmez qu’il s’agit du même compte ChatGPT
et du même espace de travail, puis suivez toutes les étapes requises d’authentification multifacteur, de SSO
ou de clé d’accès. Une fois la configuration terminée, l’hôte apparaît dans la section À distance sur votre
téléphone.

4. Vérifiez les paramètres de l’hôte.

   Dans l’application exécutée sur l’hôte, utilisez **Paramètres** \> **Connexions** pour gérer les appareils
   connectés. Vous pouvez également choisir d’empêcher la mise en veille de l’ordinateur, d’activer
   l’Utilisation de l’ordinateur ou d’installer l’Extension Chrome.

  

## Choisissez ce que vous souhaitez connecter

Commencez par l’ordinateur portable ou de bureau sur lequel vous utilisez déjà ChatGPT. Ajoutez un ordinateur
toujours actif ou un hôte SSH lorsque vous avez besoin d’un accès continu ou d’un autre environnement.

### <span class="not-prose inline-flex items-center gap-3 align-middle"><span class="inline-flex h-7 w-7 shrink-0 items-center justify-center rounded-md bg-surface-secondary text-secondary"></span><span>Votre ordinateur portable ou de bureau</span></span>

Connectez le Mac ou le PC Windows sur lequel l’application de bureau est déjà installée. Vous
accédez ainsi à distance aux mêmes projets, discussions, identifiants, plugins et à la même
configuration locale que vous utilisez déjà.

Si cet ordinateur se met en veille, perd l’accès au réseau ou si l’application se ferme, l’accès à distance
est interrompu jusqu’à ce qu’il soit de nouveau disponible. Si vous utilisez cet ordinateur comme appareil hôte,
laissez-le branché et utilisez ses paramètres de connexion pour empêcher sa mise en veille lorsque cette option est
disponible.

Sur un ordinateur portable Mac, l’accès à distance peut rester disponible si le couvercle est ouvert et l’ordinateur
branché au secteur. Si le couvercle est fermé, branchez également un écran externe. L’option
**Suspendre l’activité** interrompt toutefois l’accès à distance.

Sur un hôte Windows, maintenez la session déverrouillée et disponible pour les tâches qui utilisent
[l’Utilisation de l’ordinateur](/fr-FR/codex/computer-use). Sous Windows, l’Utilisation de l’ordinateur s’exécute au
premier plan ; le contrôle à distance convient donc surtout pour lancer ou vérifier le travail pendant que vous
réservez le bureau de l’hôte à cette tâche.

### <span class="not-prose inline-flex items-center gap-3 align-middle"><span class="inline-flex h-7 w-7 shrink-0 items-center justify-center rounded-md bg-surface-secondary text-secondary"></span><span>Un ordinateur dédié toujours actif</span></span>

Utilisez un Mac ou un PC Windows dédié et toujours actif si vous souhaitez que ChatGPT reste
accessible pour les tâches de longue durée.

Installez sur cette machine les projets, les identifiants, les serveurs MCP, les Skills et les outils que ChatGPT ou
Codex doit utiliser.

### <span class="not-prose inline-flex items-center gap-3 align-middle"><span class="inline-flex h-7 w-7 shrink-0 items-center justify-center rounded-md bg-surface-secondary text-secondary"></span><span>Un environnement de développement distant</span></span>

Utilisez un hôte SSH ou un environnement de développement distant géré lorsque le projet
se trouve déjà dans un environnement distant. Connectez d’abord l’hôte qui exécute l’application de bureau à cet
environnement ; votre téléphone se connecte toujours au même hôte et ChatGPT travaille
dans l’environnement distant avec ses dépendances, ses politiques de sécurité et ses ressources
de calcul.

Pour plus de détails sur la configuration SSH, consultez [Connexion à un hôte SSH](#connect-to-an-ssh-host).

  Pour les tâches dans le navigateur ou sur le bureau d’un ordinateur toujours actif ou d’un hôte distant, activez
l’Utilisation de l’ordinateur et installez l’Extension Chrome sur cet hôte.

## Ce que fournit l’hôte connecté

Votre téléphone envoie à ChatGPT des prompts, des approbations et des messages de suivi. L’hôte
connecté fournit l’environnement utilisé par ChatGPT.

Cela signifie que :

- Les fichiers du dépôt et les documents locaux proviennent de l’hôte connecté.
- Les commandes shell s’exécutent sur cet hôte ou dans l’environnement distant.
- Les serveurs MCP, les Skills, l’accès au navigateur et l’Utilisation de l’ordinateur dépendent de la
configuration de cet hôte.
- Les sites web auxquels vous êtes connecté et les applications de bureau ne sont accessibles que si l’hôte peut
y accéder.
- Les paramètres du bac à sable, les contrôles de sécurité et les approbations d’actions continuent de s’appliquer
à la session connectée.

Une couche de relais sécurisée permet aux machines de confiance de rester accessibles depuis vos appareils
ChatGPT autorisés sans les exposer directement à l’Internet public.

## Reprenez votre travail depuis un autre appareil

Vous pouvez poursuivre votre travail depuis un autre appareil connecté à votre compte qui exécute l’application de bureau
ChatGPT et prend en charge le contrôle à distance. Par exemple, si votre ordinateur portable n’est pas disponible, vous pouvez
lancer une discussion depuis votre téléphone sur un hôte toujours actif, puis ouvrir plus tard l’application sur
votre ordinateur portable et y poursuivre cette même discussion.

Sur un Mac ou un appareil Windows où la fonctionnalité est disponible, utilisez **Paramètres \>
Connexions \> Contrôler d’autres appareils** pour ajouter l’autre hôte. Un appareil peut autoriser
l’accès à distance tout en contrôlant un autre appareil.

  

## Connexion à un hôte SSH

Dans l’application de bureau ChatGPT, ajoutez des projets distants à partir d’un hôte SSH et lancez des discussions qui utilisent le système de fichiers et le shell distants. Les discussions liées à ces projets exécutent des commandes, lisent des fichiers et apportent des modifications sur l’hôte distant.

Appliquez à l’hôte distant les mêmes exigences de sécurité que pour un accès SSH standard : clés de confiance, comptes dotés des privilèges minimaux et aucun service sans authentification à l’écoute sur le réseau public.

1. Ajoutez l’hôte à votre configuration SSH afin que Codex le détecte automatiquement.

   ```text
   Host devbox
     HostName devbox.example.com
     User you
     IdentityFile ~/.ssh/id_ed25519

   Codex lit les alias d’hôte explicites dans `~/.ssh/config`, les résout avec
   OpenSSH et ignore les hôtes définis uniquement par un motif.

2. Vérifiez que vous pouvez vous connecter à l’hôte en SSH depuis la machine qui exécute l’application.

   ```bash
   ssh devbox

3. Sur l’hôte distant, installez Codex, puis authentifiez-vous.

   L’application lance l’App Server Codex distant via SSH à l’aide du shell de connexion de
   l’utilisateur distant. Vérifiez que la commande `codex` est disponible sur
   l’hôte distant, dans le `PATH` de ce shell.

4. Dans l’application, ouvrez **Paramètres \> Connexions**, ajoutez ou activez l’hôte SSH, puis
   choisissez un dossier de projet distant.

  

<a id="hand-off-a-thread-between-hosts"></a>
<a id="hand-off-a-chat-between-hosts"></a>
<a id="hand-off-a-task-between-hosts"></a>

## Transfert d’une discussion d’un hôte à un autre

Le transfert déplace une discussion existante et son état Git entre votre ordinateur local et un hôte distant connecté. Utilisez-le pour commencer à travailler localement, poursuivre dans un arbre de travail sur un ordinateur distant, puis rapatrier la discussion ultérieurement.

Avant de transférer une discussion, connectez l’hôte de destination et enregistrez-y un projet associé au même dépôt Git. Si le projet est un sous-répertoire du dépôt, enregistrez le même sous-répertoire sur les deux hôtes. Codex n’affiche que les destinations pour lesquelles un projet correspondant est enregistré.

Pour transférer une discussion :

1. Ouvrez la discussion dans l’application de bureau.
2. Dans le bas de la discussion, sélectionnez l’emplacement d’exécution actuel, puis sélectionnez
   l’hôte de destination. Sélectionnez **Cet ordinateur** pour rapatrier une discussion distante
   vers votre ordinateur local.
3. Vérifiez la destination et la branche, puis sélectionnez **Transférer**.

Codex crée ou réutilise un arbre de travail sur l’hôte de destination, transfère la discussion et l’état Git, puis bascule la discussion vers cet hôte. Si une réponse est en cours, le transfert l’interrompt avant de transférer la discussion.

Dans une autre discussion, vous pouvez aussi demander à Codex de transférer vers un hôte connecté une discussion désignée par son nom. Codex ne peut pas transférer la discussion depuis laquelle la demande est envoyée, et le transfert vers un environnement Codex Cloud n’est pas pris en charge.

## Authentification et exposition réseau

Les connexions distantes utilisent SSH pour démarrer et gérer l’App Server Codex distant. N’exposez pas directement les transports de l’App Server sur un réseau partagé ou public.

Si vous devez accéder à une machine distante hors de votre réseau actuel, utilisez un VPN ou un outil de réseau maillé plutôt que d’exposer directement l’App Server sur Internet.

## Dépannage

### L’hôte n’apparaît pas sur votre téléphone

Vérifiez que l’application de bureau s’exécute sur l’hôte, que vous avez activé **Autoriser
d’autres appareils à se connecter** et que les deux appareils utilisent le même compte ChatGPT et le même
espace de travail. Si vous n’avez pas utilisé la connexion depuis le 8 juin 2026, mettez à jour les deux
applications et associez de nouveau les appareils.

### Le contrôle à distance est désactivé après votre reconnexion

La déconnexion de ChatGPT désactive **Contrôle à distance**, mais ne supprime pas les
associations existantes entre vos appareils. Après votre reconnexion, réactivez **Contrôle à distance** pour
rétablir l’état de connexion précédent.

Si une erreur s’affiche après avoir activé **Contrôle à distance** et sélectionné **Ajouter**,
redémarrez l’application de bureau ChatGPT sur l’hôte, puis réessayez.

### La demande d’approbation n’apparaît pas

Dans l’application mobile ChatGPT, ouvrez **À distance**. Vérifiez que le téléphone et l’hôte utilisent
le même compte ChatGPT et le même espace de travail, puis scannez de nouveau le code QR ou relancez
la configuration depuis l’hôte. Si vous utilisez un espace de travail ChatGPT, demandez à votre administrateur de confirmer
que l’accès au contrôle à distance a été activé.

### La session distante se déconnecte

Vérifiez si l’hôte s’est mis en veille ou a perdu sa connexion réseau, ou si l’application a été fermée. Empêchez l’hôte de se mettre en veille et maintenez-le connecté pendant que ChatGPT travaille.

### L’authentification empêche la configuration

Effectuez l’authentification du compte ou de l’espace de travail demandée pendant la configuration. Si votre organisation exige le SSO, l’authentification multifacteur ou une clé d’accès, terminez la procédure correspondante avant de réessayer. Si la configuration échoue toujours, demandez à l’administrateur de votre espace de travail de confirmer que l’accès au contrôle à distance a été activé.

## Voir aussi

- [Application de bureau ChatGPT](/fr-FR/codex/app)
- [Fonctionnalités](/fr-FR/codex/features)
- [Paramètres de l’application de bureau ChatGPT](/codex/reference/settings)
- [Utilisation de l’ordinateur](/fr-FR/codex/computer-use)
- [Extension Chrome](/fr-FR/codex/chrome-extension)
- [Options de ligne de commande](/codex/developer-commands?surface=cli)
- [Authentification](/fr-FR/codex/auth)
