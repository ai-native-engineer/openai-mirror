<!-- source: https://learn.chatgpt.com/fr-FR/docs/prompting -->

<a id="prompts"></a>

## Vue d’ensemble de la conception de prompts

La conception de prompts consiste à indiquer à ChatGPT ce que vous voulez savoir, créer ou modifier. Un prompt
peut être une question, une instruction ou un objectif. Vous n’avez besoin ni d’une syntaxe technique ni
d’une formule rigide. Commencez par formuler votre demande avec vos propres mots, examinez la réponse et utilisez des messages de suivi
pour affiner le résultat.

Un prompt court suffit souvent. Pour les tâches plus vastes ou plus importantes, incluez les
éléments pertinents :

- **Objectif :** Que doit faire ChatGPT ?
- **Contexte :** Quelles informations ou sources seront utiles ?
- **Résultat :** De quel format, de quelle longueur ou de quel niveau de détail avez-vous besoin ?
- **Contraintes :** Que faut-il laisser inchangé ? Que doit éviter ChatGPT ou vérifier
  auprès de vous avant d’agir ?

N’utilisez que les éléments utiles. Vous n’avez pas besoin de tous les renseigner ni de suivre un
format imposé.

## Décrivez le résultat souhaité

Commencez par le résultat, et non par une liste détaillée d’étapes. Précisez le public ou le
format lorsque ces éléments ont une incidence sur ce que ChatGPT doit produire.

```text
Turn these meeting notes into a short update for the project team.
Put the decisions and next steps first.

Ce prompt explique quoi créer et à qui le contenu est destiné. Décrivez le processus lorsque
la manière de procéder elle-même a de l’importance. Sinon, laissez ChatGPT effectuer des recherches, comparer
les informations et adapter son approche.

<a id="context"></a>

## Ajoutez les éléments de contexte utiles

Fournissez les informations susceptibles de modifier le résultat. N’ajoutez que les sources
pertinentes et expliquez ce que ChatGPT doit retenir de chacune.

- Joignez des documents, feuilles de calcul, présentations ou fichiers PDF lorsque vous souhaitez
  que ChatGPT les résume, les compare, les transforme ou [crée des fichiers à réviser](/fr-FR/codex/artifacts-viewer).
- Ajoutez une capture d’écran, un schéma ou une autre [image en entrée](/fr-FR/codex/image-inputs) lorsque
  la tâche dépend du contexte visuel. Indiquez la zone pertinente au lieu de
  vous fier uniquement à l’image.
- Demandez à ChatGPT d’utiliser la [Recherche web](/fr-FR/codex/web-search) lorsque la réponse dépend
  d’informations à jour, et demandez des sources si vous devez vérifier le résultat.
- Utilisez un [projet](/fr-FR/codex/projects) lorsque plusieurs discussions liées doivent partager des fichiers,
  des sources ou un dossier local.

### Utilisez des sources connectées

Lorsque ChatGPT a accès à des sources connectées, indiquez-lui où chercher et ce
qu’il doit trouver. Vous n’avez pas besoin de décrire chaque recherche qu’il doit effectuer.

```text
Use the latest project plan in Drive and relevant decisions and updates from
the project's Slack channel to prepare a status update.

Les sources connectées nécessitent le plugin correspondant. Leur disponibilité peut dépendre de
votre offre et des paramètres de votre espace de travail.

### Utilisez des plugins

Les plugins fournissent à ChatGPT et Codex des instructions réutilisables et des connexions à des outils
tels que Google Drive, Gmail, Slack et GitHub. Les deux produits utilisent les plugins publics
du même répertoire universel. Demandez le résultat souhaité et laissez
l’interface active choisir parmi les outils à sa disposition. Dans ChatGPT, saisissez `@`
dans la zone de saisie pour choisir un plugin précis.

  
    <span slot="icon">
      
    </span>
    Recherchez, installez et utilisez des plugins dans ChatGPT et Codex.
  

### Personnalisez ChatGPT

Ajoutez les préférences qui doivent s’appliquer à toutes les discussions dans **Paramètres \> Personnalisation**
sous forme d’instructions personnalisées. Conservez les détails propres à la discussion en cours dans le
prompt.

  
    <span slot="icon">
      
    </span>
    Définissez une personnalité par défaut, des instructions personnalisées et d’autres préférences de l’application.
  

