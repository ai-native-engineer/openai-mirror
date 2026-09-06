<!-- source: https://learn.chatgpt.com/fr-FR/docs/security/plugin/scans -->

Commencez par une analyse Codex Security standard pour un examen initial ou une évaluation périodique
d’un dépôt ou d’un composant. Elle exécute une fois l’intégralité du workflow d’analyse.

Pour une évaluation plus approfondie, examinez les résultats, puis lancez une [analyse
approfondie](/fr-FR/codex/security/plugin/deep-scans). Les analyses approfondies prennent plus de temps et effectuent des recherches
plus poussées.

## Choisissez le périmètre de l’analyse

Dans l’application de bureau, ouvrez **Sécurité**, sélectionnez **Analyses**, puis **+ Analyse**.
Choisissez un dépôt existant ou un autre dossier, puis sélectionnez **Code source**.

Analysez l’intégralité du dépôt lorsque vous avez besoin d’une large couverture et que le dépôt
constitue un périmètre d’examen raisonnable. Dans un monorepo, choisissez un dossier lorsqu’un service,
un package ou un composant a un responsable et une frontière de sécurité clairement définis.

Vous pouvez également lancer une analyse depuis une discussion Codex :

```text
Use $codex-security:security-scan to scan this repository for security vulnerabilities.

Pour cibler cette discussion sur un dossier précis, indiquez le composant :

```text
Use $codex-security:security-scan to scan this repository for security vulnerabilities, focusing on the services/billing component.

  Pour un monorepo volumineux, commencez par un périmètre pertinent correspondant à un produit ou à un service.

## Configurez l’analyse

Pour obtenir la meilleure qualité d’analyse, utilisez <code>{RECOMMENDED_MODEL_REFERENCES.latestSecurityScanModel.slug}</code>
avec le niveau de raisonnement `xhigh`.

1. Sélectionnez **Code source** et laissez **Analyse approfondie** désactivée.
2. Confirmez le dépôt sélectionné, la branche actuelle et la dernière révision.
3. Définissez **Périmètre de l’analyse** sur l’ensemble du dépôt ou choisissez un dossier.
4. Choisissez un modèle et un niveau de raisonnement.
5. Ouvrez **Contexte supplémentaire** uniquement si cela influe sur l’examen. Un contexte utile
   indique les entrées contrôlées par un attaquant, les frontières de confiance, les actions sensibles ou
   une zone précise à traiter en priorité.
6. Sélectionnez **Lancer l’analyse**.

Ajoutez `SECURITY.md` à la racine du dépôt pour fournir des consignes de sécurité permanentes.
Décrivez le modèle de menace, les invariants de sécurité, les critères déterminant les résultats à signaler,
les exclusions et les éléments permettant d’évaluer la gravité. Ajoutez des fichiers `SECURITY.md` imbriqués pour fournir des consignes
propres à chaque répertoire. En cas de conflit entre les règles, le fichier situé au plus près du
code prévaut. Codex Security considère ces fichiers comme un contexte de règles,
et non comme des instructions exécutables.

Utilisez `AGENTS.md` pour les commandes de compilation et de validation prises en charge, ainsi que pour les autres
instructions propres au dépôt.

## Attendez la fin de toutes les phases

Une analyse exécute les phases suivantes dans cet ordre :

1. La **modélisation des menaces** recense les ressources, les points d’entrée, les frontières de confiance et les
   invariants de sécurité.
2. La **recherche de problèmes** examine le code concerné afin d’identifier les
   contrôles susceptibles d’être défaillants et les chemins de la source au puits.
3. La **validation** teste chaque résultat potentiel ou le vérifie par d’autres moyens, puis consigne les éléments probants
   ou les lacunes de preuve.
4. L’**analyse de l’impact et des chemins** évalue les chemins d’exploitation réalistes de chaque résultat potentiel,
   son impact et sa gravité.
5. La **génération de rapports** consigne les résultats validés, la couverture et les métadonnées de l’analyse.
   Des rapports détaillés pour chaque résultat sont disponibles sur demande.
6. Le **durcissement structurel**, lorsqu’il est demandé, analyse l’ensemble des résultats et
   génère des recommandations de conception.
7. La **finalisation** valide le contrat structuré de l’analyse et génère
`report.md`, avec des liens vers les éventuels rapports détaillés ou recommandations de durcissement.

