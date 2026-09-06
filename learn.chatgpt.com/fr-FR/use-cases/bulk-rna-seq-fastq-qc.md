<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/bulk-rna-seq-fastq-qc -->

## Tirez parti des Skills

Le plugin NGS Analysis comprend :

- `ngs-analysis-router`
- `ngs-bulk-rnaseq-counts-qc`
- `ngs-runtime-env`

Lorsque vous utilisez le plugin, ChatGPT peut faire appel à tous les Skills qu’il intègre.

## Guide étape par étape

1. Indiquez à ChatGPT le chemin d’un répertoire contenant la feuille d’échantillons, les fichiers FASTQ, les fichiers FASTA du transcriptome et du génome ainsi que le fichier GTF, ou fournissez les références exactes des fichiers.
2. Exécutez le prompt de démarrage afin que ChatGPT puisse valider la directionnalité, la cohérence des références et la disponibilité des outils avant l’exécution.
3. Ouvrez dans ChatGPT les artefacts MultiQC et les matrices générés afin de vérifier le taux d’alignement, la duplication, la concordance du type de bibliothèque et la disponibilité des ressources.
4. Poursuivez dans la même discussion pour résoudre les points bloquants, relancer l’exécution avec les métadonnées mises à jour ou utiliser les matrices obtenues au niveau des gènes comme entrée pour l’analyse d’expression différentielle en aval.

## Résultats

L’exécution renvoie un ensemble de comptages assorti d’une revue du contrôle qualité plutôt qu’une simple quantification
brute. Commencez par le rapport MultiQC pour repérer les avertissements susceptibles d’affecter
l’interprétation en aval. Dans cet exemple, ChatGPT met en évidence les avertissements FastQC
relatifs au contenu des séquences en parallèle du résumé de l’exécution, afin que l’équipe puisse déterminer
si le profil observé est attendu pour la préparation de la bibliothèque.

![Examinez les avertissements FastQC relatifs au contenu des séquences en parallèle du résumé de l’exécution bulk RNA-seq.](/codex/use-cases/bulk-rna-seq-fastq-qc-screenshot-1.webp)

Examinez ensuite les statistiques Salmon dans le même rapport. Les taux d’alignement,
l’attribution du type de bibliothèque et les indicateurs de duplication permettent d’évaluer rapidement si les données sont prêtes
pour l’analyse d’expression différentielle.

![Examinez les statistiques d’alignement et de type de bibliothèque de Salmon dans le rapport MultiQC généré.](/codex/use-cases/bulk-rna-seq-fastq-qc-screenshot-2.webp)

La matrice de comptage au niveau des gènes obtenue est enregistrée comme artefact réutilisable. Ouvrez-la
dans ChatGPT pour vérifier que les échantillons et les caractéristiques attendus sont présents, puis conservez-la
avec les informations de provenance de l’exécution pour l’analyse en aval.

![Ouvrez la matrice de comptage au niveau des gènes générée afin de l’examiner en vue des analyses en aval.](/codex/use-cases/bulk-rna-seq-fastq-qc-screenshot-3.webp)