## Définissez des contraintes pour éviter les problèmes concrets

Les contraintes sont les quelques instructions dont ChatGPT a besoin pour éviter de vous imposer du travail supplémentaire
ou d’effectuer une action que vous n’aviez pas prévue. Ajoutez-en une lorsqu’une modification inappropriée
rendrait le résultat inutilisable, ou lorsque vous souhaitez vérifier quelque chose avant que cela
n’ait des conséquences pour d’autres personnes.

- Ne modifiez ni les dates approuvées ni les montants du budget.
- Utilisez uniquement les sources fournies. Signalez toute information manquante au lieu de faire des suppositions.
- Veillez à ce que les recommandations respectent le budget indiqué.
- Préparez le message sous forme de brouillon. Ne l’envoyez pas.

Ne retenez qu’une ou deux contraintes : celles qui comptent le plus. Vous n’avez pas besoin de contrôler
chaque étape suivie par ChatGPT.

## Rendez le résultat directement utilisable

Indiquez à ChatGPT comment vous comptez utiliser le résultat. Cela l’aide à adapter
la longueur, le niveau de détail et la structure.

- Faites-en un résumé d’une page qu’un membre de la direction pourra parcourir rapidement avant la réunion. Présentez
d’abord la décision et les prochaines étapes.
- Transformez ces notes en e-mail de suivi précisant les décisions, les responsables et les dates
d’échéance.
- Créez un tableau clair comparant les dépenses prévues aux dépenses réelles et mettez en évidence tout
écart supérieur à 10 %.

Pour les travaux importants, demandez à ChatGPT d’effectuer une vérification finale, par exemple de confirmer que chaque
action à mener est attribuée à un responsable et assortie d’une échéance, ou de signaler les informations qu’il n’a pas pu
vérifier. Examinez ensuite vous-même le résultat avant de l’utiliser ou de le partager.

## Améliorez le résultat avec des messages de suivi

Votre premier prompt n’a pas besoin d’être parfait. Examinez le résultat, puis demandez
la modification précise que vous souhaitez.

```text
Make the opening more direct, keep the evidence, and move the recommendation
above the background section.

Vous pouvez ajouter une source manquante, rectifier l’approche, demander une autre option ou
modifier le niveau de détail sans recommencer.

### Orientation et mise en file d’attente

Lorsque Codex travaille déjà, vous pouvez envoyer un autre message sans attendre la fin de
l’exécution en cours :

- **Orienter** ajoute le message à l’exécution en cours. Utilisez cette option pour réorienter le travail, ajouter
  un détail manquant ou fournir de nouvelles informations.
- **Mettre en file d’attente** enregistre le message pour l’exécution suivante. Utilisez cette option pour un message de suivi qui doit
  attendre la fin du travail en cours.

Dans l’application de bureau ChatGPT, choisissez le comportement par défaut dans
[**Paramètres \> Général \> Comportement des messages de suivi**](/fr-FR/codex/app/settings#general).
Les messages en file d’attente s’affichent au-dessus de la zone de saisie, où vous pouvez les modifier, les réorganiser, les envoyer ou
les supprimer. Le paramètre affiche également le raccourci permettant d’utiliser l’autre comportement
pour un seul message sans modifier votre choix par défaut.

Dans Codex CLI, appuyez sur <kbd>Enter</kbd> pendant que Codex travaille pour orienter le tour
en cours, ou sur <kbd>Tab</kbd> pour mettre le message en file d’attente pour le tour suivant. Consultez les
[raccourcis interactifs](/codex/developer-commands?surface=cli#cli-interactive-shortcuts)
pour en savoir plus.

## Rassemblez tous les éléments

Pour faire le point sur un projet à l’aide de sources connectées, un prompt complet pourrait se présenter
ainsi :

```text
Prepare a one-page project status update for Monday's leadership meeting. Use
the latest project plan in Drive and relevant decisions and updates from the
project's Slack channel.

Lead with the decisions leadership needs to make and the next steps. Summarize
progress, risks, owners, and due dates. Keep approved dates and budget figures
unchanged. Flag any conflicting or missing information, and don't send or
publish anything.

Before you finish, check that every next step has an owner and due date.

Ce prompt couvre les aspects **Objectif**, **Contexte**, **Résultat** et **Contraintes**, puis
demande une vérification finale sans détailler chaque étape.

