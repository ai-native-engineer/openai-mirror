<!-- source: https://learn.chatgpt.com/fr-FR/docs/enterprise/prisma-airs -->

Connectez Palo Alto Networks Prisma AIRS afin d’appliquer vos politiques de sécurité aux
prompts Codex avant qu’ils n’atteignent le modèle. Les administrateurs de l’espace
de travail ne configurent cette intégration qu’une seule fois par espace de travail.

Prisma AIRS peut appliquer les protections configurées dans votre profil de sécurité,
notamment la prévention des pertes de données, la détection des attaques par injection
de prompt et celle des URL malveillantes.

## Avant de commencer

Prérequis :

- Un espace de travail ChatGPT dans lequel l’accès à Prisma AIRS est activé. Contactez
l’équipe en charge de votre compte OpenAI pour demander l’accès.
- Des autorisations d’administrateur de l’espace de travail.
- Une clé API Prisma AIRS, un profil de sécurité configuré et le point de terminaison
du service correspondant à votre déploiement.

## Connectez Prisma AIRS

1. Ouvrez [Contrôles des données Codex](https://chatgpt.com/codex/cloud/settings/data) en tant
   qu’administrateur de l’espace de travail.
2. Dans **Garde-fous externes**, recherchez **Prisma AIRS**. Si cette section n’est pas
   disponible, demandez à l’équipe en charge de votre compte OpenAI d’activer l’accès pour votre espace de travail.
3. Saisissez votre **Clé API**, le nom ou l’ID du **Profil de sécurité**, ainsi que la valeur du champ **URL du point de
   terminaison**.
4. Choisissez les options **Mode d’application** et **En cas d’échec d’AIRS**.
5. Sélectionnez **Enregistrer la connexion**. Codex valide la connexion et chiffre votre
   clé API.
6. Sélectionnez **Tester la connexion** pour vérifier la configuration enregistrée.
7. Activez **Activer Prisma AIRS** pour commencer à analyser les prompts dans tout
   l’espace de travail.

L’enregistrement de la connexion n’active pas l’analyse. Vous devez également activer **Activer
Prisma AIRS**.

## Choisissez un point de terminaison

Utilisez le point de terminaison approuvé pour votre déploiement Prisma AIRS :

| Région        | Point de terminaison                                                 |
| ------------- | -------------------------------------------------------- |
| États-Unis | `https://service.api.aisecurity.paloaltonetworks.com`    |
| Allemagne       | `https://service-de.api.aisecurity.paloaltonetworks.com` |
| Inde         | `https://service-in.api.aisecurity.paloaltonetworks.com` |
| Singapour     | `https://service-sg.api.aisecurity.paloaltonetworks.com` |

Codex utilise par défaut le point de terminaison des États-Unis. Les exigences de résidence
des données de l’espace de travail peuvent limiter les points de terminaison utilisables.

## Choisissez comment traiter les prompts

Le paramètre **Mode d’application** détermine ce qui se passe lorsque Prisma AIRS signale un prompt :

- **Bloquer** : bloque le prompt avant qu’il n’atteigne le modèle. Il s’agit de l’option par défaut.
- **Alerte uniquement** : consigne la détection et laisse passer le prompt.

Le paramètre **En cas d’échec d’AIRS** détermine ce qui se passe si Prisma AIRS est indisponible ou
ne répond pas :

- **Autoriser les prompts** : poursuit le traitement même si l’analyse n’a pas abouti. Il s’agit de l’option par défaut.
- **Bloquer les prompts** : bloque le prompt jusqu’à ce que Prisma AIRS puisse l’analyser.

Choisissez **Bloquer les prompts** si votre politique de sécurité exige que chaque prompt concerné
fasse l’objet d’une décision issue de l’analyse.

## Découvrez ce qui est analysé

Codex envoie le texte des nouveaux prompts au point de terminaison Prisma AIRS configuré
pour inspection. Cela s’applique aux flux de travail Codex concernés, notamment l’App, le CLI,
l’Extension IDE et le Cloud, lorsque les utilisateurs se connectent à l’espace de travail ChatGPT
configuré. Les sessions authentifiées à l’aide d’une clé API de la plateforme ne sont pas concernées. Consultez
[Imposer une méthode de connexion ou un espace de travail](/fr-FR/codex/auth#enforce-a-login-method-or-workspace)
pour imposer la méthode de connexion et l’espace de travail prévus.

Prisma AIRS n’analyse pas les réponses de l’assistant, les appels d’outils, les résultats d’outils, les fichiers,
ni les images via cette intégration. Le profil de sécurité que vous avez configuré détermine
les menaces et les données sensibles détectées par Prisma AIRS.

Codex chiffre votre clé API et ne l’affiche plus jamais une fois que vous l’avez enregistrée. Consultez les politiques de Palo
Alto Networks relatives au traitement, à la conservation et à la résidence des données avant d’activer
l’inspection des prompts. Ces politiques s’appliquent aux prompts envoyés à Prisma AIRS.

## Gérez la connexion

Revenez à la page [Contrôles des données Codex](https://chatgpt.com/codex/cloud/settings/data)
pour gérer l’intégration :

- Sélectionnez **Tester la connexion** pour vérifier les éléments enregistrés : votre clé API, votre profil de sécurité,
  ainsi que votre point de terminaison.
- Saisissez une nouvelle clé, puis sélectionnez **Renouveler la clé API** pour remplacer la clé enregistrée
  sans modifier les autres paramètres.
- Désactivez **Activer Prisma AIRS** pour arrêter l’analyse tout en conservant la
  configuration enregistrée.
- Sélectionnez **Déconnecter**, puis confirmez votre choix pour arrêter l’analyse et supprimer la
  connexion et la clé API enregistrées.

Pour une configuration plus complète de l’espace de travail et la gestion des politiques, consultez le
[Guide de déploiement pour les administrateurs](/fr-FR/codex/enterprise/admin-setup) et la page
[Configuration gérée](/fr-FR/codex/enterprise/managed-configuration).
