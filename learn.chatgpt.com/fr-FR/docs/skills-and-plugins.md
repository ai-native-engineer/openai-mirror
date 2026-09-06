<!-- source: https://learn.chatgpt.com/fr-FR/docs/skills-and-plugins -->

Les skills et les plugins aident ChatGPT et Codex à effectuer des tâches récurrentes avec les
instructions, les ressources et les outils appropriés. Ils évitent d’avoir à coller le
même prompt, modèle, ensemble d’exigences ou processus dans chaque discussion.

- Un **skill** regroupe des instructions et des ressources complémentaires pour une
  tâche ou un flux de travail spécifique.
- Un **plugin** est un package installable qui peut inclure des skills, des connecteurs ou
  les deux. Les connecteurs s’appuient sur des serveurs Model Context Protocol (MCP) et peuvent
  inclure en option une interface utilisateur ChatGPT personnalisée.

## Utilisez les skills pour les tâches récurrentes

Un skill est un flux de travail réutilisable qui fournit à ChatGPT ou Codex des consignes
propres à une tâche. Il peut formaliser la manière dont vous effectuez déjà les tâches récurrentes afin que l’un ou l’autre
produit suive le même processus chaque fois que cette tâche se présente.

Un skill peut combiner :

- Un nom et une description qui aident ChatGPT et Codex à déterminer dans quels cas le skill
s’applique.
- Des instructions de flux de travail qui définissent le processus et le résultat attendu.
- Des ressources complémentaires, comme des modèles, des exemples, des consignes de marque, des schémas
ou des outils connectés.

Les skills sont particulièrement utiles lorsque de bons résultats reposent sur une méthode reproductible. Par
exemple, un skill peut préparer une synthèse quotidienne, réviser de la documentation, créer une
présentation, appliquer une norme rédactionnelle d’équipe ou recueillir des informations auprès des
mêmes outils connectés chaque semaine.

Utilisez les skills pour gagner en cohérence, intégrer les bonnes pratiques de l’équipe au
flux de travail et partager un processus standardisé plutôt que de dépendre de connaissances
non documentées.

ChatGPT et Codex peuvent choisir un skill lorsque votre demande correspond à son objectif. Vous
pouvez aussi en sélectionner un explicitement. ChatGPT permet de mentionner les skills avec `@`, tandis que Codex
permet de le faire avec `$`.

## Créer des skills

Vous pouvez commencer par transformer une tâche que vous effectuez déjà régulièrement en un mode opératoire précis pour
ChatGPT et Codex. Pour un premier skill, pensez à un bilan hebdomadaire, à un brief de campagne,
à un suivi de réunion ou à toute autre tâche dont les étapes et le format doivent rester
cohérents.

Pour créer un skill utile :

1. **Choisissez une tâche bien définie.** Recensez vos éléments de départ habituels, comme les
   fichiers, les liens ou les notes, puis décrivez le résultat final attendu.
2. **Décrivez le flux de travail.** Dans ChatGPT, commencez par `@skill-creator` ; dans Codex,
   utilisez `$skill-creator`. Expliquez l’objectif, les étapes à suivre, le format
   attendu, ainsi que tout ce que le skill doit systématiquement inclure ou éviter. Ajoutez un modèle
   ou un bon exemple si vous en avez un.
3. **Passez le brouillon en revue et testez-le.** Vérifiez les instructions, testez le skill avec une
   demande réaliste et affinez-le si le résultat omet une étape ou s’écarte
   du format souhaité.
4. **Installez-le et réutilisez-le.** Une fois le skill activé, ChatGPT ou Codex peut l’utiliser
   pour les demandes pertinentes, ou vous pouvez le sélectionner explicitement. Vous pouvez également
   le partager avec les membres de votre équipe si les paramètres de votre espace de travail l’autorisent.

Pour en savoir plus sur la création de skills, consultez le guide dédié ci-dessous.

  
    <span slot="icon">
      
    </span>
    Créez, testez et partagez des skills réutilisables avec ChatGPT et Codex.
  

## Utilisez les plugins pour les outils et les flux de travail partagés

Les plugins facilitent l’installation et le partage de fonctionnalités réutilisables. Un plugin peut
combiner des skills avec des connecteurs pour des services tels que GitHub, Google Drive ou
Slack, et inclure des serveurs MCP donnant accès à des outils et à du contexte supplémentaires.

ChatGPT et Codex partagent le même catalogue universel de plugins. Parcourez-le lorsque vous souhaitez
ajouter un flux de travail existant plutôt que d’en créer un vous-même. Après avoir installé
un plugin, décrivez directement la tâche ou choisissez explicitement un plugin ou un
skill inclus à l’aide de la syntaxe d’appel propre à votre interface.

[Apprenez à installer et à utiliser les plugins](/fr-FR/codex/plugins).

## Choisissez entre un skill et un plugin

Utilisez un skill lorsque vous avez besoin d’instructions réutilisables pour une tâche précise. Utilisez un
plugin si vous souhaitez un package installable pouvant combiner des instructions avec des
services connectés ou d’autres outils.

Vous pouvez également faire la démonstration d’un flux de travail avec
[Enregistrer et rejouer](/fr-FR/codex/extend/record-and-replay), qui convertit l’enregistrement en un
skill réutilisable. Pour créer et distribuer votre propre package, consultez
[Créer des plugins](https://developers.openai.com/plugins/build/plugins).

Si votre plugin doit se connecter à un service ou exposer des outils MCP, consultez
[Créer un serveur MCP](https://developers.openai.com/plugins/build/mcp-server). Lorsque votre plugin est prêt pour une révision publique,
consultez [Soumettre des plugins](https://developers.openai.com/plugins/deploy/submission).

Pour découvrir d’autres exemples de flux de travail réutilisables, consultez [Utiliser les skills dans OpenAI
Academy](https://openai.com/academy/skills/).
