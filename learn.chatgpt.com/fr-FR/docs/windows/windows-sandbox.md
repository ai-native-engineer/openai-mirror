<!-- source: https://learn.chatgpt.com/fr-FR/docs/windows/windows-sandbox -->

Utilisez Codex sur Windows avec [l’application de bureau ChatGPT](/fr-FR/codex/windows/windows-app) native, le
[CLI](/fr-FR/codex/cli) ou [l’extension IDE](/fr-FR/codex/ide).

L’application de bureau ChatGPT sur Windows prend en charge des flux de travail essentiels tels que les discussions parallèles,
les arbres de travail, les tâches planifiées, les fonctionnalités Git, le navigateur intégré, les aperçus de fichiers,
les plugins et les Skills.

L’application peut s’exécuter nativement dans PowerShell avec un bac à sable Windows sans
avoir besoin de WSL ni d’une machine virtuelle. Codex reste ainsi intégré aux flux de travail natifs de Windows
tout en limitant les autorisations d’accès au système de fichiers et au réseau.

  
    
  

<div class="mb-8">
  
</div>

Le bac à sable Windows natif propose deux modes :

- nativement sur Windows avec le bac à sable `elevated`, plus robuste,
- nativement sur Windows avec le bac à sable de secours `unelevated`.

<span id="windows-sandbox"></span>

## Configurez le bac à sable Windows

Lorsque vous exécutez Codex nativement sur Windows, le mode agent utilise un bac à sable Windows pour
bloquer les écritures dans le système de fichiers en dehors du dossier de travail et empêcher l’accès au réseau
sans votre approbation explicite.

Le bac à sable Windows natif propose deux modes configurables dans
`config.toml` :

```toml
[windows]
sandbox = "elevated" # or "unelevated"

`elevated` est le bac à sable Windows natif recommandé. Il utilise des comptes utilisateur dédiés au bac à sable
et dotés de privilèges réduits, des limites d’autorisations sur le système de fichiers, des règles de
pare-feu et les modifications de stratégie locale nécessaires aux commandes exécutées dans le bac à sable.

`unelevated` est le bac à sable Windows natif de secours. Il exécute les commandes avec un
token Windows restreint dérivé de votre compte utilisateur actuel, applique des limites d’accès au système de fichiers
basées sur les ACL et utilise des contrôles hors ligne au niveau de l’environnement plutôt que
la règle de pare-feu dédiée à l’utilisateur hors ligne. Il est moins robuste que `elevated`, mais
reste utile lorsque la configuration approuvée par l’administrateur est bloquée par une stratégie locale ou
d’entreprise.

Si les deux modes sont disponibles, utilisez `elevated`. Si le bac à sable natif par défaut
ne fonctionne pas dans votre environnement, utilisez `unelevated` comme solution de secours pendant que vous
diagnostiquez le problème de configuration.

Les administrateurs d’entreprise peuvent limiter les implémentations du bac à sable natif
que Codex peut utiliser au moyen de [`requirements.toml`](/fr-FR/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml) :

```toml
[windows]
allowed_sandbox_implementations = ["elevated"]

