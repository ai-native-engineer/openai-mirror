<!-- source: https://learn.chatgpt.com/fr-FR/docs/agent-configuration/speed -->

<strong>L’utilisation est partagée entre ChatGPT Work et Codex.</strong> Les tarifs, les crédits et les limites d’utilisation sont les mêmes
  pour les deux. Consultez les [tarifs de Codex](/codex/pricing) pour
  plus de détails.

## mode Rapide

Codex permet d’augmenter la vitesse du modèle en contrepartie d’une consommation accrue de
crédits.

Pour GPT-5.6, GPT-5.5 et GPT-5.4, le mode Rapide multiplie la vitesse du modèle par 1,5.
Avec GPT-5.6 et GPT-5.5, la consommation de crédits est multipliée par 2,5 par rapport au mode Standard ; avec GPT-5.4,
elle est multipliée par 2.

Lorsqu’il est disponible, le mode Rapide de GPT-6 Astra multiplie la consommation de crédits par 2,5
par rapport au mode Standard. Consultez la page [Modèles](/fr-FR/codex/models) pour connaître la disponibilité des modèles et
la page [Tarifs](/fr-FR/codex/pricing#token-rates) pour connaître les tarifs des tokens.

Dans la CLI, utilisez `/fast on`, `/fast off` ou `/fast status` pour modifier ou consulter
le réglage actuel. Vous pouvez également enregistrer le réglage par défaut avec `service_tier =
"fast"` et `[features].fast_mode = true` dans `config.toml`. Le mode Rapide est
disponible dans l’application de bureau ChatGPT, Codex CLI et l’extension IDE lorsque vous
vous connectez avec ChatGPT. Le mode Rapide est une fonctionnalité liée aux crédits ChatGPT. Avec une clé API,
Codex applique à la place la tarification des tokens d’API, et les multiplicateurs de crédits ChatGPT ne
s’appliquent pas. Le traitement prioritaire de l’API a son propre tarif ; pour GPT-5.6, il coûte
2 fois le tarif Standard des tokens d’API.

## Codex-Spark

GPT-5.3-Codex-Spark est un modèle Codex distinct, rapide mais aux capacités plus limitées, optimisé pour
des itérations de code quasi instantanées, en temps réel. Contrairement au mode Rapide, qui accélère un
modèle pris en charge en contrepartie d’une consommation accrue de crédits, Codex-Spark est un modèle à part entière
et possède ses propres limites d’utilisation.

Pendant la phase de préversion de recherche, Codex-Spark est réservé aux abonnés ChatGPT Pro.
