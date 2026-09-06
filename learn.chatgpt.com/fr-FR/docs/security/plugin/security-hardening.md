<!-- source: https://learn.chatgpt.com/fr-FR/docs/security/plugin/security-hardening -->

Utilisez `$codex-security:propose-security-hardening` pour transformer un ensemble d’éléments probants relatifs à la
sécurité en options de renforcement structurel ou architectural. Le
workflow peut analyser un scan Codex Security terminé ou s’appuyer sur les
constats, les rapports de divulgation, les analyses d’incidents, les documents d’évaluation et
le code source qui lui sont fournis.

Le résultat est un dossier de propositions de conception, et non un correctif ; il ne démontre pas qu’une
vulnérabilité est corrigée. Codex ne modifie le dépôt qu’une fois que vous avez sélectionné une option et que vous
lui avez explicitement demandé d’appliquer cette modification.

## Préparez les éléments probants

Fournissez au workflow les éléments suivants :

- Un répertoire de scan ou un ensemble clairement défini de constats et de rapports.
- L’arborescence du code source ciblée et, le cas échéant, la révision ou l’instantané pertinent.
- Des PoC, des traces, des éléments probants liés aux incidents ou des documents d’évaluation à l’appui des
constats.
- Des contraintes relatives aux performances, à la mémoire, à la compatibilité, à la fiabilité, à l’exploitation,
aux délais de livraison ou au périmètre des modifications.

Le workflow utilise les éléments probants pour repérer les violations répétées d’invariants, les contrôles
dispersés, les points de passage où se concentrent les privilèges, les frontières d’isolation fragiles et les schémas récurrents
de remédiation. Il peut également conclure que des corrections locales constituent une réponse plus
proportionnée qu’une modification architecturale.

## Exécutez le workflow

Envoyez un prompt comme celui-ci :

```text
Use $codex-security:propose-security-hardening to analyze [scan directory or finding paths] against [source tree and revision]. Develop evidence-backed structural hardening options with engineering tradeoffs, before-and-after diagrams, a migration plan, and an implementation handoff. Do not modify the repository.

## Examinez le dossier de propositions

Pour être utile, le dossier de propositions doit remplir les critères suivants :

- Relier chaque modification proposée à des constats concrets et à des éléments probants tirés du code source et du modèle de
menaces.
- Décrire la conception actuelle et les invariants de sécurité que la nouvelle conception doit
préserver.
- Comparer différentes options en tenant compte du risque résiduel, des performances,
de la fiabilité, de l’exploitation, de la compatibilité et du coût de migration.
- Ne recommander une option que lorsque les éléments probants le justifient, en indiquant explicitement
les hypothèses et les questions en suspens.
- Inclure des consignes pour le déploiement, la validation, le retour arrière et l’implémentation.
- Distinguer les faits observés, les inférences et les propriétés de conception proposées.

Examinez les éléments probants et les compromis avant de choisir une option. Un diagramme
d’architecture ou une recommandation de conception ne remplace ni la validation des
constats initiaux ni celle du correctif mis en œuvre.

## Utilisez les recommandations de renforcement issues d’un scan

Vous pouvez demander un dossier de propositions de renforcement pour un scan standard, approfondi ou de modifications présentant
des constats à signaler. Codex enregistre le dossier dans `hardening/hardening.md`,
l’analyse structurée dans `hardening/hardening.json` et les propositions
ou diagrammes complémentaires dans `hardening/`. Le scan fournit un lien vers le dossier depuis `report.md`.

Conservez l’intégralité du répertoire de scan sans en dissocier les éléments afin que ces liens restent fonctionnels. Pour examiner
les rapports individuels qui servent de base au dossier, consultez [Rédiger des rapports de
vulnérabilité](/fr-FR/codex/security/plugin/vulnerability-reports).
