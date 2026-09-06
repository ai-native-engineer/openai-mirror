<!-- source: https://learn.chatgpt.com/fr-FR/docs/windows/windows-app -->

# Application de bureau ChatGPT pour Windows

L’[application de bureau ChatGPT pour Windows](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi) vous offre une interface unique pour
travailler sur plusieurs projets, mener des discussions en parallèle et examiner les résultats.
L’application Windows prend en charge les principaux workflows, notamment les arbres de travail, les tâches planifiées, les fonctionnalités
Git, le navigateur intégré, les aperçus de fichiers, les Plugins et les Skills.
Elle s’exécute nativement sur Windows avec PowerShell et le
[bac à sable Windows](/fr-FR/codex/windows/windows-sandbox#windows-sandbox), mais vous pouvez aussi la configurer pour qu’elle
s’exécute dans [Windows Subsystem for Linux 2 (WSL2)](#windows-subsystem-for-linux-wsl).

  
    
  

## Téléchargez l’application de bureau ChatGPT

Téléchargez l’[application de bureau ChatGPT](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi) pour Windows.

Suivez ensuite le [guide de démarrage rapide](/fr-FR/codex/quickstart?setup=app) pour commencer.

Pour connaître les options d’installation et de mise à jour en entreprise, consultez
[Déployer l’application Windows](/fr-FR/codex/enterprise/windows-deployment).

Si vous préférez installer l’application en ligne de commande, exécutez :

```powershell
winget install --id 9PLM9XGG6VKS -s msstore
```

## Bac à sable natif

L’application de bureau ChatGPT sur Windows prend en charge un [bac à sable Windows](/fr-FR/codex/windows/windows-sandbox#windows-sandbox) natif lorsque l’agent s’exécute dans PowerShell et utilise le bac à sable Linux lorsque vous exécutez l’agent dans [Windows Subsystem for Linux 2 (WSL2)](#windows-subsystem-for-linux-wsl). Pour appliquer les protections du bac à sable quel que soit le mode, sélectionnez **Demander l’approbation** sous la zone de saisie avant d’envoyer des messages à Codex.

  Lorsque Codex s’exécute en mode Accès complet, il n’est pas limité au répertoire de votre projet
  et peut effectuer involontairement des actions destructrices susceptibles d’entraîner une
  perte de données. Maintenez les limites du bac à sable et utilisez des
[règles](/fr-FR/codex/agent-configuration/rules) pour les exceptions ciblées, ou définissez votre
[politique d’approbation sur
  never](/fr-FR/codex/agent-approvals-security#run-without-approval-prompts) afin que
  Codex tente de résoudre les problèmes sans demander d’autorisations élevées,
  selon votre [configuration d’approbation et de sécurité](/fr-FR/codex/agent-approvals-security).

## Personnalisation de votre environnement de développement

<section class="feature-grid">

<div>

### Éditeur préféré

Choisissez une application par défaut pour **Ouvrir**, comme Visual Studio, VS Code ou un autre
éditeur. Vous pouvez modifier ce choix pour chaque projet. Si vous avez déjà choisi une
autre application dans le menu **Ouvrir** d’un projet, ce choix propre au projet
est prioritaire.

</div>

  
    
  

</section>

<section class="feature-grid inverse">

<div>

### Terminal intégré

Vous pouvez également choisir le terminal intégré par défaut. Selon les outils
installés, les options disponibles sont :

- PowerShell
- Invite de commandes
- Git Bash
- WSL

Cette modification ne s’applique qu’aux nouvelles sessions de terminal. Si un terminal
intégré est déjà ouvert, redémarrez l’application ou démarrez une nouvelle discussion avant
que le nouveau terminal par défaut n’apparaisse.

</div>

  
    
  

</section>

## Windows Subsystem for Linux (WSL)

Par défaut, l’application de bureau ChatGPT utilise l’agent Codex natif pour Windows. L’agent
exécute donc les commandes dans PowerShell. L’application peut néanmoins utiliser les projets stockés dans
Windows Subsystem for Linux 2 (WSL2) en faisant appel à la CLI `wsl` si nécessaire.

Pour ajouter un projet depuis le système de fichiers WSL, cliquez sur **Ajouter un nouveau projet**
ou appuyez sur <kbd>Ctrl</kbd>+<kbd>O</kbd>, puis saisissez `\\wsl$\` dans la fenêtre de l’Explorateur
de fichiers. Sélectionnez ensuite votre distribution Linux et le dossier que vous
souhaitez ouvrir.

Si vous comptez continuer à utiliser l’agent natif pour Windows, stockez de préférence vos projets sur
votre système de fichiers Windows et accédez-y depuis WSL via
`/mnt/<drive>/...`. Cette configuration est plus fiable que l’ouverture de projets
directement depuis le système de fichiers WSL.

Si vous souhaitez exécuter l’agent lui-même dans WSL2, ouvrez les **[Paramètres](codex://settings)**,
passez l’agent de Windows natif à WSL, puis **redémarrez l’application**. Cette
modification ne prend effet qu’après le redémarrage. Vos projets devraient rester en
place après celui-ci.

WSL1 était pris en charge jusqu’à Codex `0.114`. À partir de Codex `0.115`, le bac à sable
Linux utilise `bubblewrap` ; WSL1 n’est donc plus pris en charge.

  
    
  

Le terminal intégré se configure indépendamment de l’agent. Consultez la section
[Personnalisation de votre environnement de développement](#customize-for-your-dev-setup) pour connaître les
options du terminal. Vous pouvez conserver l’agent dans WSL tout en utilisant PowerShell dans le
terminal, ou utiliser WSL pour les deux, selon votre workflow.

## Outils de développement utiles

Codex fonctionne mieux lorsque quelques outils de développement courants sont déjà installés :

- **Git** : permet d’utiliser le volet de révision dans l’application de bureau ChatGPT et d’examiner ou
  d’annuler les modifications.
- **Node.js** : un outil courant que l’agent utilise pour accomplir ses tâches plus
  efficacement.
- **Python** : un outil courant que l’agent utilise pour accomplir ses tâches plus
  efficacement.
- **.NET SDK** : utile pour créer des applications Windows natives.
- **GitHub CLI** : fournit les fonctionnalités propres à GitHub dans l’application de bureau ChatGPT.

Installez-les avec le gestionnaire de paquets Windows par défaut, `winget`, en collant ce qui suit
dans le [terminal intégré](/fr-FR/codex/integrated-terminal) ou en
demandant à Codex de les installer :

```powershell
winget install --id Git.Git
winget install --id OpenJS.NodeJS.LTS
winget install --id Python.Python.3.14
winget install --id Microsoft.DotNet.SDK.10
winget install --id GitHub.cli
```

Après avoir installé GitHub CLI, exécutez `gh auth login` pour activer les fonctionnalités GitHub dans
l’application.

Si vous avez besoin d’une autre version de Python ou de .NET, modifiez les identifiants des paquets pour utiliser la
version souhaitée.

## Dépannage et FAQ

### Exécution de commandes avec des autorisations élevées

Si Codex doit exécuter des commandes avec des autorisations élevées, lancez l’application de bureau ChatGPT
elle-même en tant qu’administrateur. Après l’installation, ouvrez le menu Démarrer,
recherchez l’application et choisissez **Exécuter en tant qu’administrateur**. L’agent Codex hérite de ce
niveau d’autorisation.

### La stratégie d’exécution PowerShell bloque les commandes

Si vous n’avez jamais utilisé d’outils comme Node.js ou `npm` dans PowerShell, l’agent
Codex ou le terminal intégré peuvent rencontrer des erreurs liées à la stratégie d’exécution.

Cela peut également se produire si Codex crée des scripts PowerShell pour vous. Dans ce cas,
vous devrez peut-être définir une stratégie d’exécution moins restrictive pour que PowerShell puisse
les exécuter.

L’erreur peut ressembler à ceci :

```text
npm.ps1 cannot be loaded because running scripts is disabled on this system.
```

Une solution courante consiste à définir la stratégie d’exécution sur `RemoteSigned` :

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```

Pour plus de détails et d’autres options, consultez le
[guide de Microsoft sur les stratégies d’exécution](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies)
avant de modifier la stratégie.

### Scripts d’environnement local sur Windows

Si votre [environnement local](/fr-FR/codex/environments/local-environment) utilise des commandes
multiplateformes, comme des scripts `npm`, vous pouvez conserver un script de configuration ou un
ensemble d’actions commun à toutes les plateformes.

Si vous avez besoin d’un comportement propre à Windows, créez des scripts de configuration ou
des actions spécifiques à Windows.

Les actions s’exécutent dans l’environnement utilisé par votre terminal intégré. Consultez la section
[Personnalisation de votre environnement de développement](#customize-for-your-dev-setup).

Les scripts de configuration locale s’exécutent dans l’environnement de l’agent : WSL si l’agent utilise WSL,
et PowerShell dans le cas contraire.

### Partage de la configuration, de l’authentification et des sessions avec WSL

L’application Windows utilise le même répertoire personnel de Codex que la version native de Codex sur Windows :
`%USERPROFILE%\.codex`.

Si vous exécutez également Codex CLI dans WSL, la CLI utilise par défaut le répertoire personnel
Linux et ne partage donc pas automatiquement la configuration, les données d’authentification en cache
ni l’historique des sessions avec l’application Windows.

Pour les partager, utilisez l’une des méthodes suivantes :

- Synchronisez `~/.codex` dans WSL avec `%USERPROFILE%\.codex` sur votre système de fichiers.
- Configurez WSL pour utiliser le répertoire personnel de Codex sous Windows en définissant `CODEX_HOME` :

```bash

```

Pour appliquer ce paramètre à tous vos shells, ajoutez-le au profil de votre shell WSL, par exemple
`~/.bashrc` ou `~/.zshrc`.

### Fonctionnalités Git indisponibles

Si Git n’est pas installé nativement sur Windows, l’application ne peut pas utiliser certaines
fonctionnalités. Installez-le avec `winget install Git.Git` depuis PowerShell ou `cmd.exe`.

### Git n’est pas détecté pour les projets ouverts depuis `\\wsl$`

Pour l’instant, si vous souhaitez utiliser l’agent natif pour Windows avec un projet également
accessible depuis WSL, la solution de contournement la plus fiable consiste à stocker le projet
sur le lecteur Windows natif et à y accéder dans WSL via `/mnt/<drive>/...`.

### `Cmder` n’apparaît pas dans la boîte de dialogue Ouvrir

Si `Cmder` est installé mais n’apparaît pas dans la boîte de dialogue Ouvrir de Codex, ajoutez-le au
menu Démarrer de Windows : faites un clic droit sur `Cmder`, puis choisissez **Ajouter au menu Démarrer**. Ensuite,
redémarrez Codex ou l’ordinateur.
