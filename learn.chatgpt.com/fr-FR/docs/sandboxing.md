<!-- source: https://learn.chatgpt.com/fr-FR/docs/sandboxing -->

Le bac à sable définit les limites qui permettent à l’agent d’agir de manière autonome sans lui donner
un accès sans restriction à votre machine. Lorsqu’une discussion locale exécute des commandes dans
**l’application de bureau ChatGPT**, **Codex CLI** ou **l’extension IDE**, ces commandes s’exécutent dans un
environnement restreint au lieu de s’exécuter par défaut avec un accès complet.

Cet environnement détermine ce que l’agent peut faire de lui-même, notamment les fichiers qu’il
peut modifier et si les commandes peuvent accéder au réseau. Tant qu’une tâche reste dans
ces limites, l’agent peut poursuivre son travail sans s’arrêter pour demander une confirmation. S’il
doit les dépasser, le processus d’approbation prend le relais.

  Le bac à sable et les approbations sont deux mécanismes distincts qui fonctionnent ensemble. Le
bac à sable définit les limites techniques. La politique d’approbation détermine quand
l’agent doit s’arrêter et demander une approbation avant de les franchir.

## Rôle du bac à sable

Le bac à sable s’applique aux commandes lancées, et pas seulement aux opérations intégrées sur les
fichiers. Si l’agent exécute des outils tels que `git`, des gestionnaires de paquets ou des outils d’exécution de tests,
ces commandes sont soumises aux mêmes limites du bac à sable.

Codex s’appuie sur les mécanismes de contrôle natifs de chaque système d’exploitation. L’implémentation diffère
entre macOS, Linux, WSL2 et la version native de Windows, mais le principe reste le même dans les différentes
interfaces : fournir à l’agent un environnement de travail délimité, afin que les tâches courantes puissent s’exécuter
de façon autonome dans des limites clairement définies.

## Pourquoi c’est important

Le bac à sable limite la lassitude liée aux demandes d’approbation. Au lieu de vous demander de confirmer chaque
commande à faible risque, l’agent peut lire des fichiers, les modifier et exécuter les commandes courantes du projet
dans le périmètre que vous avez déjà approuvé.

Cela vous donne aussi un modèle de confiance plus clair pour les tâches agentiques. Votre confiance ne repose pas
seulement sur les intentions de l’agent, mais aussi sur les limites qui encadrent
son fonctionnement. Vous pouvez ainsi plus facilement le laisser travailler de façon autonome,
tout en sachant quand il s’arrêtera pour demander de l’aide.

## Bien démarrer

Le mode d’autorisations par défaut active automatiquement le bac à sable.

### Prérequis

Sur **macOS**, le bac à sable fonctionne sans configuration supplémentaire grâce au framework Seatbelt
intégré.

