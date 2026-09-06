<!-- source: https://learn.chatgpt.com/fr-FR/docs/security/faq -->

Cette FAQ porte sur Codex Security dans le cloud. Pour les analyses locales et les workflows exécutés dans
une tâche Codex, consultez le [démarrage rapide du plugin Codex Security](/fr-FR/codex/security/plugin).

{/* vale Microsoft.Auto = NO */}
{/* vale Vale.Spelling = NO */}

## Bien démarrer

### Qu’est-ce que Codex Security ?

La sécurité logicielle reste l’un des enjeux d’ingénierie les plus difficiles et les plus importants. Codex Security est une boîte à outils d’analyse de sécurité fondée sur un LLM, qui inspecte le code source et renvoie une liste structurée et hiérarchisée des vulnérabilités détectées, avec des propositions de correctifs. Elle aide les équipes de développement et de sécurité à détecter et à corriger les problèmes de sécurité à grande échelle.

### Pourquoi est-ce important ?

Les logiciels sont au cœur de l’industrie et de la société modernes, et leurs vulnérabilités créent un risque systémique. Codex Security facilite un workflow qui privilégie la défense en identifiant en continu les problèmes potentiels, en les validant lorsque cela est possible et en proposant des correctifs. Les équipes peuvent ainsi renforcer la sécurité sans ralentir le développement.

### À quel problème métier Codex Security répond-il ?

Codex Security accélère le passage d’un problème suspecté à une vulnérabilité confirmée et reproductible, étayée par des preuves et accompagnée d’une proposition de correctif. Cela allège la charge de triage et réduit les faux positifs par rapport à l’utilisation de scanners traditionnels seuls.

### Comment fonctionne Codex Security ?

Codex Security exécute l’analyse dans un conteneur éphémère et isolé, et clone temporairement le dépôt cible. Il analyse le code et renvoie des résultats structurés comprenant une description, le fichier et l’emplacement concernés, le niveau de criticité, la cause profonde et une mesure corrective suggérée.

Pour les résultats qui comprennent des étapes de vérification, le système exécute les commandes ou les tests proposés dans le même bac à sable. Il consigne leur réussite ou leur échec, les codes de sortie, stdout, stderr, les résultats des tests ainsi que les éventuels diffs ou artefacts générés, puis joint ces données comme éléments de preuve pour la revue.

### Remplace-t-il le SAST ?

Non. Codex Security complète le SAST. Il ajoute un raisonnement sémantique fondé sur un LLM et une validation automatisée, tandis que les outils SAST existants continuent d’offrir une vaste couverture déterministe.

## Fonctionnalités

### Quel est le processus d’analyse ?

Codex Security suit un processus en plusieurs étapes :

1. **Analyse** crée un modèle de menaces pour le dépôt.
2. **Analyse des commits** examine les commits fusionnés et l’historique du dépôt afin d’identifier les problèmes potentiels.
3. **Validation** tente de reproduire les vulnérabilités potentielles dans un bac à sable afin de réduire les faux positifs.
4. **Création de correctifs** s’intègre à Codex pour proposer des correctifs que les personnes chargées de la revue peuvent examiner avant d’ouvrir une PR.

Codex Security accompagne les ingénieurs dans GitHub et Codex, ainsi que dans les workflows de revue courants.

### Quels langages sont pris en charge ?

Codex Security n’est lié à aucun langage particulier. En pratique, ses performances dépendent des capacités de raisonnement du modèle pour le langage et le framework utilisés dans le dépôt.

### Quels résultats obtenez-vous une fois l’analyse terminée ?

Vous obtenez des résultats classés par priorité, avec leur niveau de criticité, leur statut de validation et un correctif proposé lorsqu’il est disponible. Ils peuvent également inclure les données de sortie d’un plantage, des preuves de reproduction, le contexte du chemin d’appel et les annotations associées.

### Comment le code client est-il isolé ?

Chaque tâche d’analyse ou de validation s’exécute dans un conteneur Codex éphémère doté d’outils limités à la session. Les artefacts sont extraits pour être examinés, puis le conteneur est détruit une fois la tâche terminée.

### Codex Security applique-t-il automatiquement les correctifs ?

Non. Le correctif proposé est une mesure corrective recommandée. Les utilisateurs peuvent l’examiner et le publier sur GitHub sous forme de PR depuis l’interface des résultats, mais Codex Security n’applique pas automatiquement les modifications au dépôt.