## Utilisez la dictée vocale

Dans l’application de bureau ChatGPT, appuyez sur <kbd>Ctrl+Shift+D</kbd> lorsque la zone de saisie est
visible, puis commencez à parler. ChatGPT transcrit vos paroles dans la zone de saisie
afin que vous puissiez relire et modifier le texte avant d’envoyer le prompt.

  
    
  

<a id="threads"></a>
<a id="chats"></a>

## Exemples de prompts pour Discussion

Utilisez Discussion pour poser des questions, trouver des idées, rédiger des brouillons et prendre des décisions au quotidien. Commencez par
le résultat souhaité, puis n’ajoutez des détails que s’ils changent la réponse.

### Comprendre un sujet

```text
Explain how compound interest works for someone who has never invested.
Use one concrete example and define any financial terms you introduce.

### Rédiger et améliorer un texte

```text
Draft a friendly email declining this invitation because I will be traveling.
Keep it under 120 words and leave the door open for a future event.

### Comparer les options

```text
Compare these two phone plans for one person who travels internationally twice
a year. Show the important differences in a table, then recommend one and explain
the tradeoff.

### Élaborer un plan concret

```text
Plan five weekday dinners that take less than 30 minutes. Avoid peanuts, reuse
ingredients across meals, and finish with one consolidated shopping list.

<a id="prompting-for-work"></a>
<a id="prompting-in-work-mode"></a>

## Conception de prompts pour ChatGPT Work

Utilisez Discussion pour les questions rapides, les reformulations courtes, le brainstorming et les
brouillons simples. Utilisez ChatGPT Work pour les tâches qui mobilisent différentes sources ou différents outils, comprennent une
suite d’étapes, apportent des modifications ou produisent un livrable plus conséquent.

Dans ChatGPT Work, décrivez le résultat souhaité, fournissez les documents sources, indiquez
le public visé et expliquez comment vous vérifierez le travail. Demandez à ChatGPT de planifier,
de rassembler les informations nécessaires, de créer des fichiers et de les vérifier avant de terminer.

<a id="use-work-efficiently"></a>
<a id="use-work-mode-efficiently"></a>

### Utilisez ChatGPT Work efficacement

ChatGPT Work est utile pour les tâches longues ou récurrentes, ainsi que pour créer des fichiers finalisés que vous
pourrez réutiliser. Une tâche qui consomme davantage de crédits peut néanmoins être judicieuse si elle vous fait gagner
du temps, améliore la qualité ou vous aide à prendre une décision importante.

Commencez par demander un seul résultat que vous pourrez examiner :

- Incluez uniquement les sources pertinentes et limitez la période concernée lorsque cela est approprié.
- Définissez le public visé, le format de sortie et la longueur souhaitée.
- Distinguez le travail requis des améliorations ou finitions facultatives.
- Demandez un plan lorsque la méthode employée est importante. N’autorisez ChatGPT
à envoyer, publier ou modifier des informations sur lesquelles d’autres personnes s’appuient qu’après votre approbation.
- Réduisez le périmètre de la tâche ou arrêtez-la si elle commence à effectuer un travail dont vous n’avez plus besoin.

Examinez le premier résultat, affinez les instructions et réutilisez le workflow s’il
fonctionne.

### Transformer des documents sources en fichiers finalisés

```text
Use the attached quarterly reports to create a leadership brief and a six-slide
presentation.

The audience is the executive team. Lead with the three decisions they need to
make, distinguish reported facts from your analysis, cite each number to its
source file, and check that the brief and slides agree before you finish.

### Mener des recherches pour prendre une décision

```text
Research three customer-support platforms for a 50-person company. Compare
pricing, security, integrations, and migration effort using current sources.
Deliver a recommendation memo with links, assumptions, and the questions we
should answer before signing a contract.

### Coordonner un lancement

