<!-- source: https://learn.chatgpt.com/fr-FR/docs/amazon-bedrock -->

Configurez les interfaces locales de ChatGPT Work et de Codex pour utiliser les modèles OpenAI disponibles
via Amazon Bedrock. Dans cette configuration, le client local envoie à
Bedrock les requêtes adressées au modèle en s’appuyant sur l’authentification et les contrôles d’accès gérés par AWS.

## Fonctionnement

Lorsque vous configurez une interface locale de ChatGPT Work ou de Codex avec Amazon Bedrock comme
fournisseur de modèles, la Responses API hébergée par OpenAI ne se trouve pas sur le chemin des requêtes.
Le client local envoie les requêtes adressées au modèle à Amazon Bedrock, et Bedrock fournit une
implémentation de la Responses API compatible avec OpenAI pour les modèles OpenAI pris en charge.

  L’authentification s’appuie nativement sur AWS. Les utilisateurs s’authentifient avec une clé d’API Bedrock ou des
  identifiants IAM AWS. Ils n’utilisent ni la connexion à ChatGPT ni `OPENAI_API_KEY` pour ce
  fournisseur.

## Avant de commencer

Vérifiez que vous disposez des éléments suivants :

- Un accès aux modèles OpenAI pris en charge dans Amazon Bedrock.
- Une région AWS où le modèle sélectionné est disponible.
- Une authentification pour le chemin Amazon Bedrock Mantle configurée pour le compte
AWS.

## Configuration du fournisseur

Ajoutez le fournisseur de modèles `amazon-bedrock` pour le chemin Amazon Bedrock Mantle dans
`~/.codex/config.toml`. L’application de bureau ChatGPT, Codex CLI, l’extension IDE et le
SDK lisent les mêmes couches de configuration locale. La spécification d’un modèle est facultative.
Sélectionnez explicitement un modèle pris en charge si nécessaire.

```toml
model_provider = "amazon-bedrock"

  Ce guide couvre le chemin Amazon Bedrock Mantle dans les régions AWS
commerciales prises en charge. Les interfaces locales de ChatGPT Work et de Codex ne prennent pas en charge les points de terminaison Bedrock Mantle
dans les régions AWS GovCloud.

## Options d’authentification

Les interfaces locales de ChatGPT Work et de Codex prennent en charge deux méthodes d’authentification Bedrock.
Elles les vérifient dans l’ordre suivant :

1. Clé d’API Bedrock.
2. Chaîne d’identifiants AWS SDK.

### Option 1 : clé d’API Bedrock

Définissez la clé d’API Bedrock dans l’environnement utilisé par le client local. Vous devez
indiquer une région lorsque vous utilisez l’authentification par clé d’API.

```shell

### Option 2 : identifiants AWS SDK

Utilisez cette méthode lorsque votre organisation gère l’accès à Bedrock par l’intermédiaire de la chaîne
d’identifiants AWS SDK. Le client local peut utiliser les sources standard
d’identifiants AWS SDK suivantes :

#### Fichiers de configuration AWS partagés

Configurez les fichiers AWS partagés `config` et `credentials` :

```shell
aws configure

#### Variables d’environnement

Définissez les variables d’environnement standard d’AWS SDK pour les identifiants :

```shell

#### Identifiants AWS Management Console

Connectez-vous avec les identifiants AWS Management Console :

```shell
aws login

#### AWS SSO ou profil nommé

Connectez-vous avec AWS SSO et sélectionnez le profil nommé :

```shell
aws sso login --profile codex-bedrock

#### Identité fédérée

Pour la fédération SSO d’entreprise ou OIDC, configurez une identité fédérée avec
`credential_process` en dehors du client local et confiez à AWS SDK la résolution des
identifiants. Gérez la connexion dans le navigateur, l’échange de tokens, la mise en cache et le renouvellement dans
l’utilitaire `credential_process` de votre profil AWS.

