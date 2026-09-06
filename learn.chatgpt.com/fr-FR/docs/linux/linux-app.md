<!-- source: https://learn.chatgpt.com/fr-FR/docs/linux/linux-app -->

L’application de bureau ChatGPT pour Linux est disponible en version préliminaire. Installez le paquet
adapté à votre distribution Linux et à l’architecture de votre processeur, puis connectez-vous à votre
compte ChatGPT pour travailler avec des projets, des fichiers locaux et Codex.

## Distributions et architectures prises en charge

La version préliminaire prend en charge les versions de bureau des distributions Linux suivantes :

- Ubuntu 24.04 LTS et 26.04 LTS
- Debian 13
- Fedora 43 et 44

Chaque distribution prise en charge propose des paquets pour les processeurs x64 et ARM64. Pour vérifier
l’architecture de votre processeur, exécutez :

```bash
uname -m

Le résultat `x86_64` indique un processeur x64. Le résultat `aarch64` ou
`arm64` indique un processeur ARM64.

## Téléchargez le paquet adapté

Choisissez `.deb` pour Ubuntu ou Debian, et `.rpm` pour Fedora :

| Distribution     | Architecture | Téléchargement                                                                                                          |
| ---------------- | ------------ | ----------------------------------------------------------------------------------------------------------------- |
| Ubuntu ou Debian | x64          | [Téléchargez `.deb` pour x64](https://persistent.oaistatic.com/codex-app-prod/linux/deb/latest/chatgpt_amd64.deb)     |
| Ubuntu ou Debian | ARM64        | [Téléchargez `.deb` pour ARM64](https://persistent.oaistatic.com/codex-app-prod/linux/deb/latest/chatgpt_arm64.deb)   |
| Fedora           | x64          | [Téléchargez `.rpm` pour x64](https://persistent.oaistatic.com/codex-app-prod/linux/rpm/latest/chatgpt.x86_64.rpm)    |
| Fedora           | ARM64        | [Téléchargez `.rpm` pour ARM64](https://persistent.oaistatic.com/codex-app-prod/linux/rpm/latest/chatgpt.aarch64.rpm) |

## Installation sur Ubuntu ou Debian

Téléchargez le paquet `.deb` adapté à l’architecture de votre processeur. Ouvrez ensuite un
terminal, accédez au répertoire contenant le paquet et installez-le avec
`apt` :

```bash
cd ~/Downloads
sudo apt install ./chatgpt_amd64.deb

Pour ARM64, remplacez `chatgpt_amd64.deb` par `chatgpt_arm64.deb`.

Ouvrez **ChatGPT** depuis votre menu des applications, ou exécutez `chatgpt` dans un terminal.
Connectez-vous à votre compte ChatGPT et suivez le
[guide de démarrage rapide de l’application de bureau](/fr-FR/codex/quickstart?setup=app).

## Installation sur Fedora

Téléchargez le paquet `.rpm` adapté à l’architecture de votre processeur. Ouvrez ensuite un
terminal, accédez au répertoire contenant le paquet et installez-le avec
`dnf` :

```bash
cd ~/Downloads
sudo dnf install ./chatgpt.x86_64.rpm

Pour ARM64, remplacez `chatgpt.x86_64.rpm` par `chatgpt.aarch64.rpm`.

Ouvrez **ChatGPT** depuis votre menu des applications, ou exécutez `chatgpt` dans un terminal.
Connectez-vous à votre compte ChatGPT et suivez le
[guide de démarrage rapide de l’application de bureau](/fr-FR/codex/quickstart?setup=app).

## Mettez l’application à jour

Le paquet configure le dépôt de paquets signé d’OpenAI pendant l’installation.
Utilisez le gestionnaire de paquets de votre distribution pour installer les mises à jour ultérieures.

Sur Ubuntu ou Debian, exécutez :

```bash
sudo apt update
sudo apt install --only-upgrade chatgpt

Sur Fedora, exécutez :

```bash
sudo dnf upgrade --refresh chatgpt

## Compatibilité et limitations

La version préliminaire prend en charge les distributions de bureau répertoriées dans la section
[Distributions et architectures prises en charge](#supported-distributions-and-architectures).
D’autres distributions Linux peuvent fonctionner, mais ne sont pas officiellement prises en charge.

Certaines fonctionnalités nécessitent des plateformes spécifiques. Par exemple,
la fonctionnalité [Utilisation de l’ordinateur](/fr-FR/codex/computer-use) est disponible sur macOS et Windows, mais pas
encore dans la version préliminaire pour Linux. Une prochaine version ajoutera la prise en charge de Linux.

## Prise en charge de Wayland

La prise en charge native de Wayland est expérimentale et continuera de s’améliorer. Dans une session
Wayland, l’application utilise XWayland lorsqu’il est disponible. Pour sélectionner explicitement Wayland
en mode natif, fermez complètement l’application et lancez-la depuis un terminal :

```bash
chatgpt --ozone-platform=wayland

Certaines fonctionnalités, comme les fenêtres flottantes, le positionnement des fenêtres, la gestion du focus et les raccourcis
clavier, peuvent ne pas fonctionner complètement tant que la prise en charge native de Wayland n’est pas arrivée à maturité.

## Étapes suivantes

- Suivez le [guide de démarrage rapide de l’application de bureau](/fr-FR/codex/quickstart?setup=app).
- Configurez l’[Extension Chrome](/fr-FR/codex/chrome-extension) pour l’intégration au navigateur.
- Vérifiez les [autorisations](/fr-FR/codex/permissions) des projets locaux et des commandes.
