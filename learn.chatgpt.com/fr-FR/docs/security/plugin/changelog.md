<!-- source: https://learn.chatgpt.com/fr-FR/docs/security/plugin/changelog -->

Consultez ce journal des modifications pour découvrir les changements apportés au Plugin Codex Security.

**Dernière version du plugin :** `0.1.20`.

Vérifiez la version du plugin dans votre environnement Codex actuel avant d’utiliser une fonctionnalité d’une version plus récente.

Les entrées du journal des modifications suivent la version du plugin, et non celle du paquet. Les utilisateurs de la CLI et du
SDK peuvent exécuter `npx @openai/codex-security info --json` pour vérifier simultanément les versions du
paquet et du plugin inclus.

## 0.1.20 (17 août 2026)

### Exécutez les analyses approfondies sous forme d’audits complets et indépendants

- Faites réaliser à chaque agent d’analyse approfondie le même audit de bout en bout que pour les analyses standard, notamment la modélisation des menaces, la validation, l’analyse des chemins d’attaque et la génération de rapports de couverture.
- Regroupez les rapports finalisés par les agents en une seule analyse, tout en respectant les durées maximales configurées et en préservant la couverture partielle, la reprise après redémarrage et l’annulation.
- Utilisez quatre agents en parallèle par défaut, arrêtez l’analyse après quatre analyses consécutives
  terminées sans nouveau constat et limitez une analyse approfondie à 40 exécutions d’agents. Les paramètres