```text
Create a launch plan for the attached product brief. Include the timeline,
owners, dependencies, risks, announcement draft, customer FAQ, and a checklist
for launch day. Flag any missing decisions before producing the final files.

Pour les tâches récurrentes, commencez par affiner le prompt dans une discussion normale. Une fois le résultat
fiable, [planifiez une tâche dans cette discussion](/fr-FR/codex/automations#schedule-a-task-inside-a-chat).
Créez plutôt une tâche planifiée autonome si chaque exécution planifiée doit ouvrir
une nouvelle discussion.

<a id="use-editor-context"></a>

## Conception de prompts pour Codex

Utilisez Codex lorsque vous souhaitez que ChatGPT travaille avec du code, une base de code ou des outils de développement.
Un prompt Codex utile précise le comportement attendu, indique le code concerné ou les
étapes de reproduction, respecte les contraintes importantes et explique comment vérifier la
modification.

<a id="goal-mode"></a>

Pour une tâche en plusieurs étapes, saisissez `/plan` dans la zone de saisie de l’App si vous souhaitez que Codex
analyse la tâche et propose une approche avant toute modification. Lorsque le [mode Objectif](/fr-FR/codex/long-running-work)
est disponible, utilisez `/goal` après le plan pour définir un objectif persistant. Consultez les [commandes
slash de l’App](/codex/reference/slash-commands)
pour connaître la liste actuelle des commandes.

### Comment lire ces exemples

Chaque workflow comprend :

- **Quand l’utiliser** et quelle interface Codex convient le mieux (IDE, CLI ou Cloud).
- **Étapes** avec des exemples de prompts utilisateur.
- **Notes sur le contexte** : ce que Codex voit automatiquement et ce que vous devez joindre.
- **Vérification** : comment vérifier le résultat.

> **Remarque :** L’extension IDE inclut automatiquement vos fichiers ouverts dans le contexte. Dans la CLI, indiquez explicitement les chemins ou joignez des fichiers à l’aide de `/mention` et de la saisie semi-automatique des chemins avec `@`.

Codex exécute les commandes locales dans un [bac à sable](/fr-FR/codex/sandboxing)
qui limite l’accès aux fichiers et au réseau. Si une tâche doit franchir cette limite,
Codex applique votre politique d’approbation avant de poursuivre.

### Expliquer une base de code

Utilisez ce workflow pour vous familiariser avec une base de code, reprendre un service ou comprendre un protocole, un modèle de données ou un flux de requêtes.

#### Workflow de l’extension IDE (le plus rapide pour l’exploration locale)

1. Ouvrez les fichiers les plus pertinents.
2. Sélectionnez le code qui vous intéresse (facultatif, mais recommandé).
3. Demandez à Codex :

   ```text
   Explain how the request flows through the selected code.

   Include:
   - a short summary of the responsibilities of each module involved
   - what data is validated and where
   - one or two "gotchas" to watch for when changing this

Vérification :

- Demandez un diagramme ou une liste de contrôle que vous pourrez vérifier :

```text
Summarize the request flow as a numbered list of steps. Then list the files involved.

#### Workflow CLI (adapté si vous souhaitez un journal de session et des commandes shell)

1. Démarrez une session interactive :

   ```bash
   codex

2. Joignez les fichiers (facultatif), puis saisissez le prompt :

   ```text
   I need to understand the protocol used by this service. Read @foo.ts @schema.ts and explain the schema and request/response flow. Focus on required vs optional fields and backward compatibility rules.

Notes sur le contexte :

- Dans la zone de saisie, vous pouvez utiliser `@` pour insérer des chemins de fichiers de l’espace de travail, ou `/mention` pour joindre un fichier précis.

### Corriger un bug

Utilisez ce workflow lorsque vous pouvez reproduire localement le dysfonctionnement.

#### Workflow CLI (cycle court avec reproduction et vérification)

1. Démarrez Codex à la racine du dépôt :

   ```bash
   codex

2. Fournissez à Codex une procédure de reproduction ainsi que les fichiers que vous soupçonnez d’être en cause :

   ```text
   Bug: Clicking "Save" on the settings screen sometimes shows "Saved" but doesn't persist the change.

   Repro:
   1) Start the app: npm run dev
   2) Go to /settings
   3) Toggle "Enable alerts"
   4) Click Save
   5) Refresh the page: the toggle resets

   Constraints:
   - Do not change the API shape.
   - Keep the fix minimal and add a regression test if feasible.

   Start by reproducing the bug locally, then propose a patch and run checks.

Notes sur le contexte :

- Ce que vous fournissez : les étapes de reproduction et les contraintes (ces éléments comptent davantage qu’une description générale).
- Ce que fournit Codex : la sortie des commandes, les points d’appel découverts et les éventuelles traces de pile qu’il génère.

Vérification :

- Codex doit réexécuter les étapes de reproduction après la correction.
- Si vous disposez d’un pipeline de vérification standard, demandez-lui de l’exécuter :

```text
After the fix, run lint + the smallest relevant test suite. Report the commands and results.