## Application de bureau et extension IDE

Les applications de bureau et les extensions IDE peuvent ne pas hériter des variables d’environnement du
shell. Placez les valeurs requises dans `~/.codex/.env`, puis redémarrez l’application ou
l’extension.

```shell

## Vérification de la configuration

- Dans Codex CLI, ouvrez `/status` et vérifiez que Codex utilise le fournisseur de modèles
`amazon-bedrock`.
- Dans l’application de bureau ChatGPT, sélectionnez Work ou Codex et lancez une nouvelle tâche après
avoir redémarré l’application.
- Dans l’extension IDE, lancez une nouvelle session après avoir redémarré l’extension.
- Vérifiez que le modèle sélectionné est disponible dans la région AWS configurée et que
l’identité AWS est autorisée à y accéder.

## Modèles pris en charge

Utilisez les identifiants exacts des modèles :

```text
openai.gpt-5.6-sol
openai.gpt-5.6-terra
openai.gpt-5.6-luna
openai.gpt-5.5
openai.gpt-5.4

La disponibilité des modèles varie selon la région AWS. Avant de sélectionner un modèle, consultez [les modèles
pris en charge par
région AWS](https://docs.aws.amazon.com/bedrock/latest/userguide/models-region-compatibility.html).

## Disponibilité des fonctionnalités

Cette configuration prend en charge les workflows locaux de ChatGPT Work et de Codex. La version hébergée de
ChatGPT Work sur le Web, Codex Cloud et les fonctionnalités qui dépendent de services cloud hébergés par OpenAI,
d’outils hébergés ou de la découverte gérée dans le cloud ne sont actuellement pas
disponibles.

  Le mode Rapide n’est pas disponible avec Amazon Bedrock. Le mode Rapide utilise le traitement
prioritaire, et l’offre initiale d’Amazon Bedrock ne prend en charge que l’inférence
à la demande.

  

  <div
    id="codex-plan-region-limits"
    className="not-prose mt-3 text-sm text-secondary"
  >
    <sup>\*</sup> Cette fonctionnalité est actuellement limitée à certaines régions. Consultez
    sa documentation pour en savoir plus sur les restrictions géographiques.
  </div>
  <div
    id="codex-plan-plugin-limits"
    className="not-prose mt-1 text-sm text-secondary"
  >
    <sup>†</sup> Les lots de plugins locaux et les plugins sélectionnés par OpenAI qui ne
    nécessitent pas d’authentification ChatGPT, notamment Codex Security, sont disponibles.
    Les plugins qui nécessitent une authentification ChatGPT, des connecteurs ou un partage
    hébergé dans le cloud ne sont pas disponibles.
  </div>

## Dépannage

Si la configuration échoue, vérifiez les points suivants :

- L’identifiant du modèle correspond exactement à celui d’un modèle pris en charge.
- Vous avez indiqué une région AWS dans laquelle le modèle est disponible.
- La clé API Bedrock ou les identifiants AWS sont valides et n’ont pas expiré.
- L’identité AWS est autorisée à accéder au modèle Bedrock sélectionné.
- `AWS_BEARER_TOKEN_BEDROCK` ne contient ni clé expirée ni clé autre que celle prévue.
- Pour utiliser l’application de bureau ou l’extension IDE, les variables d’environnement requises sont
  présentes dans `~/.codex/.env`.

## Périmètre de l’assistance

L’assistance OpenAI peut vous aider pour la mise en place et la configuration des clients ChatGPT Work et Codex,
le fonctionnement local de la CLI, celui de l’application de bureau et de l’extension IDE,
ainsi que l’expérience produit locale.

Pour les identifiants AWS, les autorisations IAM, l’accès aux modèles Bedrock, les quotas, la facturation,
la disponibilité régionale, les échecs des requêtes Bedrock, les journaux des services AWS ou le fonctionnement du service Bedrock,
contactez l’administrateur AWS du client ou AWS Support.
