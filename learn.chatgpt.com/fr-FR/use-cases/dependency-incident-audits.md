<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/dependency-incident-audits -->

## Commencez par élaborer un plan d’audit sûr

Lorsqu’un incident lié à une dépendance ou à la chaîne d’approvisionnement évolue rapidement, le premier résultat utile n’est pas un correctif préparé à la hâte. C’est un plan d’audit clair : les changements survenus, les packages ou flux de travail susceptibles d’être affectés et les éléments qui prouveraient que votre dépôt est exposé.

Avant d’installer, de lancer un build, de tester ou d’exécuter quoi que ce soit, utilisez Codex pour transformer l’avis de sécurité en une liste de contrôle prudente à suivre en lecture seule.

## Effectuez la première passe en lecture seule

1. Fournissez à Codex l’avis de sécurité public, le rapport d’incident ou la liste des packages concernés.
2. Demandez-lui de distinguer les sources faisant autorité des commentaires plus généraux.
3. Demandez-lui de définir les éléments qui permettraient de confirmer ou d’exclure l’exposition.
4. Laissez-le inspecter les manifestes, les fichiers de verrouillage, les flux de travail CI, les scripts et les fichiers pertinents du dépôt.
5. Demandez des constats regroupés par niveau de preuve, gravité et prochaine étape recommandée.

En cas d’incident lié à un package, évitez d’exécuter des commandes d’installation, de build, de test, d’import ou de cycle de vie tant que vous ne savez pas précisément quels éléments sont concernés par l’avis de sécurité. Codex peut effectuer des recherches dans les fichiers de verrouillage et les flux de travail sans exécuter de code non fiable.

## Présentez séparément le niveau de preuve et la gravité

Un résultat d’audit utile doit indiquer à la fois la gravité potentielle d’un constat et la solidité des preuves :

  <p>
    <strong>Exposition confirmée :</strong> le fichier de verrouillage contient une version affectée
    du package dans une chaîne de dépendances utilisée en production.
  </p>
  <p>
    <strong>À vérifier :</strong> un job CI dispose d’autorisations de publication, mais
    le flux de travail ne semble pas installer directement le package concerné.
  </p>
  <p>
    <strong>Exposition exclue :</strong> le nom du package n’apparaît que dans la documentation et n’est pas
    présent dans les manifestes ni les fichiers de verrouillage.
  </p>
  <p>
    <strong>Étape suivante :</strong> examinez la mise à jour proposée de la dépendance et le plan de rotation des tokens
    avant toute action destructive.
  </p>

Une fois la passe en lecture seule terminée, vous pouvez demander à Codex de préparer une PR de remédiation, de mettre à jour les autorisations CI ou de rédiger une note de suivi sur l’incident. Séparez ces actions de l’audit initial.
