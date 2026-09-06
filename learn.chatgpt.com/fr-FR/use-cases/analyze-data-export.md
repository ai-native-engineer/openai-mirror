<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/analyze-data-export -->

## Avant de commencer

Joignez un fichier CSV ou une feuille de calcul, ou connectez Google Drive et collez dans la discussion l’URL exacte de Google Drive ou Google Sheets. Sites peut transformer ces sources en tableau de bord privé et interactif sans le publier ni rendre vos données publiques.

Vous pouvez créer le tableau de bord dans ChatGPT Work depuis le navigateur ou l’application de bureau. Pour qu’une vérification planifiée continue lorsque votre ordinateur portable est éteint, lancez la tâche dans le navigateur. Une tâche lancée depuis l’application de bureau exige que votre ordinateur soit allumé et que l’application de bureau soit en cours d’exécution.

## Ce que vous obtiendrez

ChatGPT vérifie les données sources, crée un tableau de bord et affiche les chiffres qui sous-tendent les graphiques. Cet exemple utilise des exports trimestriels fictifs de données de vente, une table de correspondance des segments de clientèle et un aperçu représentatif du tableau de bord. Il distingue la plus forte variation en valeur de la plus forte variation en pourcentage et signale une commande qui ne peut être associée à aucun segment de clientèle.

<div data-use-case-export-only>

### Exemple de tableau de bord

| Segment de clientèle | Chiffre d’affaires du T1 | Chiffre d’affaires du T2 |         Variation |
| ---------------- | ---------: | ---------: | -------------: |
| Entreprise       |     $3,000 |     $2,450 | -$550 (-18.3%) |
| Marché intermédiaire       |     $1,000 |     $1,170 |   +$170 (+17%) |
| PME              |       $400 |       $520 |   +$120 (+30%) |

Le segment Entreprise a enregistré la plus forte variation en valeur, tandis que le segment PME a enregistré la plus forte variation en pourcentage. Une commande du T2 d’un montant de $160 n’a pu être associée à aucun segment de la table de correspondance et a été exclue des totaux par segment. Le tableau de bord privé comprend un graphique comparatif, des filtres par segment et par date, la fraîcheur des données sources et les calculs sous-jacents.

Lorsqu’on lui demande de vérifier la source chaque matin en semaine, ChatGPT met à jour le tableau de bord dès que les données approuvées changent et signale les changements significatifs ou les enregistrements manquants. Il ne publie ni ne partage le tableau de bord sans approbation.

</div>

## Fonctionnement

- **Connectez la source :** joignez un export de données de vente ou une feuille de calcul, ou collez le lien exact vers une feuille Google Sheets approuvée ou un fichier Google Drive approuvé. ChatGPT vérifie les colonnes, les dates et les enregistrements clients avant de tirer des conclusions.
- **Créez le tableau de bord :** Sites transforme les résultats en tableau de bord privé et interactif avec des graphiques, des filtres, la fraîcheur des données sources et les calculs à l’appui.
- **Maintenez-le à jour :** une tâche ChatGPT Work planifiée vérifie la source approuvée chaque jour de semaine et met à jour le tableau de bord lorsque les données changent. Le site ne déclenche pas lui-même les vérifications planifiées.
- **Ne faites remonter que l’essentiel :** demandez à ChatGPT de signaler les changements inhabituels, les enregistrements manquants ou les décisions à examiner. Si rien d’important ne change, il ne doit rien signaler.
- **Vérifiez avant de partager :** examinez d’abord le tableau de bord. Demandez à ChatGPT de ne le partager avec les personnes indiquées qu’après votre approbation de la modification des accès.

## Partagez le tableau de bord

Après avoir vérifié le tableau de bord, demandez à ChatGPT de le partager avec certaines personnes ou de le rendre accessible dans votre espace de travail. Vous pouvez également gérer les accès directement dans [Sites](https://chatgpt.com/sites). Demandez à ChatGPT d’afficher les paramètres de partage actuels et d’attendre votre approbation avant d’inviter qui que ce soit, de publier le tableau de bord ou d’en modifier la visibilité.

Consultez la [documentation de Sites](/fr-FR/codex/sites) pour découvrir les options de partage et d’accès à l’espace de travail.

## Allez plus loin

**Modifiez les données suivies par le tableau de bord**

**Configurez une alerte plus pertinente**

**Préparez un bilan hebdomadaire**