#### Workflow de l’extension IDE

1. Ouvrez le fichier où vous pensez que se trouve le bug, ainsi que son appelant direct.
2. Demandez à Codex :

   ```text
   Find the bug causing "Saved" to show without persisting changes. After proposing the fix, tell me how to verify it in the UI.

### Écrire un test

Utilisez ce workflow lorsque vous souhaitez définir précisément le périmètre du test.

#### Workflow de l’extension IDE (à partir d’une sélection)

1. Ouvrez le fichier qui contient la fonction.
2. Sélectionnez les lignes qui définissent la fonction. Dans la palette de commandes, choisissez « Add to Codex Thread » pour ajouter ces lignes au contexte.
3. Demandez à Codex :

   ```text
   Write a unit test for this function. Follow conventions used in other tests.

Notes sur le contexte :

- Ce que fournit la commande « Add to Codex Thread » : les lignes sélectionnées (il s’agit du périmètre défini par les « numéros de ligne »), ainsi que les fichiers ouverts.

#### Workflow CLI (chemin et plage de lignes décrits dans le prompt)

1. Lancez Codex :

   ```bash
   codex

2. Saisissez un prompt avec le nom d’une fonction :

   ```text
   Add a test for the invert_list function in @transform.ts. Cover the happy path plus edge cases.

### Créer un prototype à partir d’une capture d’écran

Utilisez ce workflow pour transformer une maquette, une capture d’écran ou une référence d’interface utilisateur en prototype fonctionnel.

#### Workflow CLI (image + prompt)

1. Enregistrez votre capture d’écran en local (par exemple `./specs/ui.png`).
2. Lancez Codex :

   ```bash
   codex

3. Faites glisser le fichier image dans le terminal pour le joindre au prompt.

4. Poursuivez en précisant les contraintes et la structure :

   ```text
   Create a new dashboard based on this image.

   Constraints:
   - Use react, vite, and tailwind. Write the code in typescript.
   - Match spacing, typography, and layout as closely as possible.

   Outputs:
   - A new route/page that renders the UI
   - Any small components needed
   - README.md with instructions to run it locally

Notes sur le contexte :

- L’image précise les exigences visuelles, mais vous devez tout de même indiquer les contraintes d’implémentation (framework, routage, style des composants).
- Décrivez par écrit les comportements que l’image ne montre pas, comme les états au survol, les règles de validation ou les interactions au clavier.

Vérification :

- Demandez à Codex de lancer le serveur de développement, si cela est autorisé, et de vous indiquer précisément où vérifier le résultat :

```text
Start the dev server and tell me the local URL/route to view the prototype.

#### Workflow de l’extension IDE (image + fichiers existants)

1. Joignez l’image à la discussion Codex par glisser-déposer ou en la collant.
2. Envoyez un prompt à Codex :

   ```text
   Create a new settings page. Use the attached screenshot as the target UI.
   Follow design and visual patterns from other files in this project.

### Affiner l’interface utilisateur avec des mises à jour en direct

Utilisez ce workflow pour obtenir une boucle rapide « conception → ajustement → actualisation → ajustement » pendant que Codex modifie le code.

#### Workflow CLI (lancez Vite, puis procédez par prompts courts)

1. Lancez Codex :

   ```bash
   codex

2. Lancez le serveur de développement dans une autre fenêtre de terminal :

   ```bash
   npm run dev

3. Demandez à Codex d’apporter des modifications :

   ```text
   Propose 2-3 styling improvements for the landing page.

4. Choisissez une direction, puis poursuivez avec des prompts courts et précis :

   ```text
   Go with option 2.

   Change only the header:
   - make the typography more editorial
   - increase whitespace
   - ensure it still looks good on mobile

