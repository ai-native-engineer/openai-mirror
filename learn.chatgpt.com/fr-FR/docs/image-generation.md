<!-- source: https://learn.chatgpt.com/fr-FR/docs/image-generation -->

Demandez à ChatGPT de générer ou de modifier des images. Utilisez la génération d’images pour les ressources d’interface utilisateur,
les bannières, les arrière-plans, les illustrations, les planches de sprites et les espaces réservés que vous souhaitez
créer parallèlement au code ou dans une discussion ChatGPT.

Demandez une image depuis la zone de saisie de l’application. Ajoutez une image de référence lorsque vous souhaitez
que ChatGPT transforme une ressource existante ou s’en serve de guide visuel.

### Examiner et modifier les images générées

Sélectionnez une image générée pour l’ouvrir dans une visionneuse agrandie. Basculez entre
**Vue ciblée** pour examiner une seule image et **Vue canvas** pour voir les images
générées au cours de la même discussion.

Dans la **Vue canvas**, utilisez **Commenter** pour ajouter des commentaires précis à une ou plusieurs
images. Sélectionnez **Sélection multiple** pour choisir les images à inclure, puis
envoyez vos commentaires et toute instruction de modification supplémentaire dans la même discussion.
Décrivez ce qui doit changer et ce qui doit rester inchangé.

Demandez une image dans une discussion de la version web de ChatGPT. Joignez une image de référence dans la
zone de saisie si vous souhaitez que ChatGPT la modifie ou s’en serve de guide visuel.

Décrivez l’image dans une session interactive ou incluez `$imagegen` pour appeler
explicitement le skill de génération d’images. Joignez une image existante avec `-i` ou
`--image` si elle doit servir de guide pour le résultat.

Demandez une image dans la discussion de l’extension. Faites glisser une image de référence dans
la zone de saisie tout en maintenant la touche <kbd>Shift</kbd> enfoncée si vous souhaitez que Codex modifie une ressource
existante ou s’appuie dessus.

## Générer ou modifier une image

Décrivez l’image en langage naturel. Ajoutez une image de référence si vous souhaitez
que ChatGPT transforme ou étende une ressource existante.

Incluez `$imagegen` dans votre prompt pour appeler explicitement le skill de génération
d’images.

La génération d’images intégrée utilise `gpt-image-2` et est prise en compte dans vos limites générales
d’utilisation de Codex. En moyenne, les générations d’images consomment les quotas inclus 3 à 5 fois plus
vite que des interactions similaires sans génération d’images, selon la qualité
et la taille de l’image. Pour les lots plus importants, définissez `OPENAI_API_KEY` dans votre environnement et demandez
à ChatGPT de générer des images via l’API afin que les tarifs de l’API s’appliquent.

La disponibilité de la génération d’images et les limites d’utilisation dans la version web de ChatGPT dépendent de votre offre et des
paramètres de votre espace de travail. Pour générer des images par programmation, utilisez cette [API de
génération d’images](/api/docs/guides/image-generation).

## Rédiger des prompts d’image efficaces

Un prompt d’image efficace se limite souvent à une à trois phrases claires. Décrivez les
détails qui conditionnent la réussite du résultat :

- Expliquez l’objectif de l’image ou le public visé.
- Indiquez le sujet principal et l’action représentée.
- Décrivez le décor, la composition et le style visuel.
- Ajoutez des précisions sur le cadrage, les dimensions, l’éclairage, les couleurs ou les matériaux si ces éléments sont importants.
- Précisez les contraintes, notamment tout élément que l’image ne doit pas contenir.

Préférez des descriptions visuelles concrètes aux appréciations vagues. Par exemple, indiquez
d’où vient la lumière plutôt que de demander un « bel éclairage ». Répétez toute
exigence qui doit rester inchangée.

## Affiner le résultat

