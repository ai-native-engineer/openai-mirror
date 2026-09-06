<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/react-native-expo-apps -->

## Commencez par Expo Go

Expo est un excellent choix par défaut lorsque vous souhaitez que Codex transforme une idée d’application mobile en une
application React Native testée. Le cycle à suivre consiste à commencer par `expo start`, puis à utiliser Expo Go
sur un appareil et, enfin, à passer à un client de développement ou à un build EAS uniquement s’il faut
du code natif personnalisé, distribuer l’application via une boutique d’applications ou utiliser une fonctionnalité qu’Expo Go ne peut pas exécuter.

Cela permet à Codex de se concentrer sur le flux de travail de l’application au lieu de consacrer la première itération
à la configuration des IDE natifs et des simulateurs, au provisionnement ou à la configuration du build.

## Utilisez le plugin Expo

Expo a publié un [plugin Expo](https://docs.expo.dev/skills/) qui fournit à Codex des recommandations propres à Expo pour Expo Router, les interfaces au rendu natif, les formulaires,
la navigation, les animations, la récupération de données, la configuration de NativeWind, les modules Expo, les clients
de développement, le déploiement, les mises à niveau et l’intégration de l’action Codex Run.

Utilisez-le lorsque Codex crée de nouveaux écrans Expo, ajoute des packages, intègre des appels
d’API, prépare un client de développement ou prépare une application pour TestFlight, l’App
Store, le Play Store ou EAS Hosting.

Ajoutez, si besoin, le [Serveur MCP Expo](https://docs.expo.dev/eas/ai/mcp/) lorsque la tâche nécessite de consulter la
documentation Expo à jour, d’installer des packages compatibles, d’effectuer des opérations sur les builds et les
flux de travail EAS, de prendre des captures d’écran, d’interagir avec le simulateur, d’utiliser React Native DevTools
ou d’accéder aux données de TestFlight.

## Processus d’itération

1. Demandez à Codex d’inspecter le dépôt et de confirmer s’il s’agit d’une nouvelle application Expo ou d’un
projet Expo existant.
2. Commencez par Expo Router et Expo Go, et utilisez `npx expo install` lorsque vous ajoutez des
   packages Expo.
3. Demandez à Codex de créer un flux de travail complet avec une navigation au rendu natif,
des états de chargement, des états vides et des états d’erreur.
4. Procédez à la vérification par le moyen le plus rapide disponible, par exemple avec Expo Go sur un appareil ou un
simulateur, puis ne passez à un client de développement ou à EAS que si nécessaire.

## Suggestion de prompt de suivi