5. Répétez l’opération avec des demandes ciblées :

   ```text
   Next iteration: reduce visual noise.
   Keep the layout, but simplify colors and remove any redundant borders.

Vérification :

- Examinez les modifications dans le navigateur à mesure que Codex met à jour le code.
- Créez un commit avec les modifications qui vous conviennent et annulez les autres.
- Si vous annulez ou retouchez une modification, prévenez Codex afin qu’il n’écrase pas votre version lorsqu’il traitera le prompt suivant.

### Déléguer une refactorisation au cloud

Utilisez ce workflow pour concevoir une approche en vous appuyant sur le contexte local, puis déléguer la longue phase d’implémentation à une discussion dans le cloud qui pourra s’exécuter en parallèle.

#### Planification en local (IDE)

1. Assurez-vous d’avoir créé un commit avec votre travail en cours ou, au minimum, de l’avoir placé dans le stash, afin de pouvoir comparer proprement les modifications.
2. Demandez à Codex de produire un plan de refactorisation. Si vous avez accès à la skill `$plan`, invoquez-la explicitement :

   ```text
   $plan

   We need to refactor the auth subsystem to:
   - split responsibilities (token parsing vs session loading vs permissions)
   - reduce circular imports
   - improve testability

   Constraints:
   - No user-visible behavior changes
   - Keep public APIs stable
   - Include a step-by-step migration plan

3. Examinez le plan et discutez des modifications à apporter :

   ```text
   Revise the plan to:
   - specify exactly which files move in each milestone
   - include a rollback strategy

Notes sur le contexte :

- La planification donne de meilleurs résultats lorsque Codex peut analyser le code actuel en local (points d’entrée, limites entre les modules et indices sur le graphe des dépendances).

#### Délégation dans le cloud (IDE → Cloud)

1. Si ce n’est pas déjà fait, configurez un [environnement cloud Codex](/fr-FR/codex/environments/cloud-environment).
2. Cliquez sur l’icône en forme de nuage sous la zone de saisie, puis sélectionnez votre environnement cloud.
3. Lorsque vous saisissez le prompt suivant, Codex crée dans le cloud une nouvelle discussion qui reprend le contexte de la discussion existante, y compris le plan et les éventuelles modifications locales du code source.

   ```text
   Implement Milestone 1 from the plan.

4. Examinez le diff dans le cloud et apportez d’autres ajustements si nécessaire.

5. Créez une PR directement depuis le cloud ou récupérez les modifications en local pour les tester et finaliser le travail.

6. Procédez de même pour les autres jalons du plan.

Les tâches déléguées au cloud s’exécutent dans des environnements isolés. L’accès Internet est
désactivé pendant la phase de l’agent, sauf si vous l’activez pour l’environnement. Apprenez-en davantage
sur [l’accès Internet dans le cloud](/fr-FR/codex/cloud/internet-access).

### Effectuer une revue de code en local

Utilisez ce workflow pour obtenir un deuxième avis avant de créer un commit ou une PR.

#### Workflow CLI (revue de votre arbre de travail)

1. Lancez Codex :

   ```bash
   codex

2. Exécutez la commande de revue :

   ```text
   /review

3. Facultatif : fournissez des consignes personnalisées sur les points à examiner :

   ```text
   /review Focus on edge cases and security issues

Vérification :

- Appliquez les correctifs en fonction des retours de la revue, puis relancez `/review` pour confirmer que les problèmes sont résolus.

### Effectuer la revue d’une pull request GitHub

Utilisez ce workflow pour obtenir des commentaires de revue sans récupérer la branche en local.

Avant d’utiliser ce workflow, activez la fonctionnalité **Revue de code** de Codex sur votre dépôt. Consultez [Revue de code](/fr-FR/codex/third-party/github).

#### Workflow GitHub (piloté par des commentaires)

1. Ouvrez la pull request sur GitHub.
2. Ajoutez un commentaire qui mentionne Codex et indique explicitement les points à examiner :

   ```text
   @codex review

3. Facultatif : fournissez des instructions plus précises.

   ```text
   @codex review for security vulnerabilities and security concerns

### Mettre à jour la documentation

Utilisez ce workflow lorsque vous devez apporter une modification précise et claire à la documentation.

#### Workflow IDE ou CLI (modifications en local + validation en local)

1. Identifiez les fichiers de documentation à modifier et ouvrez-les (IDE), ou mentionnez-les avec `@` (IDE ou CLI).
2. Donnez à Codex un prompt précisant le périmètre et les exigences de validation :

   ```text
   Update the "advanced features" documentation to provide authentication troubleshooting guidance. Verify that all links are valid.

3. Une fois que Codex a rédigé les modifications, relisez la documentation et ajustez-la si nécessaire.

Vérification :

- Lisez la page générée.