Cet exemple impose le bac à sable `elevated` et empêche les utilisateurs de se rabattre
sur `unelevated`. Pour autoriser l’une ou l’autre implémentation, incluez les deux valeurs ;
Codex privilégie `elevated` lorsqu’aucun mode n’est sélectionné. Consultez
[la référence de `requirements.toml`](/fr-FR/codex/config-file/config-reference#requirementstoml) pour connaître
les valeurs prises en charge.

Par défaut, les deux modes de bac à sable utilisent aussi un bureau privé pour renforcer
l’isolation de l’interface utilisateur. Définissez `windows.sandbox_private_desktop = false` uniquement si vous avez besoin de
l’ancien comportement `Winsta0\\Default` pour assurer la compatibilité.

### Autorisations du bac à sable

  L’exécution de Codex en mode Accès complet signifie que Codex n’est pas limité au répertoire de votre projet
  et peut effectuer involontairement des actions destructrices susceptibles d’entraîner
  une perte de données. Pour une automatisation plus sûre, conservez les limites du bac à sable et utilisez des
[règles](/fr-FR/codex/agent-configuration/rules) pour des exceptions précises, ou définissez votre
[politique d’approbation sur
  never](/fr-FR/codex/agent-approvals-security#run-without-approval-prompts) afin que
  Codex tente de résoudre les problèmes sans demander d’autorisations élevées,
  en fonction de votre [configuration des approbations et de la sécurité](/fr-FR/codex/agent-approvals-security).

### Tableau de compatibilité des versions de Windows

| Version de Windows                  | Niveau de prise en charge   | Notes                                                                                                                                                                                 |
| -------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Windows 11                       | Recommandé     | Meilleure configuration de référence pour Codex sur Windows. Utilisez-la si vous standardisez un déploiement d’entreprise.                                                                                       |
| Windows 10 récent et entièrement mis à jour | Prise en charge dans la mesure du possible     | Peut fonctionner, mais est moins fiable que Windows 11. Sous Windows 10, Codex dépend de la prise en charge des consoles modernes, notamment de ConPTY. En pratique, la version 1809 ou ultérieure de Windows 10 est requise. |
| Anciennes versions de Windows 10          | Non recommandé | Elles sont plus susceptibles de ne pas inclure les composants de console requis tels que ConPTY et d’échouer dans les environnements d’entreprise.                                                                          |

Conditions supplémentaires concernant l’environnement :

- `winget` doit être disponible. S’il ne l’est pas, mettez Windows à jour ou installez
  Windows Package Manager avant de configurer Codex.
- Le bac à sable natif recommandé nécessite une configuration approuvée par un administrateur.
- Certains appareils gérés par une entreprise bloquent les étapes de configuration requises, même lorsque la
version du système d’exploitation est compatible.

### Accordez au bac à sable un accès en lecture

Lorsqu’une commande échoue parce que le bac à sable Windows ne peut pas lire un répertoire, utilisez :

```text
/sandbox-add-read-dir C:\absolute\directory\path

Le chemin doit être absolu et pointer vers un répertoire existant. Une fois la commande exécutée avec succès, les commandes suivantes exécutées dans le bac à sable peuvent lire ce répertoire pendant la session en cours.

<span id="windows-subsystem-for-linux"></span>

Utilisez par défaut le bac à sable Windows natif. Choisissez [WSL](/fr-FR/codex/windows/wsl)
si vous avez besoin d’outils natifs de Linux, si votre flux de travail se déroule déjà dans WSL2 ou si
aucun des deux modes de bac à sable Windows natif ne répond à vos besoins.

## Dépannage et FAQ

Pour dépanner une machine Windows gérée, commencez par vérifier le mode de bac à sable natif,
la version de Windows et toute erreur de stratégie affichée par Codex. La plupart des problèmes de prise en charge native de
Windows proviennent de la configuration du bac à sable, des droits d’ouverture de session ou des autorisations du système de fichiers,
et non de l’éditeur lui-même.

Si Codex ne parvient pas à terminer la configuration du bac à sable `elevated`, les causes les plus fréquentes
sont les suivantes :

- l’invite UAC de Windows ou l’invite d’administrateur a été refusée,
- la machine n’autorise pas la création d’utilisateurs ou de groupes locaux,
- la machine n’autorise pas la modification des règles de pare-feu,
- la machine bloque les droits d’ouverture de session nécessaires aux utilisateurs du bac à sable,
- ou une autre stratégie d’entreprise bloque une partie du processus de configuration.

Solutions à essayer :

1. Relancez la configuration du bac à sable `elevated` et approuvez l’invite d’administrateur
   si votre environnement le permet.
2. Si votre ordinateur portable professionnel bloque cette opération, demandez à votre équipe informatique si la machine
autorise une configuration approuvée par un administrateur pour créer des utilisateurs ou des groupes locaux, configurer le pare-feu
et accorder aux utilisateurs du bac à sable les droits d’ouverture de session requis.
3. Si la configuration par défaut échoue encore, utilisez le bac à sable `unelevated` afin de pouvoir
   continuer à travailler pendant l’analyse du problème.

Cela signifie que Codex n’a pas pu terminer la configuration du bac à sable `elevated`, plus robuste, sur votre
machine.

- Codex peut tout de même s’exécuter en mode bac à sable.
- Il applique toujours des limites d’accès au système de fichiers basées sur les ACL, mais n’utilise pas la
  séparation des utilisateurs du bac à sable propre à `elevated` et offre une isolation réseau
  moins robuste.
- Cette solution de secours est utile, mais ce n’est pas la configuration d’entreprise
recommandée à long terme.

Si vous utilisez un ordinateur portable d’entreprise géré, la meilleure solution à long terme consiste généralement à
faire fonctionner le bac à sable `elevated` avec l’aide de votre équipe informatique.

Si les commandes exécutées dans le bac à sable échouent avec l’erreur `1385`, Windows refuse le type d’ouverture de session
dont l’utilisateur du bac à sable a besoin pour lancer la commande.

En pratique, cela signifie généralement que Codex a bien créé les utilisateurs du bac à sable,
mais que la stratégie Windows empêche toujours ces utilisateurs de lancer des
commandes dans le bac à sable.

Que faire :

1. Demandez à votre équipe informatique si la stratégie de l’appareil accorde les droits d’ouverture de session requis
aux utilisateurs du bac à sable créés par Codex.
2. Comparez les stratégies de groupe ou les unités d’organisation (OU) si le problème ne touche que certaines
machines ou équipes.
3. Si vous devez continuer à travailler immédiatement, utilisez le bac à sable `unelevated` pendant
   l’analyse du problème de stratégie.
4. Envoyez `CODEX_HOME/.sandbox/sandbox.log` avec votre version de Windows et une
   brève description de l’échec.

Codex peut signaler que le groupe `Everyone` dispose d’un accès en écriture à certains dossiers.

Si cet avertissement s’affiche, les autorisations Windows sur ces dossiers sont trop étendues pour
que le bac à sable puisse les protéger entièrement.

Que faire :

1. Examinez les dossiers répertoriés par Codex dans l’avertissement.
2. Retirez au groupe `Everyone` l’accès en écriture à ces dossiers si cela est approprié dans
   votre environnement.
3. Redémarrez Codex ou relancez la configuration du bac à sable une fois ces autorisations
corrigées.

Si vous ne savez pas comment modifier ces autorisations, demandez de l’aide à votre équipe informatique.

Certaines discussions Codex se déroulent volontairement sans accès sortant au réseau,
selon le mode d’autorisation utilisé.

Si une tâche échoue faute de pouvoir accéder au réseau :

1. Vérifiez si la tâche était censée s’exécuter avec l’accès au réseau désactivé.
2. Si vous vous attendiez à disposer d’un accès au réseau, redémarrez Codex et réessayez.
3. Si le problème persiste, récupérez le journal du bac à sable afin que l’équipe puisse vérifier
si le bac à sable de la machine est dans un état incomplet ou défaillant.

Cela peut se produire après :

- le déplacement d’un dépôt ou d’un espace de travail,
- la modification des autorisations de la machine,
- la modification des stratégies Windows,
- ou d’autres modifications de la configuration système.

À essayer :

1. Redémarrez Codex.
2. Relancez la configuration du bac à sable `elevated`.
3. Si cela ne résout pas le problème, utilisez temporairement le bac à sable `unelevated`
   comme solution de secours.
4. Récupérez le journal du bac à sable pour examen.

Si vous rencontrez toujours des problèmes, envoyez :

- `CODEX_HOME/.sandbox/sandbox.log`

Il est également utile d’indiquer :

- une brève description de ce que vous tentiez de faire,
- si le bac à sable `elevated` a échoué ou si le bac à sable `unelevated` a été utilisé,
- tout message d’erreur affiché dans l’application,
- si vous avez rencontré l’erreur `1385` ou une autre erreur Windows ou PowerShell,
- et si vous utilisez Windows 11 ou Windows 10.

N’envoyez pas :

- le contenu de `CODEX_HOME/.sandbox-secrets/`

Il se peut que votre système ne dispose pas des outils de développement C++ requis par certaines dépendances natives :

- Visual Studio Build Tools (charge de travail C++)
- Microsoft Visual C++ Redistributable (x64)
- Avec `winget`, exécutez `winget install --id Microsoft.VisualStudio.2022.BuildTools -e`

Ensuite, redémarrez complètement VS Code après l’installation.
