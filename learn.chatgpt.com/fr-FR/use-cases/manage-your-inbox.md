<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/manage-your-inbox -->

## Avant de commencer

Vous pouvez réaliser cette tâche dans ChatGPT Work depuis un navigateur ou l’application de bureau. Avant de commencer :

- **Connectez votre messagerie.** Installez le [plugin Gmail ou Outlook Email](/fr-FR/docs/plugins). Vous pouvez également connecter Slack, Google Drive et votre calendrier afin de fournir davantage de contexte à ChatGPT lorsqu’il rédige des réponses.
- **Choisissez où s’exécutent les vérifications planifiées.** Commencez dans le navigateur si vous souhaitez que les vérifications continuent lorsque votre ordinateur portable est éteint. Si vous utilisez l’application de bureau, laissez votre ordinateur allumé et l’application de bureau ChatGPT ouverte. Les conversations vocales ne prennent pas en charge les [tâches planifiées](/fr-FR/docs/automations) ; configurez-les ou gérez-les plutôt dans une discussion.

## À quoi vous attendre

ChatGPT examine les e-mails récents, repère les messages qui nécessitent votre attention, propose un nettoyage et prépare des réponses sans les envoyer. Une fois le nettoyage approuvé, il peut appliquer ces modifications aux e-mails plus anciens en attente. Voici à quoi cette conversation peut ressembler :

<div data-use-case-export-only>

J’ai examiné votre boîte de réception professionnelle connectée, principalement consacrée aux lancements de produits, à la documentation et au travail de production. Elle compte **116 messages, dont 96 non lus** ; la plupart des e-mails non lus concernent l’activité des projets, les mises à jour du calendrier, les notifications de fichiers partagés et les newsletters.

### Éléments nécessitant votre attention

- **Préparation de l’enregistrement :** envoyez les sujets de démonstration demandés, une courte biographie et une photo avant la session de demain.
- **Révision de la documentation :** traitez les retours sur l’exactitude des informations produit avant que le guide ne passe à l’étape suivante.
- **Échec du déploiement de l’aperçu :** analysez l’échec du build avant de vous appuyer sur les modifications actuelles.
- **Tâche relative aux avantages sociaux :** effectuez la modification en attente concernant les avantages sociaux.
- **Alerte de connexion :** vérifiez si vous êtes à l’origine de la connexion récente et, dans le cas contraire, suivez les instructions de l’alerte.

### Nettoyage

J’attribuerais les libellés `Project activity`, `Calendar` et `Docs` aux notifications courantes liées aux projets, au calendrier et aux documents, puis je les archiverais ; les e-mails archivés restent accessibles via la recherche. Les demandes directes, les révisions en cours, les builds en échec, les alertes de sécurité et tout élément non résolu resteraient visibles. Les newsletters et autres abonnements récurrents méritent d’être examinés séparément.

### Une réponse à l’organisateur de l’enregistrement

L’organisateur de l’enregistrement attend les sujets de démonstration, une courte biographie et une photo. J’ai consulté les dernières informations de planification et rédigé une réponse dans votre style :

> J’ai hâte d’y être. Je prévois de présenter les trois flux de travail dont nous avons discuté et je vous enverrai la biographie et la photo aujourd’hui. J’ai bien vu l’invitation mise à jour dans le calendrier ; je vais donc m’organiser en fonction du nouvel horaire.

Dorénavant, je vérifierai votre messagerie à **8 h et à 16 h en semaine**. Je signalerai les e-mails nouveaux ou modifiés qui nécessitent votre attention, consulterai les sources connectées comme la messagerie, les documents ou votre calendrier lorsque cela est pertinent, et préparerai des réponses dans votre style. Vous pouvez me réorienter à tout moment en répondant ici.

### Que souhaitez-vous que je fasse ?

1. **Appliquer le nettoyage ?** Oui / non. Les messages courants recevront un libellé et seront archivés, mais pas supprimés.
2. **Enregistrer la réponse comme brouillon ?** Oui / non.
3. **Conserver les horaires et priorités proposés ?** Oui / non.

Répondez « 1 oui, 2 oui, 3 non » et indiquez les modifications souhaitées.

</div>

**Avertissement :** Le plugin Gmail peut déplacer des e-mails vers la Corbeille lorsque vous le demandez explicitement. Examinez d’abord les groupes proposés et quelques exemples de messages. En cas de doute, archivez les messages au lieu de les supprimer. Les actions disponibles peuvent varier selon le plugin de messagerie et les paramètres de l’espace de travail.

## Fonctionnement

Un flux de travail de messagerie se compose de plusieurs éléments :

- **Contexte fourni par les outils connectés :** les plugins permettent à ChatGPT de lire vos e-mails et de consulter d’autres outils connectés lorsqu’une réponse nécessite davantage de contexte. Slack peut contenir la conversation ou la décision la plus récente, Google Drive des fichiers ou des documents de projet pertinents, et votre calendrier peut préciser certaines dates ou réunions.
- **Priorités :** vous pouvez indiquer à ChatGPT les personnes, demandes, alertes et messages récurrents à privilégier ou à ignorer. Les vérifications ultérieures pourront suivre ces instructions.
- **Actions soumises à approbation :** ChatGPT propose un nettoyage et prépare des brouillons de réponse, mais attend votre approbation avant d’agir.
- **Tâches planifiées :** plutôt que d’attendre votre retour et une nouvelle demande, ChatGPT peut rechercher les nouveaux messages dans la même tâche, selon un calendrier défini.

## Créez votre propre flux de travail de messagerie

Vous pouvez être plus précis si vous savez déjà ce que vous voulez. Un prompt pour les **e-mails professionnels**
peut mettre l’accent sur les conversations actives, les demandes, les approbations et le contexte
des projets :

Un prompt pour les **e-mails personnels** pourrait plutôt mettre l’accent sur les personnes de votre entourage, les factures,
les colis, les voyages, les rendez-vous et les alertes de compte :

Les deux exemples suivent la même structure de base : ce qu’il faut vérifier, ce qui compte, ce qu’il faut faire, quand le faire et les actions qui nécessitent une approbation.

## Pour aller plus loin

Une fois le workflow de base opérationnel, vous pouvez l’affiner ou demander à ChatGPT de prendre en charge d’autres tâches utiles liées aux e-mails.

**Vérifiez toujours le contexte pertinent**

**Rédigez un point d’avancement récurrent**

**Relancez les e-mails restés sans réponse**

**Modifiez le format**

**Indiquez-lui ce qui compte**

**Ajustez la rédaction des réponses**

**Modifiez les horaires de vérification**

Exigez une approbation pour les actions de tri et de réponse jusqu’à ce que vous ayez confiance dans les règles.

Les actions Gmail et Outlook ainsi que les tâches planifiées dépendent de votre abonnement et des paramètres de votre espace de travail.
