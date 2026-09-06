<!-- source: https://learn.chatgpt.com/fr-FR/docs/environments/cloud-environment -->

Utilisez les environnements pour contrôler ce que Codex installe et exécute lors des discussions dans le cloud. Vous pouvez, par exemple, ajouter des dépendances, installer des outils de lint et de formatage, et définir des variables d’environnement.

Configurez les environnements dans les [paramètres de Codex](https://chatgpt.com/codex/settings/environments).

<a id="how-codex-cloud-tasks-run"></a>

## Fonctionnement des discussions Codex dans le cloud

Voici ce qui se passe lorsque vous envoyez un prompt :

1. Codex crée un conteneur et positionne votre dépôt sur la branche sélectionnée ou sur le commit correspondant au SHA sélectionné.
2. Codex exécute votre script de configuration et, lorsqu’un conteneur mis en cache est réactivé, un script de maintenance facultatif.
3. Codex applique vos paramètres d’accès Internet. Les scripts de configuration s’exécutent avec un accès Internet. L’accès Internet de l’agent est désactivé par défaut, mais vous pouvez activer un accès limité ou sans restriction si nécessaire. Consultez la page [Accès Internet de l’agent](/fr-FR/codex/cloud/internet-access).
4. L’agent exécute en boucle des commandes de terminal. Il modifie le code, effectue des vérifications et tente de valider son travail. Si votre dépôt contient `AGENTS.md`, l’agent s’en sert pour trouver les commandes de lint et de test propres au projet.
5. Lorsque l’agent a terminé, il affiche sa réponse et un diff des fichiers qu’il a modifiés. Vous pouvez ouvrir une PR ou poser des questions complémentaires.

## Image universelle par défaut

L’agent Codex s’exécute dans une image de conteneur par défaut appelée `universal`, où sont préinstallés des langages, paquets et outils courants.

Dans les paramètres de l’environnement, sélectionnez **Définir les versions des paquets** pour fixer les versions de Python, Node.js et d’autres environnements d’exécution.

  Pour obtenir le détail des éléments installés, consultez
[openai/codex-universal](https://github.com/openai/codex-universal), qui fournit un
  Dockerfile de référence et une image que vous pouvez récupérer et tester localement.

Même si `codex-universal` inclut des langages préinstallés pour plus de rapidité et de simplicité, vous pouvez également installer des paquets supplémentaires dans le conteneur à l’aide de [scripts de configuration](#manual-setup).

## Variables d’environnement et secrets

Les **variables d’environnement** sont définies pendant toute la durée de la discussion, y compris pendant l’exécution des scripts de configuration et la phase de l’agent.

Les **secrets** sont semblables aux variables d’environnement, à ces différences près :

- Ils sont stockés avec une couche de chiffrement supplémentaire et ne sont déchiffrés que pour l’exécution de la tâche.
- Ils ne sont disponibles que pour les scripts de configuration. Pour des raisons de sécurité, les secrets sont retirés avant le début de la phase de l’agent.

## Configuration automatique

Pour les projets qui utilisent des gestionnaires de paquets courants (`npm`, `yarn`, `pnpm`, `pip`, `pipenv` et `poetry`), Codex peut installer automatiquement les dépendances et les outils.

## Configuration manuelle

Si votre configuration de développement est plus complexe, vous pouvez également fournir un script de configuration personnalisé. Par exemple :

```bash
# Install type checker
pip install pyright

# Install dependencies
poetry install --with test
pnpm install

  Les scripts de configuration s’exécutent dans une session Bash distincte de celle de l’agent. Les effets de commandes comme
`export` ne persistent donc pas pendant la phase de l’agent. Pour rendre persistantes les
  variables d’environnement, ajoutez-les dans `~/.bashrc` ou configurez-les dans les paramètres de l’environnement.

## Mise en cache des conteneurs

Codex met en cache l’état du conteneur pendant 12 heures au maximum afin d’accélérer les nouvelles discussions et les questions complémentaires.

Lorsqu’un environnement est mis en cache :

- Codex clone le dépôt et se place sur la branche par défaut.
- Codex exécute le script de configuration et met en cache l’état du conteneur ainsi obtenu.

Lorsqu’un conteneur mis en cache est réactivé :

- Codex se place sur la branche spécifiée pour la discussion.
- Codex exécute le script de maintenance (facultatif). Cette opération est utile si le script de configuration a été exécuté sur un commit plus ancien et que les dépendances doivent être mises à jour.

Codex invalide automatiquement le cache si vous modifiez le script de configuration, le script de maintenance, les variables d’environnement ou les secrets. Si votre dépôt subit des modifications qui rendent l’état mis en cache incompatible, sélectionnez **Réinitialiser le cache** sur la page de l’environnement.

  Pour les utilisateurs Business et Entreprise, les caches sont partagés entre tous les utilisateurs qui ont
accès à l’environnement. L’invalidation du cache affectera tous les utilisateurs de
l’environnement au sein de votre espace de travail.

## Accès Internet et proxy réseau

L’accès Internet est disponible pendant l’exécution du script de configuration afin d’installer les dépendances. Pendant la phase de l’agent, l’accès Internet est désactivé par défaut, mais vous pouvez configurer un accès limité ou sans restriction. Consultez la page [Accès Internet de l’agent](/fr-FR/codex/cloud/internet-access).

Les environnements s’exécutent derrière un proxy réseau HTTP/HTTPS à des fins de sécurité et de prévention des abus. Tout le trafic Internet sortant passe par ce proxy.
