<!-- source: https://learn.chatgpt.com/fr-FR/docs/features/codex-micro -->

<div class="grid gap-6 lg:grid-cols-2 lg:items-start lg:gap-10">
  <div class="min-w-0 [&_p]:!mt-0">

Codex Micro est le fruit d’une collaboration en série limitée entre Codex et Work Louder. Il
fonctionne avec l’application de bureau ChatGPT et vous permet de consulter rapidement vos discussions,
de passer de l’une à l’autre, d’utiliser la saisie vocale et de déclencher des actions courantes ou des Skills sans
quitter le clavier.

  </div>
  <div class="min-w-0">
    
      
    
  </div>
</div>

## Configurer Codex Micro

1. Ouvrez l’application de bureau ChatGPT.
2. Appuyez une fois sur le bouton arrière pour allumer Codex Micro.
3. Connectez-le à l’aide d’un câble USB-C ou [appairez-le en Bluetooth](#pair-with-bluetooth),
   puis suivez la procédure de configuration qui s’affiche lorsque ChatGPT le détecte.
4. Sur macOS, autorisez **Surveillance de l’entrée** lorsque vous y êtes invité, afin que ChatGPT puisse réagir aux
   appuis sur les touches.
5. Ouvrez **Paramètres \> Codex Micro** pour choisir ce que les touches Agent doivent suivre ou
   déclencher, personnaliser les touches Commande, le stick analogique et la molette, et régler
   l’éclairage et les commandes vocales.

Par défaut, maintenez brièvement la molette enfoncée pour ouvrir ces paramètres. Vous
pouvez également sélectionner l’icône Micro à côté du nom de votre compte, en bas de ChatGPT.
Une affectation personnalisée de la molette peut remplacer ce raccourci d’appui prolongé.

Les paramètres de l’appareil restent disponibles après la première détection d’un Micro compatible
par ChatGPT. Work Louder Input n’est pas requis pour l’intégration à ChatGPT.
Utilisez-le pour personnaliser les commandes d’autres applications ou configurer des couches supplémentaires.

## Appairer en Bluetooth

Codex Micro propose trois canaux Bluetooth.

1. Appuyez une fois sur le bouton arrière pour allumer le Micro.
2. Maintenez la commande tactile située sur le bord inférieur gauche enfoncée pendant trois secondes.
L’éclairage sous le Micro devient bleu lorsque le mode Bluetooth est actif.
3. Appuyez brièvement sur la commande tactile pour choisir le canal Bluetooth 1, 2 ou 3. Si le voyant du canal
clignote rapidement, le Micro est prêt pour l’appairage.
4. Ouvrez les réglages Bluetooth de votre ordinateur et connectez le Micro lorsqu’il
apparaît.
5. Attendez que le voyant du canal reste allumé en continu, ce qui indique que l’appairage est terminé.

Le sélecteur de connexion se ferme après cinq secondes sans interaction. Pour passer à
un autre canal déjà appairé, rouvrez le sélecteur, choisissez le canal et attendez
qu’il se ferme. Pour appairer de nouveau ce canal, maintenez la commande tactile enfoncée
pendant trois secondes, jusqu’à ce que son voyant commence à clignoter.

Pour utiliser plutôt l’USB-C, ouvrez le sélecteur de connexion et touchez la commande tactile
jusqu’à ce que l’éclairage sous le Micro devienne blanc. Si vous branchez un câble USB-C alors que
le Micro est encore en mode Bluetooth, il se recharge, mais ne bascule pas vers la
connexion filaire.

Pour consulter les schémas du matériel, reportez-vous au [guide de configuration de Codex Micro
de Work Louder](https://worklouder.cc/openai-micro-setup).

<a id="read-and-switch-tasks-with-agent-keys"></a>

## Consulter les discussions et passer de l’une à l’autre avec les touches Agent

Chacune des six touches Agent au fini dépoli peut suivre une discussion et s’illuminer pour indiquer son
état actuel. Appuyez une fois sur une touche Agent pour passer à cette discussion sans faire passer
ChatGPT au premier plan. Appuyez deux fois dessus en moins de 350 millisecondes pour changer de discussion et
faire passer la fenêtre ChatGPT au premier plan. Pour que ChatGPT passe au premier plan dès le premier appui, activez
**Mettre ChatGPT au premier plan d’un seul appui** dans les paramètres de l’appareil.

| Voyant | État           | Signification                                   |
| ----- | ---------------- | ----------------------------------------- |
| Blanc | Inactif             | La discussion est inactive.                         |
| Bleu  | Réflexion en cours         | ChatGPT travaille.                       |
| Vert | Terminé         | La discussion est terminée et comporte une mise à jour non lue. |
| Ambre | Intervention requise   | ChatGPT attend votre approbation ou votre réponse.  |
| Rouge   | Erreur            | Une erreur s’est produite.                     |
| Éteint   | Aucune discussion affectée | La touche ne suit aucune discussion.            |

La touche associée à la discussion sélectionnée émet des pulsations lumineuses de la couleur correspondant à son état.

Par défaut, les touches suivent vos six discussions mises à jour le plus récemment, qu’elles soient épinglées
ou non. Dans les paramètres de l’appareil, modifiez **Touches Agent** pour utiliser une
autre organisation :

- **Discussions les plus récentes** : suivez les six discussions mises à jour le plus récemment, épinglées ou
  non.
- **Discussions épinglées** : suivez les six premières discussions de **Épinglées**.
- **Discussions prioritaires** : placez en premier les discussions en attente d’une intervention, les discussions non lues et les
  discussions actives.
- **Affectations personnalisées** : affectez à chaque touche Agent une discussion, un raccourci, une action de touche physique ou un
  Skill activé. Appuyez sur une touche Agent non affectée pour ouvrir une nouvelle discussion.
  Lorsque vous démarrez la discussion, ChatGPT l’affecte à cette touche.

Les couleurs d’état ne changent pas pour les touches qui suivent des discussions. Avec le réglage **Affectations
personnalisées**, une touche Agent peut plutôt déclencher une action.

## Utiliser et personnaliser les touches Commande

Codex Micro propose six actions dans sa disposition par défaut :

<div class="grid gap-6 md:grid-cols-[minmax(0,1fr)_minmax(16rem,42%)] md:items-start">
  <div class="min-w-0 [&_table]:!mt-0 [&_td:first-child]:!px-2 [&_th:first-child]:!px-2 md:order-2">

|                            Touche                            | Action par défaut                           |
| :-------------------------------------------------------: | ---------------------------------------- |
|     | Activez ou désactivez le mode Rapide.                |
|  | Approuvez la demande en cours.             |
|   | Refusez la demande en cours.             |
|    | Poursuivez la discussion actuelle dans une nouvelle discussion. |
|       | Démarrez la fonction Appuyer pour parler.                      |
|   | Envoyez le message depuis la zone de saisie.        |

  </div>
  <div class="min-w-0 md:order-1">

La touche Micro utilise le microphone de votre ordinateur. Codex Micro n’a pas de
microphone intégré. Par défaut, elle utilise **Appuyer pour parler** : maintenez la touche enfoncée pendant que
vous parlez, puis relâchez-la pour arrêter. Pour enregistrer sans maintenir la touche, appuyez deux fois dessus
en moins de 350 millisecondes afin que l’enregistrement continue. Appuyez de nouveau dessus pour l’arrêter.

Une lumière vert d’eau parcourt le clavier pendant l’enregistrement. Elle devient une
lumière blanche animée pendant que ChatGPT traite votre voix, puis passe au blanc fixe
lorsque le prompt est prêt. Appuyez sur la touche Codex pour l’envoyer.

Si **Discussion vocale** est disponible sous **Touche du microphone**, sélectionnez cette option pour utiliser la
touche Micro afin de démarrer une discussion vocale ou d’activer ou désactiver votre microphone ; maintenez-la enfoncée pour
mettre fin à la discussion. Activez **Utiliser des touches de microphone distinctes** pour attribuer séparément une action aux deux contacteurs
situés sous la large touche Micro.

Dans les paramètres de l’appareil, sélectionnez une touche Commande dans l’aperçu **Disposition**, puis
choisissez son capuchon et son action. Vous pouvez ouvrir le navigateur ou le terminal, gérer
les discussions, examiner les modifications, exécuter des actions Git et de pull request, joindre des fichiers ou des photos,
ouvrir les Plugins ou les Tâches planifiées, modifier l’effort de raisonnement, exécuter une skill activée,
ou attribuer un autre raccourci. Si vous choisissez un capuchon de touche déjà utilisé
ailleurs, ChatGPT intervertit les deux au lieu d’utiliser deux fois le même capuchon.

Après avoir reconfiguré une touche, remplacez son capuchon physique par celui qui correspond à sa nouvelle action.
Sélectionnez **Réinitialiser la disposition** pour restaurer les attributions par défaut des touches Commande et du joystick analogique
sans modifier le mode des touches Agent ni les attributions personnalisées des discussions.

  </div>
</div>

## Utilisez le joystick analogique et la molette

<div class="grid gap-6 md:grid-cols-[minmax(0,1fr)_minmax(16rem,42%)] md:items-start">
  <div class="min-w-0">

Le joystick analogique se déplace librement dans toutes les directions. Lorsque vous l’éloignez suffisamment
du centre, ChatGPT convertit le mouvement en l’une des quatre actions directionnelles
possibles. Codex Micro utilise initialement les attributions présentées ici.

Dans les paramètres de l’appareil, choisissez une commande disponible de l’application de bureau ChatGPT ou une skill activée pour chaque
direction.

  </div>
  <div class="min-w-0 [&_table]:!mt-0">

| Direction | Action par défaut             |
| --------- | -------------------------- |
| Haut        | Activez ou désactivez le Mode plan.  |
| Droite     | Avancez dans l’historique de l’application. |
| Bas      | Affichez ou masquez la barre latérale.  |
| Gauche      | Revenez en arrière dans l’historique de l’application.    |

  </div>
</div>

Par défaut, la molette utilise le mode **Navigation dans la zone de saisie**. Tournez-la pour parcourir
les commandes et options de la zone de saisie, puis appuyez dessus pour ouvrir ou sélectionner l’élément
actif. Lorsqu’une commande ou un menu de la zone de saisie est ouvert, la touche Agent située juste
à droite de la molette s’allume en rouge. Appuyez sur cette touche pour annuler.

Choisissez l’un des quatre modes de la molette dans les paramètres de l’appareil :

| Mode                       | Comportement                                                                       |
| -------------------------- | ------------------------------------------------------------------------------ |
| **Navigation dans la zone de saisie**    | Parcourez les commandes de la zone de saisie et sélectionnez la commande active.                 |
| **Raisonnement uniquement**         | Réglez l’effort de raisonnement et ouvrez le curseur ou les options avancées correspondantes.               |
| **Défilement de la discussion** | Faites défiler la discussion active ; appuyez sur la molette pour accéder au message le plus récent.          |
| **Attributions personnalisées**     | Attribuez une action ou une skill à la rotation vers la gauche, à la rotation vers la droite, à l’appui et à l’appui prolongé. |

Un appui prolongé sur la molette ouvre les paramètres de l’appareil dans tous les modes sauf
**Attributions personnalisées**, où il déclenche l’action attribuée à l’appui prolongé.

## Réglez l’éclairage

{/* vale Microsoft.Auto = NO */}

Dans les paramètres de l’appareil, réglez **Luminosité** et choisissez pour **Atténuation automatique**
un délai compris entre 30 secondes et une heure, ou désactivez l’atténuation automatique. L’éclairage
se rallume lorsque vous utilisez le Micro ou qu’une touche Agent change d’état. Par défaut,
il s’éteint au bout de trois minutes.

{/* vale Microsoft.Auto = YES */}

Lorsque le Micro indique l’état de sa batterie, vous pouvez le consulter dans les paramètres de l’appareil
et à côté de l’icône Micro dans la barre latérale.

## Ajoutez d’autres couches

ChatGPT utilise la couche 1. Utilisez [Work Louder
Input](https://worklouder.cc/micro-setup) pour configurer jusqu’à cinq couches supplémentaires
avec des raccourcis et des actions pour d’autres applications.

## Résolvez les problèmes liés à Codex Micro

### Corrigez les problèmes de surveillance de l’entrée sur macOS

Si les paramètres de l’appareil indiquent que la surveillance de l’entrée n’est pas configurée, sélectionnez **Ouvrir
Réglages Système**, puis suivez ces étapes :

1. Ouvrez **Réglages Système \> Confidentialité et sécurité \> Surveillance de l’entrée**.
2. Activez l’accès pour ChatGPT s’il figure déjà dans la liste. S’il n’y figure pas, faites glisser
**ChatGPT** depuis Applications vers la liste, ou sélectionnez **Ajouter (+)**, puis choisissez
**ChatGPT**.
3. Quittez et rouvrez ChatGPT, puis vérifiez qu’il détecte le Micro sur la couche 1.

Pour en savoir plus sur cette autorisation macOS, consultez le [guide d’Apple sur la surveillance
de l’entrée](https://support.apple.com/guide/mac-help/mchl4cedafb6/mac).

### Résolvez les interférences de connexion

ChatGPT réessaie automatiquement lorsqu’il détecte un Micro, mais ne parvient pas à s’y connecter ou perd
la communication. Si le problème persiste, reconnectez le Micro et vérifiez si
un utilitaire de clavier ou un outil de sécurité en bloque l’accès.

{/* vale Vale.Spelling = NO */}

Sur macOS, Work Louder indique que Karabiner et Logitech Options+ peuvent perturber
la communication avec le Micro lorsque ces applications disposent de l’autorisation Surveillance de l’entrée. Pour
détecter les interférences, quittez l’utilitaire de clavier ou retirez-lui temporairement
l’autorisation Surveillance de l’entrée, puis reconnectez le Micro. Si votre organisation gère
votre ordinateur, demandez à votre administrateur informatique de vérifier les règles appliquées à l’appareil.

{/* vale Vale.Spelling = YES */}

### Obtenez davantage d’aide auprès de Work Louder

Pour obtenir de l’aide sur le Bluetooth, les câbles, l’alimentation ou la réinitialisation du clavier, consultez le [guide de configuration de Codex Micro de Work
Louder](https://worklouder.cc/openai-micro-setup). Pour
contacter directement l’assistance, écrivez à
[hello@worklouder.cc](mailto:hello@worklouder.cc).

## Procurez-vous un Micro compatible

Vérifiez la disponibilité de Codex Micro sur le site [OpenAI Supply
Co](https://openai.com/supply/co-lab/work-louder/). L’application de bureau ChatGPT prend également
en charge [Creator Micro 2](https://worklouder.cc/creator-micro-2), disponible
directement auprès de Work Louder.