### Le projet doit-il être compilé pour être analysé ?

Non. Codex Security peut produire des résultats à partir du contexte du dépôt et des commits, sans étape de compilation. Lors de la validation automatique, il peut tenter de compiler le projet dans le conteneur si cela facilite la reproduction du problème. Pour en savoir plus sur la configuration de l’environnement, consultez la page [Environnements cloud Codex](/fr-FR/codex/environments/cloud-environment).

### Comment Codex Security réduit-il les faux positifs et évite-t-il de générer des correctifs inopérants ?

Codex Security procède en deux étapes. Le modèle classe d’abord les problèmes potentiels par priorité. La validation automatique tente ensuite de reproduire chacun d’eux dans un conteneur vierge. Les problèmes reproduits avec succès sont marqués comme validés, ce qui permet de réduire les faux positifs avant la revue humaine.

### Combien de temps dure l’analyse initiale, et que se passe-t-il ensuite ?

La durée de l’analyse initiale dépend de la taille du dépôt, du temps de compilation et du nombre de résultats qui passent à l’étape de validation. Pour certains dépôts, l’analyse peut prendre plusieurs heures. Pour les dépôts plus volumineux, elle peut prendre plusieurs jours. Les analyses suivantes sont généralement plus rapides, car elles se concentrent sur les nouveaux commits et les modifications incrémentales.

### Qu’est-ce qu’un modèle de menaces ?

Un modèle de menaces constitue le contexte de sécurité d’un dépôt lors de son analyse. Il associe une vue d’ensemble concise du projet à des informations sur la surface d’attaque, telles que les points d’entrée, les frontières de confiance, les hypothèses en matière d’authentification et les composants à risque. Pour en savoir plus, consultez [Améliorer le modèle de menaces](/fr-FR/codex/security/threat-model).

### Comment un modèle de menaces est-il généré ?

Codex Security demande au modèle de résumer l’architecture du dépôt et ses points d’entrée pertinents pour la sécurité, de déterminer le type de dépôt, d’exécuter des extracteurs spécialisés et de fusionner les résultats dans une vue d’ensemble du projet ou un artefact de modèle de menaces utilisé tout au long de l’analyse.

### Remplace-t-il la revue manuelle de sécurité ?

Non. Codex Security accélère la revue et aide à classer les résultats par priorité, mais ne remplace ni la validation au niveau du code, ni les vérifications de l’exploitabilité, ni l’évaluation des menaces par un humain.

### Puis-je modifier le modèle de menaces ?

Oui. Codex Security crée le modèle de menaces initial, que vous pouvez mettre à jour au fil de l’évolution de l’architecture, des risques et du contexte métier. Pour connaître la procédure de modification, consultez [Améliorer le modèle de menaces](/fr-FR/codex/security/threat-model).

### Dois-je configurer une analyse avant d’utiliser la modélisation des menaces ?

Oui. Les recommandations relatives au modèle de menaces dépendent de ce que vous analysez et de la manière dont vous le faites ; vous devez donc commencer par configurer le dépôt. Consultez [Configuration de Codex Security](/fr-FR/codex/security/setup).

### Que contient le correctif proposé ?

Lorsqu’une mesure corrective peut être générée pour un résultat, le correctif proposé contient un diff minimal et applicable, avec le nom du fichier et le contexte des lignes concernées.

### Le correctif modifie-t-il directement la branche de ma PR ?

Non. Le workflow génère un diff, un fichier de patch ou une suggestion de modification, que les mainteneurs et les personnes chargées de la revue peuvent examiner avant de l’appliquer.

## Validation

### Qu’est-ce que la validation automatique ?

La validation automatique est la phase qui tente de reproduire un problème suspecté dans un conteneur isolé. Elle consigne la réussite ou l’échec de la reproduction et enregistre les journaux, les commandes et les artefacts associés comme éléments de preuve.

### Que se passe-t-il en cas d’échec de la validation ?

Le résultat reste non validé. Les journaux et les rapports indiquent malgré tout ce qui a été tenté, afin que les ingénieurs puissent réessayer, approfondir l’analyse ou ajuster les étapes de reproduction.

{/* vale Microsoft.Auto = YES */}
{/* vale Vale.Spelling = YES */}
