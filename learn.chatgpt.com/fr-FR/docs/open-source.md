<!-- source: https://learn.chatgpt.com/fr-FR/docs/open-source -->

OpenAI développe publiquement des composants clés de Codex. Ce travail est hébergé sur GitHub, où vous pouvez suivre son avancement, signaler des problèmes et apporter des améliorations.

Si vous maintenez un projet open source largement utilisé ou souhaitez recommander des mainteneurs qui supervisent des projets importants, vous pouvez également [postuler au programme Codex for OSS](/community/codex-for-oss) pour bénéficier de crédits API et de ChatGPT Pro avec Codex, ainsi que d’un accès à Codex Security accordé sur sélection.

## Composants open source

| Composant                     | Où le trouver                                                                                             | Remarques                                                   |
| ----------------------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| CLI Codex                     | [openai/codex](https://github.com/openai/codex)                                                           | Dépôt principal pour le développement open source de Codex      |
| SDK Codex                     | [openai/codex/codex-sdk](https://github.com/openai/codex/tree/main/sdk)                                   | Le code source du SDK se trouve dans le dépôt Codex                      |
| CLI Codex Security            | [openai/codex-security](https://github.com/openai/codex-security)                                         | CLI permettant de détecter et de valider des vulnérabilités de sécurité |
| SDK TypeScript de Codex Security | [openai/codex-security/sdk/typescript](https://github.com/openai/codex-security/tree/main/sdk/typescript) | SDK TypeScript pour lancer des analyses Codex Security         |
| App Server Codex              | [openai/codex/codex-rs/app-server](https://github.com/openai/codex/tree/main/codex-rs/app-server)         | Le code source de l’App Server se trouve dans le dépôt Codex               |
| Skills                        | [openai/skills](https://github.com/openai/skills)                                                         | Skills réutilisables pour étendre les capacités de ChatGPT et de Codex           |
| Plugins                       | [openai/plugins](https://github.com/openai/plugins)                                                       | Plugins réutilisables pour ChatGPT et Codex                  |
| Extension IDE                 | -                                                                                                         | Non open source                                         |
| Codex Cloud                   | -                                                                                                         | Non open source                                         |
| Environnement cloud universel   | [openai/codex-universal](https://github.com/openai/codex-universal)                                       | Environnement de base utilisé par Codex Cloud                    |

## Où signaler des problèmes et soumettre des demandes de fonctionnalités

Utilisez le dépôt GitHub approprié pour signaler des bugs et soumettre des demandes de fonctionnalités :

- Signalements de bugs et demandes de fonctionnalités pour Codex : [openai/codex/issues](https://github.com/openai/codex/issues)
- Signalements de bugs et demandes de fonctionnalités pour la CLI et le SDK TypeScript de Codex Security : [openai/codex-security/issues](https://github.com/openai/codex-security/issues)
- Forum de discussion : [openai/codex/discussions](https://github.com/openai/codex/discussions)

Lorsque vous ouvrez une issue, indiquez le composant utilisé (CLI, SDK, extension IDE, Codex Cloud ou Codex Security) ainsi que sa version, si possible.