Commencez par l’idée centrale, puis apportez de petites modifications ciblées. Ajustez un
élément à la fois pour éviter que la composition et les autres détails importants ne changent.
Vous pouvez également sélectionner une zone précise de l’image et décrire la modification à
lui apporter.

Lorsque vous modifiez une image existante, indiquez précisément ce qui doit changer et ce qui doit
rester identique.

Pour les modifications plus générales, formulez des retours directs et exploitables : rendez l’image
plus lumineuse, réduisez la saturation des couleurs, simplifiez l’arrière-plan ou conservez la
composition tout en changeant le style.

## Utiliser plusieurs images de référence

Utilisez un nombre limité d’images de référence lorsque l’une définit le contenu et
une autre le style, la mise en page ou une autre orientation visuelle. Identifiez chaque
image par son numéro et expliquez comment elles s’articulent. Lorsque vous combinez des éléments, utilisez des termes spatiaux comme
premier plan, arrière-plan, gauche et droite.

## Ajouter du texte à une image

Gardez le texte intégré à l’image court et indiquez-le avec précision. Placez le texte exact entre
guillemets, respectez la casse souhaitée et décrivez son style de police, sa taille, sa couleur et son
emplacement. Pour un nom inhabituel, épelez-le lettre par lettre lorsque
la précision est importante. Indiquez si tout autre texte est autorisé.

## Créer des infographies et des mises en page denses

La génération d’images peut aider à ébaucher des visuels explicatifs, des affiches, des diagrammes légendés,
des chronologies et d’autres visuels riches en informations. Décrivez la hiérarchie des
informations et la mise en page, gardez les libellés concis et demandez un rendu net du texte.
Pour un texte dense ou une typographie dont la qualité est essentielle en production, vérifiez chaque mot et finalisez
le visuel dans un outil de design si nécessaire.

## Autres considérations

- **Utilisez avec prudence l’image de personnes réelles.** Lorsque vous représentez une personne réelle, fournissez une
  photo de référence lorsque cela est pertinent et assurez-vous d’avoir l’autorisation d’utiliser
  son image.
- **Demandez une approche originale.** Demandez une création générique ou originale
  plutôt que d’imiter une marque, un produit, un artiste ou une œuvre en particulier.
- **La mention de la source est facultative.** Vous n’avez pas besoin de créditer OpenAI pour les images générées,
  mais vous pouvez expliquer comment un visuel a été créé lorsque cette information est utile.
- **Respectez les politiques applicables.** Utilisez les images conformément aux directives de votre
  organisation et aux [politiques
  d’utilisation d’OpenAI](https://openai.com/policies/usage-policies/).

## Documentation connexe

- [Tarifs de Codex](/fr-FR/codex/pricing#image-generation-usage-limits)
- [Entrées d’images](/fr-FR/codex/image-inputs)
- [Guide de l’API de génération d’images](/api/docs/guides/image-generation)
- [Utiliser des fichiers](/fr-FR/codex/artifacts-viewer)
- [Créer des images avec ChatGPT](https://openai.com/academy/image-generation/)

  
    <span slot="icon">
      
    </span>
    Découvrez d’autres prompts de génération d’images et leurs résultats.
  

- [Entrées d’images](/fr-FR/codex/image-inputs)
- [Guide de l’API de génération d’images](/api/docs/guides/image-generation)
- [Utiliser des fichiers](/fr-FR/codex/artifacts-viewer)
- [Créer des images avec ChatGPT](https://openai.com/academy/image-generation/)

  
    <span slot="icon">
      
    </span>
    Découvrez d’autres prompts de génération d’images et leurs résultats.
  

- [Tarifs de Codex](/fr-FR/codex/pricing#image-generation-usage-limits)
- [Entrées d’images](/fr-FR/codex/image-inputs)
- [Guide de l’API de génération d’images](/api/docs/guides/image-generation)
- [Utiliser des fichiers](/fr-FR/codex/artifacts-viewer)

  
    <span slot="icon">
      
    </span>
    Découvrez davantage de prompts et de résultats de génération d’images.