`workers = "auto"` existants correspondent désormais à quatre agents. Consultez
[Configuration de l’environnement d’exécution des analyses approfondies](/fr-FR/codex/security/plugin/deep-scans#configure-deep-scan-runtime).
- Reprenez l’exécution des agents qui ont terminé la revue du code source mais perdu leur brouillon final, au lieu de répéter l’audit complet.

### Vérifiez Trusted Access for Cyber avant les analyses hébergées

- Sur les hôtes Codex qui proposent l’application Codex Security Access, vérifiez l’état de Trusted Access avant le démarrage des analyses standard, des analyses des modifications et des analyses approfondies.
- Recevez un avertissement bien visible lorsque les résultats d’analyse protégés risquent d’être indisponibles, accompagné d’un lien d’inscription si l’accès n’est pas accordé.
- Poursuivez l’analyse si la vérification ne permet pas de confirmer l’état de Trusted Access ou si l’accès n’est pas accordé ; cet avertissement ne conditionne pas l’exécution de l’analyse.
- Les paquets publics de la CLI et du SDK n’effectuent pas cette vérification informative dans la version `0.1.20`.

### Exécutez des analyses approfondies dans davantage d’environnements

- Lancez des agents d’analyse approfondie depuis des installations de la CLI et du SDK distribuées sous forme de paquets, y compris
  sur Windows sans exécutable `codex` installé globalement.
- Isolez les paramètres des analyses approfondies de la CLI et du SDK autonomes de ceux des autres analyses en cours.
- Conservez les paramètres d’approbation non interactive dans les agents imbriqués d’analyse approfondie.

### Préservez les résultats d’analyse dans davantage de cas de défaillance

- Préservez davantage d’analyses enregistrées et de résultats finalisés par les agents lors des procédures de récupération après redémarrage, archivage ou transfert.
- Récupérez les constats valides à partir de données d’analyse anciennes ou incomplètes.
- Menez les analyses à terme même lorsque des rapports de couverture indépendants se chevauchent.
- Comptabilisez correctement les entrées mises en cache dans les totaux de consommation de tokens, pour les réponses actuelles comme pour les réponses plus anciennes des fournisseurs.

## 0.1.19 (13 août 2026)

### Définissez une durée maximale pour les analyses approfondies

- Attribuez à `[deep_scan].max_time_hours` une durée strictement positive ne dépassant pas 96 heures.
  Vous pouvez utiliser des fractions d’heure.
- Conservez les résultats de détection déjà obtenus à l’expiration du délai, puis poursuivez la validation et la génération de rapports.
- Marquez le rapport comme partiel si aucune revue du code source ne se termine avant l’expiration du délai.

### Améliorez la fiabilité des analyses

- Conservez le travail de détection terminé lorsqu’un agent s’arrête ou qu’un processus de réduction effectue une nouvelle tentative.
- Lisez des fichiers source plus volumineux et générez des rapports sans les anciennes limites de taille fixes.
- Lisez les modifications enregistrées dans la révision sélectionnée et conservez les chemins relatifs au dépôt sur Windows.
- Transmettez les identifiants OpenRouter et Fireworks aux agents chargés des analyses approfondies.

## 0.1.18 (7 août 2026)

### Utilisez Amazon Bedrock pour les analyses de sécurité

- Lancez des analyses avec des tokens au porteur Amazon Bedrock et des profils AWS, des paramètres de région, une identité web ou des identifiants de conteneur.
- Veillez à ce que l’authentification AWS reste disponible pour les agents délégués aux analyses approfondies.

### Exécutez les analyses standard avec moins de coordination

- Utilisez un workflow plus simple pour les analyses standard de dépôts et celles limitées à certains chemins.
- Conservez les consignes des fichiers `SECURITY.md` présents dans les sous-dossiers, le périmètre exact de l’analyse, les informations de progression
  et les rapports d’analyse finaux.

### Démarrez et terminez les analyses de manière plus fiable

- Accordez jusqu’à cinq minutes aux analyses lancées depuis un prompt pour initialiser les dépôts volumineux, au lieu de les interrompre après 30 secondes.
- Menez à terme les analyses standard et approfondies lorsqu’un hôte limite la longueur des noms d’outils.

### Conservez la possibilité d’appliquer des correctifs après des modifications du système de fichiers

- Corrigez les problèmes détectés par les analyses terminées même après un remontage du système de fichiers qui modifie son identifiant de périphérique.
- Continuez d’exiger la copie de travail et la révision Git d’origine avant d’appliquer un correctif.

## 0.1.17 (5 août 2026)

### Suivez la progression des analyses en temps réel

- Suivez la phase d’analyse en cours, le temps écoulé, les agents actifs, les fichiers examinés et la consommation de tokens dans une même vue de progression en temps réel.
- Suivez l’avancement de la revue du dépôt à mesure que l’examen de chaque fichier se termine, sans attendre la fin de l’analyse.

### Reprenez les analyses approfondies interrompues

- Poursuivez une analyse approfondie en cours après le redémarrage de son coordinateur, sans répéter les revues de fichiers déjà terminées.
- Conservez les résultats de détection déjà obtenus, la propriété de l’analyse et le travail en attente lors des mises à jour de l’application ou des interruptions de sessions d’analyse.

### Réduisez la surcharge liée au démarrage et à la finalisation des analyses

- Lancez directement les analyses standard, les analyses des modifications et les analyses approfondies dans les workflows natifs, sans ouvrir l’ancien widget d’analyse intégré, désormais retiré.
- Réutilisez les résumés d’analyses terminées sans recharger chaque constat, sauf si vous demandez les résultats structurés complets.

## 0.1.16 (4 août 2026)

### Suivez la consommation mesurée des analyses

- Consultez la consommation totale de tokens, ainsi que celle des tokens d’entrée, des tokens d’entrée mis en cache et des tokens de sortie, pour l’analyse principale et ses agents délégués.
- Distinguez les mesures complètes, partielles et indisponibles au lieu d’afficher zéro lorsque les données de consommation manquent.

### Exécutez des analyses plus approfondies avec des résultats cohérents

- Utilisez les mêmes phases de modélisation des menaces, de découverte, de validation, d’analyse des chemins d’attaque
et de génération de rapports pour les analyses standard et approfondies.
- Configurez depuis la CLI ou le SDK les agents d’exécution des analyses approfondies, la délégation par agent,
la saturation et les limites de découverte.
- Exécutez des analyses approfondies avec l’environnement d’exécution pris en charge par le modèle pour les agents, et restaurez
les anciens états d’analyse sans perdre l’historique existant.
- Générez le rapport principal des analyses de modifications et des analyses approfondies sans avoir à produire séparément
des rapports de vulnérabilité ou des recommandations de durcissement.

### Préservez l’exactitude des consignes d’analyse et des cibles de dépôt

- Mettez à jour les consignes de sécurité pendant une analyse en cours et transmettez-les aux phases suivantes
ainsi qu’aux agents d’exécution délégués des analyses approfondies.
- Conservez les URL des dépôts, les références aux pull requests et un contexte de sécurité plus étendu,
sans autoriser d’accès réseau que vous n’avez pas demandé.
- Faites échouer les analyses si le dépôt ou la cible de l’analyse change pendant l’exécution afin que
l’automatisation n’accepte pas de constats obsolètes.
- Respectez les paramètres de proxy d’entreprise et de certificats de confiance dans les environnements
réseau gérés.

### Rédigez des rapports de vulnérabilité plus clairs

- Produisez des rapports de vulnérabilité étayés par le code source, qui distinguent les comportements observés
des hypothèses non vérifiées.
- Présentez de façon réaliste les limites des preuves de concept et indiquez les versions concernées,
les frontières de sécurité et des consignes de remédiation concrètes.

## 0.1.15 (30 juillet 2026)

### Conservez les résultats des analyses lorsque le dépôt change

- Gardez les constats finalisés et les rapports rattachés à la révision ou à l’instantané de l’arbre de travail
d’origine, même si les fichiers ou la révision du dépôt changent
pendant une analyse.
- Affichez un avertissement à la fin de l’analyse lorsque le code sélectionné change ou que la cible devient
indisponible, au lieu de supprimer les résultats de l’analyse.
- Archivez une analyse existante avant de réutiliser son répertoire de sortie pour une autre analyse.

### Tenez compte des retours sur les constats après examen

- Enregistrez un motif lorsque vous clôturez un constat en le classant comme faux positif.
- Réutilisez les décisions de classement en faux positif déjà examinées lors des analyses ultérieures de la même cible,
sans les appliquer à une autre copie de travail ni à une cible sans rapport.
- Écartez un constat récurrent uniquement si le motif précédent reste applicable
au code et aux contrôles de sécurité actuels.

### Récupérez les constats valides sans surestimer la couverture

- Conservez les constats valides lorsqu’un autre constat, un rapport ou un artefact de durcissement est
mal formé, et affichez un avertissement pour les données ignorées.
- Supprimez les constats en double et conservez le plus solide selon sa gravité,
son niveau de confiance et les éléments de preuve qui l’étayent.
- Indiquez une couverture partielle lorsque Codex ne peut pas vérifier les constats, les justificatifs de revue
ou les zones à examiner ensuite.
- Incluez dans les exportations SARIF les avertissements de couverture incomplète et de revue différée.

### Gardez les paramètres et la progression de l’analyse visibles

- Enregistrez le modèle et l’effort de raisonnement sélectionnés avec les analyses standard et approfondies pour que
l’historique et la progression restent cohérents après chaque rechargement.
- Affichez le nombre de revues indépendantes en cours et terminées pour les analyses approfondies,
ainsi que le moment où débute la consolidation des résultats.
- Adaptez la phase de découverte des analyses standard à la capacité disponible des agents d’exécution, tout en conservant
une seule liste de fichiers inclus dans le périmètre et une seule passe d’examen des candidats.

### Prenez en charge davantage de structures de dépôts et de systèmes de fichiers

- Incluez les dépôts Git imbriqués lors de la capture d’un instantané de l’arbre de travail.
- Conservez à l’identique les chemins des fichiers inclus dans le périmètre et gérez les chemins Windows
insensibles à la casse.
- Développez le chemin configuré dans `CODEX_HOME` lorsqu’il commence par `~`, pendant la vérification préalable à l’analyse.

## 0.1.14 (28 juillet 2026)

### Examinez l’historique des analyses et les constats récurrents

- Filtrez les dépôts, les constats et l’historique des analyses grâce à des pages de résultats de taille limitée
et à des informations d’état plus claires.
- Relancez une analyse avec ses paramètres enregistrés et comparez les analyses terminées afin de distinguer
les constats nouveaux, persistants, résolus et non réanalysés.
- Regroupez les arbres de travail d’un même dépôt et utilisez des identifiants stables pour les dépôts et les constats
dans toutes les vues.

### Définissez la politique de sécurité du dépôt

- Utilisez `$codex-security:define-security-policy` pour examiner ou mettre à jour les consignes de
`SECURITY.md` applicables au périmètre concerné : frontières de confiance, invariants de sécurité, constats
  à signaler, gravité, exclusions et risques acceptés.
- Appliquez le fichier de politique le plus proche, en limitant sa taille et en refusant les liens symboliques
qui pointent hors du dépôt.

### Examinez les constats avant d’en assurer le suivi

- Sélectionnez jusqu’à 25 constats issus d’une analyse terminée afin d’en assurer le suivi
dans Linear ou via les issues GitHub.
- Renvoyez les constats sélectionnés à Codex pour révision et approbation, au lieu de
créer directement des issues depuis l’espace de travail des constats.

### Exécutez des analyses standard avec un workflow plus simple

- Utilisez une liste déterministe unique des fichiers inclus dans le périmètre et un registre compact des candidats pour
les analyses standard portant sur un dépôt ou sur des chemins ciblés.
- Conservez le manifeste, les constats, la couverture, le rapport et les sorties SARIF existants
tout en réduisant les étapes d’analyse répétées.

## 0.1.13 (25 juillet 2026)

### Examinez les constats dans davantage d’environnements

- Conservez les constats de sécurité avérés lorsque le code concerné est local, interne, utilisé pour
l’entraînement ou non déployé en production.
- Ajustez la gravité et le niveau de confiance en fonction du contexte de déploiement et d’exposition,
au lieu d’écarter automatiquement le constat.

## 0.1.12 (23 juillet 2026)

### Exécutez des analyses plus approfondies avec un suivi de progression plus clair

- Exécutez des analyses approfondies qui coordonnent des agents d’exécution à l’échelle de tout un dépôt
ou d’un répertoire sélectionné.
- Transmettez vos paramètres de modèle et de raisonnement aux tâches d’analyse déléguées.
- Consultez les résultats de la vérification préalable, la progression de l’analyse, la capacité disponible des agents d’exécution
et le comportement en cas de repli avant et pendant une analyse.

### Examinez et relancez les analyses précédentes

- Ouvrez les analyses en cours et précédentes depuis la liste des analyses de sécurité.
- Rouvrez une analyse enregistrée dans l’espace de travail des constats, ou relancez-la pour actualiser les
résultats.
- Consultez des états de fin plus clairs, ainsi que des détails sur les constats et un historique des analyses
plus cohérents.

### Configurez les analyses avec moins d’interruptions

- Lancez des analyses depuis le parcours de configuration natif sans quitter votre tâche en cours.
- Conservez la configuration de l’analyse dans le panneau latéral, même lorsque Codex est en mode plein écran.
- Fermez le panneau de configuration lorsque vous n’en avez pas besoin et conservez cette préférence pour les analyses suivantes.

### Examinez et corrigez les constats validés

- Conservez les constats validés de faible gravité dans les résultats des analyses terminées.
- Consultez des détails plus cohérents sur les constats dans les analyses, les rapports et les exports.
- Relancez la correction et réutilisez le contexte pertinent de l’analyse lors des corrections suivantes.

### Exportez les résultats pour les workflows de sécurité existants

- Exportez les constats finalisés au format JSON, CSV ou SARIF.
- Générez localement des résultats SARIF pour les intégrations avec des outils d’analyse de code et de sécurité.
- Assurez la cohérence des détails des constats dans tous les formats d’exportation.

## 0.1.11 (10 juillet 2026)

### Générez des rapports détaillés sur les constats et le renforcement de la sécurité

- Générez, pour chaque constat d’analyse à signaler, un rapport de vulnérabilité étayé par le code source, accompagné de fichiers de preuve de concept lorsqu’ils sont disponibles.
- Examinez un dossier de renforcement structurel analysant l’ensemble des constats, les compromis techniques, les options de migration et les diagrammes à l’appui.
- Utilisez `report.md` comme point d’entrée vers ces résultats dérivés situés dans `findings/`
  et `hardening/`. Conservez le répertoire d’analyse dans son intégralité lorsque vous partagez ou
  archivez les résultats.

### Exécutez directement les workflows de génération de rapports

- Utilisez `$codex-security:vulnerability-writeup` pour transformer des documents de divulgation,
  des constats préliminaires, des PoCs et du code source en rapports aboutis, sans avoir à
  lancer au préalable une analyse Codex Security.
- Utilisez `$codex-security:propose-security-hardening` pour élaborer des options structurelles ou architecturales
  étayées par des preuves à partir d’analyses, de constats, de documents d’incident ou
  d’évaluation et de code source.

### Appliquez de manière cohérente les consignes du dépôt et la couverture d’analyse

- Définissez le contexte du modèle de menaces, les invariants de sécurité, les critères
  de signalement des constats, les exclusions et les éléments de contexte liés à la gravité dans des fichiers `SECURITY.md`
  situés à la racine ou dans des sous-répertoires. Le fichier applicable le plus proche prévaut.
- Améliorez la couverture de la revue du dépôt avant la validation, sans perdre la trace des surfaces dont l’examen a été explicitement reporté ni des lacunes dans les preuves.
- Examinez les fichiers source supprimés lors des analyses de modifications et élargissez la couverture par défaut de la revue du dépôt avant la validation.
- Avant de lancer une analyse approfondie, vérifiez les Skills de ses différentes phases, les agents délégués et leur capacité disponible.

## 0.1.10 (23 juin 2026)

### Améliorez la prise en charge des tickets Jira et Linear

- Demandez confirmation avant d’importer des sous-tickets Linear et préservez les relations parent-enfant dans les résultats.
- Distinguez l’absence de connexions, les autorisations insuffisantes, les tickets inaccessibles et les défaillances temporaires des connecteurs.
- Interrompez le processus au lieu de produire un verdict lorsque le contenu du ticket demandé n’est pas disponible.
- Attribuez des rangs entiers positifs uniques à partir de `1` dans chaque file de constats confirmés
  ou à examiner.

### Examinez les modifications du code de manière plus fiable

- Comparez un commit examiné à son véritable parent et conservez la cible du diff dans l’espace de travail des constats.
- Signalez que l’état du patch est indisponible au lieu d’examiner une autre modification.
- Examinez des résultats de triage plus cohérents et des constats dont le contexte est présenté de manière plus homogène.

## 0.1.9 (18 juin 2026)

### Examinez les analyses dans l’espace de travail des constats

- Examinez les analyses terminées dans un espace de travail dédié qui regroupe les constats, la couverture, la gravité, le niveau de confiance et les artefacts d’analyse.
- Filtrez et triez les constats, notamment par niveau de confiance décroissant, tout en préservant l’état de votre espace de travail lors des actualisations.
- Ouvrez un constat pour examiner au même endroit les preuves tirées du code source, les détails de validation, l’atteignabilité, l’impact et les recommandations de correction.

### Exécutez des analyses avec moins de configuration

- Exécutez des analyses standard sur des dépôts Git, des dossiers spécifiques ou des bases de code sans historique Git. Les analyses approfondies peuvent aussi cibler un dossier précis.
- Annulez explicitement une analyse en cours, reprenez une analyse interrompue sans nouvelle invite de configuration et recevez un avertissement avant de lancer des analyses approfondies simultanées.
- Suivez plus facilement la configuration et la progression grâce à des états plus clairs, avec des résumés de progression plus compacts et des erreurs qui restent visibles jusqu’à ce que vous les corrigiez.

### Exportez des résultats portables et vérifiables

- Utilisez un format cohérent pour les analyses terminées, comprenant un manifeste, des constats structurés, des données de couverture et un rapport Markdown dérivé du même résultat canonique.
- Exportez les constats aux formats JSON, CSV ou SARIF pour les analyser, les archiver et les intégrer à d’autres outils de sécurité.
- Terminez les analyses de manière plus fiable, notamment lorsque des chemins Windows ou le verrouillage des analyses affectent l’accès au système de fichiers.

### Triez et suivez les constats existants

- Triez les constats existants issus de scanners, d’avis de sécurité, de rapports de bug bounty, de GitHub, de Jira, de Linear ou de résultats de Codex Security en les confrontant à la base de code actuelle. Le workflow de triage renvoie un verdict étayé par des preuves et une file d’actions classées par ordre de priorité.
- Assurez le suivi des constats validés sélectionnés dans Linear, Jira ou des issues GitHub, ou créez un brouillon privé de GitHub Security Advisory lorsque le dépôt remplit les conditions requises pour un avis de sécurité.
- Examinez les vérifications de doublons, le contexte de la source, la visibilité de la destination et le contenu exact proposé avant d’approuver une opération d’écriture. Codex relit le résultat après sa création ou sa mise à jour afin de le vérifier.

## 0.1.7 (4 juin 2026)

### Menez des révisions de sécurité étayées par des preuves

- Analysez un dépôt autorisé ou un dossier sélectionné à la recherche de vulnérabilités de sécurité.
- Effectuez plusieurs cycles de découverte sur l’ensemble d’un dépôt lorsque vous avez besoin d’une couverture plus exhaustive.
- Examinez les pull requests, les commits, les différences entre branches et les patchs locaux afin de détecter les régressions de sécurité.
- Soumettez chaque constat potentiel aux étapes de modélisation des menaces, de découverte des constats, de validation et d’analyse de l’impact avant de générer les rapports d’analyse.
- Corrigez un constat accepté avec un patch ciblé, des tests de non-régression et une vérification du problème d’origine.
