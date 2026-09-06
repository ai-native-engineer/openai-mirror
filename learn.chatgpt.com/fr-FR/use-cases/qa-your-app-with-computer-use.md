<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/qa-your-app-with-computer-use -->

## Introduction

La fonctionnalité Utilisation de l’ordinateur se prête particulièrement bien aux campagnes de QA, car elle peut observer l’interface, suivre différents parcours en cliquant, remplir des champs et consigner les dysfonctionnements. Elle permet ainsi de détecter aussi bien les bugs fonctionnels que les problèmes d’interface dans des scénarios d’utilisation réalistes.

L’essentiel est d’indiquer à Codex l’environnement à tester, les parcours les plus importants et le type de rapport que vous souhaitez obtenir.

## Comment l’utiliser

1. Installez le [plugin Utilisation de l’ordinateur](/fr-FR/codex/computer-use).
2. Indiquez à Codex l’application, le build ou l’environnement à tester.
3. Indiquez les parcours ou les cas d’utilisation clés qui comptent le plus pour vous.
4. Demandez un rapport structuré pour faciliter le triage ou la transmission des résultats.

Vous pouvez formuler une demande générale :

- `@Computer Test my app. Find any major issues and give me a report.`

Vous pouvez aussi préciser davantage votre demande :

- `@Computer Test my app in staging. Cover signup, invite a teammate, and upgrade billing. Log every bug with repro steps, expected result, actual result, and severity.`

Si vous conservez déjà un fichier de plan de test dans le dépôt, joignez-le à la discussion ou indiquez son emplacement à Codex afin que la campagne de QA suive vos parcours existants.

## Conseils pratiques

### Précisez la configuration

Si l’état du compte, les données de test, les feature flags ou le choix de l’environnement influent sur le parcours, précisez ces éléments d’emblée. Codex produira de bien meilleurs résultats s’il sait dans quel contexte le comportement doit être testé : en local, en préproduction ou dans des conditions proches de la production.

### Précisez les types de problèmes qui vous intéressent

Précisez si vous souhaitez que Codex se concentre sur les fonctionnalités défaillantes, les problèmes de mise en page, les textes prêtant à confusion, les régressions visuelles ou l’ensemble de ces éléments.

### Décidez s’il faut arrêter ou poursuivre le test

Si un seul problème bloquant doit interrompre le test, précisez-le. Sinon, demandez à Codex d’aller au bout du parcours et de recenser tous les problèmes non bloquants avant d’en faire la synthèse.

## Pour aller plus loin

Après la campagne de QA, gardez la même discussion ouverte et demandez à Codex de corriger l’un des bugs détectés, de transformer les constats en brouillons prêts à être utilisés dans Linear ou GitHub, ou de cibler la prochaine campagne sur un parcours défaillant précis.

## Prompt suggéré

**Menez une campagne de QA structurée**
