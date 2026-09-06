<!-- source: https://learn.chatgpt.com/fr-FR/docs/image-inputs -->

Ajoutez des images à un prompt lorsque la tâche nécessite un contexte visuel, par exemple une
capture d’écran montrant une erreur, un design d’interface, un diagramme d’architecture ou une ressource existante. Expliquez
ce que ChatGPT doit examiner et quel résultat vous souhaitez obtenir ; ne comptez pas uniquement sur l’image
pour expliquer la tâche.

Faites glisser une image dans la zone de saisie du prompt tout en maintenant la touche <kbd>Maj</kbd> enfoncée pour l’ajouter
au contexte. Vous pouvez également demander à ChatGPT d’examiner une image sur votre système ou utiliser
un outil de capture d’écran pour vérifier le résultat dans une autre application.

Joignez, collez ou faites glisser une image dans la zone de saisie de ChatGPT sur le Web. Dans le prompt,
indiquez à ChatGPT ce qu’il doit examiner et le résultat que vous souhaitez obtenir à partir de l’image.

Collez une image dans la zone de saisie interactive, ou transmettez un ou plusieurs fichiers en
ligne de commande :

```bash
codex -i screenshot.png "Explain this error and suggest the smallest fix"
codex --image before.png,after.png "Compare these states and list the regressions"

Pour plusieurs images, séparez les chemins par des virgules ou répétez `--image`. Codex
accepte les formats d’image courants, notamment PNG et JPEG.

Faites glisser une image dans la zone de saisie du prompt tout en maintenant la touche <kbd>Maj</kbd> enfoncée afin que
l’extension accepte le glisser-déposer au lieu de le transmettre à l’éditeur.

## Rédigez le prompt en fonction de l’image

Indiquez ce que montre l’image, désignez la zone pertinente, puis précisez le résultat attendu
et les contraintes. Si vous joignez plusieurs images, identifiez-les et expliquez
comment ChatGPT doit les comparer.

Par exemple :

```text
Compare this checkout screen with the design. Fix spacing and typography only;
do not change behavior. Verify the result with a new screenshot.

## Utilisez la fonctionnalité d’image appropriée

Utilisez une entrée d’image pour demander à ChatGPT d’examiner une référence visuelle. Utilisez
la [génération d’images](/fr-FR/codex/image-generation) pour demander à ChatGPT de
créer ou modifier une image.