L’atelier affiche la phase d’analyse en cours et la progression éventuellement signalée par le plugin.
Sélectionnez **Afficher l’activité** pour examiner la tâche Codex. Attendez le résultat
complet plutôt que d’évaluer prématurément les résultats potentiels ou d’interrompre l’analyse parce qu’une phase prend
plus de temps qu’une autre.

## Examinez l’analyse terminée

Examinez le résultat dans l’ordre suivant :

1. Confirmez la cible, la révision et le périmètre de l’analyse.
2. Consultez les surfaces examinées ainsi que toutes les zones explicitement reportées ou à traiter ultérieurement.
3. Pour chaque résultat, examinez le contrôle ou le puits à l’origine du problème, l’entrée contrôlée par
un attaquant, la méthode de validation, les incertitudes restantes, l’accessibilité réelle,
la justification du niveau de gravité et la correction proposée.
4. Écartez les résultats dont les preuves n’étayent pas le chemin ou l’impact indiqué.
5. Sélectionnez un résultat accepté avant de commencer un correctif.

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    Examinez le niveau de gravité du résultat, son état de validation, sa cause racine et son chemin
d’attaque.
  </figcaption>
</figure>

## Évaluez une première analyse

Avant l’analyse, choisissez deux à quatre critères d’évaluation, tels que la détection
indépendante, la qualité des preuves, les faux positifs ou la qualité des corrections. Si vous
effectuez un test par rapport à un résultat connu, consignez si vous l’avez communiqué à Codex ou
si vous ne l’avez pas fourni pour l’analyse.

Consignez la révision du dépôt, la version du plugin, le modèle et le niveau de raisonnement.
Utilisez ce point de référence pour comparer les analyses ultérieures après toute modification du code, des contrôles de sécurité ou
des paramètres d’analyse.

## Choisissez une fréquence d’analyse

Définissez la fréquence d’analyse selon le niveau de risque du dépôt et la capacité de votre équipe
à traiter les résultats. Lancez une analyse aux étapes suivantes :

- **Point de référence :** Lancez une analyse standard lorsque vous intégrez un dépôt, prenez
  en charge un composant ou avez besoin d’un point de départ pour un nouveau modèle de menace.
- **Modifications du code :** [Examinez les modifications
  du code](/fr-FR/codex/security/plugin/code-changes) lorsqu’une pull request ou un commit
  modifie du code sensible sur le plan de la sécurité ou une intégration externe.
- **Examen périodique :** Définissez une fréquence d’examen récurrente selon l’exposition de votre système
  et la fréquence de modification du code. Adaptez-la à la capacité de votre équipe à
  traiter les résultats.
- **Après un correctif :** [Corrigez et vérifiez le
  résultat](/fr-FR/codex/security/plugin/fix-findings). Vérifiez que le problème ne
  se reproduit plus et conservez l’analyse d’origine à des fins de comparaison.

Ces déclencheurs d’analyse ne créent pas de planification automatisée.

## Rouvrez une analyse précédente

Ouvrez **Sécurité**, puis sélectionnez dans **Analyses** une analyse enregistrée afin d’en examiner les
résultats, la couverture et les artefacts de rapport disponibles. Pour évaluer le code le plus récent,
lancez une nouvelle analyse du même dépôt. La nouvelle analyse ne remplace pas
l’analyse précédente ni ses artefacts.

## Exploitez les résultats

Utilisez l’atelier de sécurité pour examiner les résultats, la couverture et les zones à traiter
sans consulter les données JSON brutes. Lorsqu’il est disponible, ouvrez `report.md`, qui constitue un point d’entrée lisible
vers le répertoire complet de l’analyse. Conservez le répertoire dans son intégralité lorsque
vous le partagez ou l’archivez : le rapport contient des liens vers les rapports détaillés dans `findings/`
et vers les recommandations de durcissement structurel dans `hardening/` lorsque ces artefacts facultatifs
sont disponibles.

En arrière-plan de l’espace de travail, chaque analyse conserve `scan-manifest.json`, `findings.json`,
et `coverage.json` pour l’automatisation et les intégrations. Vous n’avez normalement pas besoin
d’ouvrir vous-même ces fichiers.

Pour obtenir des artefacts portables ou suivre les problèmes dans un outil externe, consultez [Exporter ou suivre les
résultats](/fr-FR/codex/security/plugin/export-findings).

## Étape suivante

Après avoir accepté un résultat, utilisez [Corriger et vérifier un
résultat](/fr-FR/codex/security/plugin/fix-findings) pour générer puis examiner un
seul patch au périmètre limité. Ne demandez pas à Codex de corriger tous les résultats d’une analyse dans une même discussion.
