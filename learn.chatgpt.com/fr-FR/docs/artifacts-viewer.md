<!-- source: https://learn.chatgpt.com/fr-FR/docs/artifacts-viewer -->

Lorsqu’une tâche produit un fichier, fournissez à ChatGPT les données sources, le type de fichier attendu,
sa structure et les critères de révision à prendre en compte. Les outils de prévisualisation et de révision
dépendent de l’interface utilisée.

L’application de bureau ChatGPT affiche à côté de la discussion un aperçu des documents, présentations,
feuilles de calcul et fichiers PDF générés. Lorsque les aperçus automatiques sont
activés, l’application peut ouvrir un fichier généré une fois la tâche terminée.

Lorsque les aperçus HTML sont disponibles, les fichiers `.html` et `.htm` générés peuvent également
s’ouvrir sous forme d’aperçus interactifs. Basculez entre l’aperçu du rendu et l’affichage du code
source pour examiner le résultat ou son code HTML sous-jacent.

Utilisez des annotations pour désigner une partie précise d’un aperçu pris en charge et demander
une révision ciblée.

Dans ChatGPT Work sur le Web, joignez les fichiers sources ou demandez à ChatGPT de créer un
document, une présentation, une feuille de calcul ou un fichier PDF. Examinez le fichier généré dans la
discussion, téléchargez-le si nécessaire et fournissez des commentaires ciblés pour la version suivante.

Codex CLI peut créer et modifier des fichiers dans le répertoire de travail, mais n’inclut pas
d’interface visuelle pour les prévisualiser ou les annoter. Demandez à Codex d’indiquer le chemin de chaque
fichier généré, ainsi que les vérifications qu’il a effectuées.

L’extension IDE peut créer et modifier des fichiers dans l’espace de travail. Examinez les fichiers texte et
les fichiers de code dans l’éditeur, puis ouvrez les documents, présentations, feuilles de calcul ou
fichiers PDF dans une visionneuse compatible.

  
    
  

## Créer des fichiers à réviser

Pour les feuilles de calcul et les présentations, décrivez les feuilles, les colonnes, les graphiques,
les sections des diapositives et les vérifications attendues. Demandez à ChatGPT d’expliquer où il a enregistré le
fichier généré et comment il l’a vérifié.

<a id="refine-files-with-annotations"></a>
<span id="follow-artifact-work"></span>
<a id="review-and-refine-files"></a>

## Affiner des fichiers à l’aide d’annotations

Les annotations permettent de désigner une partie précise d’un fichier et d’indiquer à ChatGPT
ce qu’il doit modifier. Le même workflow d’annotation, disponible pour le code, les fichiers Markdown
et les sites web, fonctionne également avec les documents, les feuilles de calcul et les
présentations.

Par exemple, vous pouvez :

- Sélectionnez une barre de navigation sur un site web et demandez à ChatGPT d’en modifier la police.
- Surlignez une affirmation dans une thèse d’investissement et demandez-en la source.
- Annotez un graphique sur une diapositive et demandez un libellé plus clair.

ChatGPT utilise la zone sélectionnée comme contexte de votre demande, ce qui vous permet d’affiner
le fichier sans repartir de zéro ni modifier les parties qui vous conviennent déjà.
Les annotations sont particulièrement utiles après le premier jet, lorsque le travail doit être
révisé et affiné de manière itérative.

## Réviser et affiner des fichiers sur le Web

Ouvrez ou téléchargez le fichier généré pour l’examiner dans la visionneuse appropriée.
Lorsque vous demandez une révision, indiquez la page, la diapositive, la feuille, le tableau ou le passage qui
requiert votre attention et précisez ce qui doit rester inchangé. Demandez à ChatGPT d’indiquer
le nouveau nom du fichier et les vérifications qu’il a effectuées avant de télécharger la
version suivante.

## Réviser et affiner des fichiers

Utilisez la barre latérale de la discussion pendant qu’une tâche s’exécute. Elle peut afficher le plan de l’agent,
les sources, les fichiers générés et le résumé de la discussion afin de vous permettre d’orienter le travail,
d’examiner les fichiers générés et de demander une nouvelle itération.

Demandez à ChatGPT d’expliquer où il a enregistré chaque fichier et comment il a vérifié le
résultat obtenu. Utilisez l’aperçu pour examiner le fichier généré, puis formulez des commentaires ciblés sur
les éléments à reprendre dans la structure, les données, la mise en page ou la validation.

## Documentation associée

- [Génération d’images](/fr-FR/codex/image-generation)
