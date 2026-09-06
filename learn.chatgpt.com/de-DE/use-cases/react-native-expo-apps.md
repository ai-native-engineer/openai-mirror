<!-- source: https://learn.chatgpt.com/de-DE/use-cases/react-native-expo-apps -->

## Mit Expo Go beginnen

Expo ist eine gute Standardwahl, wenn Codex aus einer Idee für eine mobile App eine
getestete App mit React Native entwickeln soll. Ein sinnvoller Ablauf sieht so aus: Beginne mit `expo start` und verwende danach Expo Go
auf einem Gerät. Wechsle erst dann zu einem Dev-Client oder EAS-Build, wenn die App
benutzerdefinierten nativen Code, die Veröffentlichung in einem Store oder eine Funktion benötigt, die Expo Go nicht ausführen kann.

So kann sich Codex auf den Arbeitsablauf der App konzentrieren, statt beim ersten Durchlauf
die native IDE und den Simulator einzurichten oder sich mit der Provisionierung und der Build-Konfiguration zu befassen.

## Expo-Plug-in verwenden

Expo hat ein [Expo-Plug-in](https://docs.expo.dev/skills/) veröffentlicht. Es bietet Codex Expo-spezifische Anleitungen zu Expo Router, nativen Benutzeroberflächen, Formularen,
Navigation, Animationen, Datenabrufen, dem NativeWind-Setup, Expo-Modulen,
Dev-Clients, Bereitstellung, Upgrades und der Einbindung der Codex Run-Aktion.

Verwende es, wenn Codex neue Expo-Ansichten erstellt, Pakete hinzufügt, API-Aufrufe einbindet,
einen Dev-Client vorbereitet oder eine App für TestFlight, den App Store,
den Play Store oder EAS Hosting bereit macht.

Füge optional den [Expo MCP-Server](https://docs.expo.dev/eas/ai/mcp/) hinzu, wenn die Aufgabe Folgendes erfordert: das Nachschlagen in der aktuellen
Expo-Dokumentation, die Installation kompatibler Pakete, Vorgänge für EAS-Builds und
Arbeitsabläufe, Screenshots, die Interaktion mit dem Simulator, React Native DevTools
oder TestFlight-Daten.

## Iterationsprozess

1. Lass Codex das Repository prüfen und feststellen, ob es eine neue Expo-App oder ein
bestehendes Expo-Projekt ist.
2. Beginne mit Expo Router und Expo Go und verwende `npx expo install`, wenn du
   Expo-Pakete hinzufügst.
3. Lass Codex einen vollständigen Arbeitsablauf mit nativ wirkender Navigation,
Ladezuständen, Leerzuständen und Fehlerzuständen umsetzen.
4. Nutze zur Überprüfung die schnellste verfügbare Option, etwa Expo Go auf einem Gerät oder in einem
Simulator, und wechsle nur bei Bedarf zu einem Dev-Client oder EAS.

## Vorschlag für einen Folge-Prompt