Sur **Windows**, Codex utilise le [bac à sable
Windows](/fr-FR/codex/windows/windows-sandbox#windows-sandbox) natif lorsque vous l’exécutez dans PowerShell, et
l’implémentation du bac à sable Linux lorsque vous l’exécutez dans WSL2.

Sous **Linux et WSL2**, commencez par installer `bubblewrap` avec votre gestionnaire de paquets :

  <div slot="ubuntu-debian">

```bash
sudo apt install bubblewrap

  </div>

  <div slot="fedora">

```bash
sudo dnf install bubblewrap

  </div>

Codex utilise le premier exécutable `bwrap` trouvé dans `PATH`. Si aucun exécutable `bwrap`
n’est disponible, Codex utilise à la place un utilitaire intégré, mais celui-ci
nécessite la prise en charge de la création d’espaces de noms utilisateur non privilégiés. L’installation du
paquet de la distribution qui fournit `bwrap` garantit la fiabilité de cette configuration.

Codex affiche un avertissement au démarrage si `bwrap` est absent ou si l’utilitaire
ne peut pas créer l’espace de noms utilisateur requis. Sur les distributions qui restreignent ce
paramètre AppArmor, chargez de préférence le profil AppArmor `bwrap` afin que `bwrap` puisse
continuer à fonctionner sans désactiver globalement la restriction.

  **Remarque sur AppArmor dans Ubuntu :** Sur Ubuntu 25.04, l’installation de `bubblewrap` depuis
  le dépôt de paquets d’Ubuntu devrait fonctionner sans configuration AppArmor supplémentaire. Le
profil `bwrap-userns-restrict` est fourni dans le paquet `apparmor` à l’emplacement
`/etc/apparmor.d/bwrap-userns-restrict`.

Sur Ubuntu 24.04, Codex peut encore signaler qu’il ne peut pas créer l’espace de noms
utilisateur requis après l’installation de `bubblewrap`. Copiez et chargez le profil supplémentaire :

```bash
sudo apt update
sudo apt install apparmor-profiles apparmor-utils
sudo install -m 0644 \
  /usr/share/apparmor/extra-profiles/bwrap-userns-restrict \
  /etc/apparmor.d/bwrap-userns-restrict
sudo apparmor_parser -r /etc/apparmor.d/bwrap-userns-restrict

`apparmor_parser -r` charge le profil dans le noyau sans redémarrage. Vous
pouvez également recharger tous les profils AppArmor :

```bash
sudo systemctl reload apparmor.service

Si ce profil n’est pas disponible ou ne résout pas le problème, vous pouvez désactiver
la restriction AppArmor sur les espaces de noms utilisateur non privilégiés avec :

```bash
sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0

## Fonctionnement des autorisations

Utilisez le contrôle des autorisations de votre interface pour modifier la façon dont Codex gère les
actions locales.

Les approbations déterminent quand Codex s’interrompt avant une action, tandis que le bac à sable
détermine les fichiers et les ressources réseau auxquels les commandes peuvent accéder. Lorsqu’une demande
d’approbation propose différentes portées, par exemple une approbation ponctuelle ou valable pour toute la session,
choisissez la portée la plus restreinte qui permette à la tâche de continuer. Conservez par défaut les limites du projet ;
utilisez des projets ou des arbres de travail distincts au lieu
d’étendre l’accès à des dépôts sans rapport entre eux.

ChatGPT Work exécute le code et les commandes shell dans un environnement géré et isolé.
La politique de l’espace de travail et les contrôles propres à chaque outil déterminent les fonctionnalités
disponibles. Lorsque le paramètre est disponible, utilisez **Paramètres \> Contrôles des données \> Accès
réseau de Work** pour gérer l’accès réseau du code et des commandes shell. Activez
**Autoriser l’accès à Internet public** pour permettre à ces commandes d’accéder à Internet
public. Lorsque cette option est désactivée, les commandes ne peuvent accéder qu’aux noms d’hôte requis figurant dans une
liste d’autorisation gérée.

La recherche web, les plugins et le navigateur distant disposent de contrôles distincts.
Les modifications prennent effet une fois l’exécution de code ou de commandes shell en cours terminée et après que Work
a actualisé son environnement d’exécution. La version web de ChatGPT ne donne accès ni au bac à sable local de Codex
ni au sélecteur de mode d’approbation.

Dans l’application de bureau ChatGPT, utilisez le contrôle des autorisations sous la zone de saisie.
Selon votre configuration, le menu peut inclure **Demander l’approbation**,
**Approuver à ma place** pour les demandes d’approbation éligibles, **Accès complet**, ainsi que des profils
d’autorisations nommés ou personnalisés.

Dans la CLI, saisissez
[`/permissions`](/codex/developer-commands?surface=cli#cli-update-permissions-with-permissions)
pour ouvrir le sélecteur d’autorisations et changer de profil d’autorisations actif.

Dans l’extension IDE, utilisez le contrôle des autorisations sous la zone de saisie.
Selon votre configuration, le menu peut inclure **Demander l’approbation**,
**Approuver à ma place** pour les demandes d’approbation éligibles, **Accès complet**, ainsi que des profils
d’autorisations nommés ou personnalisés.

<div class="not-prose my-8 max-w-[18rem] mr-auto">
  
    
      
    
  
</div>

<a id="configure-defaults"></a>

## Configuration des valeurs par défaut

Pour retrouver le même comportement à chaque démarrage, définissez des valeurs par défaut dans `config.toml`.
La page [Principes de configuration](/fr-FR/codex/config-file/config-basic) en explique le fonctionnement, et la
[Référence de configuration](/fr-FR/codex/config-file/config-reference) documente précisément les clés
`sandbox_mode`, `approval_policy`, `approvals_reviewer` et
`sandbox_workspace_write.writable_roots`. Utilisez ces paramètres pour déterminer le degré
d’autonomie accordé par défaut à l’agent, les répertoires dans lesquels il peut écrire, les cas où il
doit s’interrompre pour demander une approbation et qui examine les demandes d’approbation éligibles.

Les principaux modes de bac à sable sont les suivants :

- `read-only` : L’agent peut consulter les fichiers, mais ne peut ni les modifier ni exécuter
  de commandes sans approbation.
- `workspace-write` : L’agent peut lire des fichiers, modifier ceux de l’espace de travail et exécuter
  des commandes locales courantes à l’intérieur de ce périmètre. C’est le mode par défaut, conçu pour fluidifier
  le travail local.
- `danger-full-access` : L’agent fonctionne sans les restrictions du bac à sable. Ce mode supprime
  les restrictions d’accès au système de fichiers et au réseau. Ne l’utilisez que si vous souhaitez
  que l’agent agisse avec un accès complet.

Les politiques d’approbation courantes sont les suivantes :

- `untrusted` : L’agent demande une approbation avant d’exécuter une commande qui ne figure pas dans son ensemble
  de commandes de confiance.
- `on-request` : Par défaut, l’agent travaille dans le bac à sable et demande une approbation lorsqu’il
  doit en dépasser les limites.
- `never` : L’agent ne s’arrête pas pour demander une approbation.

Lorsque les approbations sont interactives, vous pouvez également choisir qui les examine avec
`approvals_reviewer` :

- `user` : les demandes d’approbation sont présentées à l’utilisateur. Il s’agit de la valeur par défaut.
- `auto_review` : les demandes d’approbation éligibles sont transmises à un agent réviseur (voir
[révision automatique](/fr-FR/codex/sandboxing/auto-review)).

Pour accorder un accès complet, utilisez `sandbox_mode = "danger-full-access"` avec
`approval_policy = "never"`. À l’inverse, le préréglage d’automatisation locale
à moindre risque utilise `sandbox_mode = "workspace-write"` avec
`approval_policy = "on-request"`, ou les options CLI équivalentes
`--sandbox workspace-write --ask-for-approval on-request`. Vous pouvez ensuite conserver
`approvals_reviewer = "user"` pour les approbations manuelles, ou définir
`approvals_reviewer = "auto_review"` pour la révision automatique des demandes d’approbation.

Si l’agent doit travailler dans plusieurs répertoires, les racines accessibles en écriture permettent
d’étendre les emplacements qu’il peut modifier sans désactiver entièrement le bac à sable. Si
vous avez besoin d’un périmètre de confiance plus large ou plus restreint, ajustez le mode de bac à sable par défaut
et la politique d’approbation plutôt que de vous appuyer sur des exceptions ponctuelles.

Lorsqu’un workflow nécessite une exception particulière, utilisez les [règles](/fr-FR/codex/agent-configuration/rules). Elles
permettent d’autoriser des préfixes de commande hors du bac à sable, de demander une approbation ou de les interdire, ce qui est
souvent préférable à un élargissement global de l’accès. Pour savoir où accéder aux paramètres
propres à l’IDE, consultez les [paramètres de l’extension IDE Codex](/codex/developer-settings?surface=ide).

La révision automatique, lorsqu’elle est disponible, ne modifie pas le périmètre du bac à sable. Elle
fait partie des valeurs possibles de `approvals_reviewer` pour les demandes d’approbation déclenchées aux limites de ce périmètre, par exemple
les demandes de sortie du bac à sable, les accès réseau bloqués ou les appels d’outils avec effets de bord
qui nécessitent encore une approbation. Les actions déjà autorisées dans le bac à sable s’exécutent
sans révision supplémentaire. Pour en savoir plus sur le cycle de vie du réviseur, les types de déclenchement, la sémantique
du refus et la configuration, consultez la
[révision automatique](/fr-FR/codex/sandboxing/auto-review).

Les informations propres à chaque plateforme figurent dans la documentation correspondante. Pour la configuration native de Windows,
son fonctionnement et son dépannage, consultez [Windows](/fr-FR/codex/windows/windows-sandbox). Pour connaître les exigences applicables aux administrateurs
et les restrictions imposées au niveau de l’organisation sur le bac à sable et les approbations, consultez
[Autorisations de l’agent et sécurité](/fr-FR/codex/agent-approvals-security).
