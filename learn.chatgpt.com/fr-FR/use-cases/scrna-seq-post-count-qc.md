<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/scrna-seq-post-count-qc -->

## Tirez parti des Skills

Le plugin NGS Analysis comprend :

- `ngs-analysis-router`
- `scrna-seq-qc`
- `ngs-scrna-seq`

Lorsque vous utilisez le plugin, ChatGPT peut exploiter tous les Skills qu’il regroupe.

## Guide étape par étape

1. Indiquez à ChatGPT les fichiers appropriés de matrice, de codes-barres et de gènes ou caractéristiques, ainsi que le manifeste et les métadonnées du jeu de données, ou fournissez les références exactes des fichiers.
2. Exécutez le prompt de démarrage afin que ChatGPT choisisse les seuils de contrôle qualité d’après les distributions observées et consigne leur justification dans les artefacts produits par l’exécution.
3. Ouvrez l’index des visualisations et le notebook ou l’application de révision pour examiner le nombre de cellules satisfaisant ou non aux critères de contrôle qualité, les UMAP et le niveau de confiance des annotations.
4. Poursuivez dans la même discussion pour affiner les seuils, fournir un atlas de référence correspondant ou relancer l’analyse après avoir débloqué la détection des doublets.

## Résultats

L’exécution produit une interface de révision des décisions de filtrage, pas seulement une
matrice filtrée. Commencez par les graphiques justifiant les seuils et le récapitulatif du contrôle qualité
pour voir combien de cellules chaque filtre a supprimées ou signalées et
si les seuils retenus correspondent aux distributions observées.

![Examinez les graphiques justifiant les seuils et le nombre de cellules satisfaisant ou non aux critères de contrôle qualité pour une analyse unicellulaire.](/codex/use-cases/scrna-seq-post-count-qc-screenshot-1.webp)

Examinez ensuite les UMAP générées par étiquette générale et par cluster Leiden. Ces
vues facilitent le repérage des annotations manquantes, des clusters suspects ou des
seuils qui nécessitent un nouvel examen.

![Examinez les graphiques UMAP par étiquette générale et par cluster Leiden.](/codex/use-cases/scrna-seq-post-count-qc-screenshot-2.webp)

Enfin, examinez les métriques par cellule et les résultats du filtrage. ChatGPT conserve
ce tableau avec le fichier `.h5ad` filtré et les artefacts de visualisation afin que vous puissiez
ajuster les seuils dans la même discussion sans perdre la justification de la
première passe.

![Ouvrez les métriques de contrôle qualité par cellule et les résultats du filtrage pour les examiner.](/codex/use-cases/scrna-seq-post-count-qc-screenshot-3.webp)
