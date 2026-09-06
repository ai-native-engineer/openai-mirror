<!-- source: https://learn.chatgpt.com/de-DE/use-cases/ios-liquid-glass -->

## iOS 26 als Ausgangsbasis verwenden

Behandle Liquid Glass zunächst als Migrationsprojekt für iOS 26 und Xcode 26. Erstelle mit dem SDK von iOS 26 einen neuen Build der App, prüfe, welche Darstellung die Standard-Bedienelemente von SwiftUI automatisch liefern, und beauftrage Codex erst dann mit der Neugestaltung der benutzerdefinierten Teile, die noch zu flach oder zu wuchtig wirken oder sich zu stark von der Systemoberfläche abheben.

Falls die App weiterhin ältere iOS-Versionen unterstützt, nenne diese Einschränkung gleich zu Beginn ausdrücklich. Der Skill SwiftUI Liquid Glass im [Plug-in Build iOS Apps](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps) sollte neue APIs, die nur für Liquid Glass verfügbar sind, mit `#available(iOS 26, *)` absichern und einen Fallback-Pfad beibehalten, der auch auf älteren Geräten gut lesbar bleibt.

## Das iOS-Plug-in nutzen

Verwende das [Plug-in Build iOS Apps](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps), wenn Codex Änderungen an der SwiftUI-Benutzeroberfläche mit simulatorgestützter Validierung kombinieren soll. Bei Arbeiten an Liquid Glass solltest du Codex zunächst einen Ablauf prüfen, einige ausgewählte Oberflächen migrieren, das Ergebnis in einem Simulator mit iOS 26 starten und Screenshots erstellen lassen, bevor du den Umfang erweiterst.

Dieses Plug-in enthält einen Skill für Liquid Glass in SwiftUI. Dessen einfache Standardeinstellungen solltest du in deinen Prompt übernehmen:

- Bevorzuge die nativen APIs `glassEffect` und `GlassEffectContainer`, Schaltflächenstile für Liquid Glass und Übergänge mit `glassEffectID` gegenüber benutzerdefinierten Ansichten mit Weichzeichnereffekt.
- Wende `.glassEffect(...)` nach den Layout- und visuellen Modifiern an, damit das Material am Ende genau die gewünschte Form umschließt.
- Fasse zusammengehörige Glaselemente in `GlassEffectContainer` zusammen, wenn mehrere Oberflächen gleichzeitig angezeigt werden.
- Verwende `.interactive()` nur für Schaltflächen, Chips und Bedienelemente, die tatsächlich auf Berührungen reagieren.
- Halte Eckenformen, Farbtöne und Abstände durchgängig einheitlich, statt verschiedene Sonderlösungen für Glaseffekte zu mischen.
- Behalte für Bereitstellungsziele vor iOS 26 einen Fallback ohne Liquid Glass bei.

Weitere Informationen zum Installieren von Plug-ins und Skills findest du in unserer Dokumentation zu [Plug-ins](/de-DE/codex/plugins) und [Skills](/de-DE/codex/build-skills).

## Die WWDC-Sessions ansehen

Diese WWDC25-Sessions sind eine gute Referenz, bevor du Codex einen produktiv genutzten Ablauf refaktorieren lässt:

- [Liquid Glass kennenlernen](https://developer.apple.com/videos/play/wwdc2025/219/)
- [Das neue Designsystem kennenlernen](https://developer.apple.com/videos/play/wwdc2025/356/)
- [Eine SwiftUI-App mit dem neuen Design entwickeln](https://developer.apple.com/videos/play/wwdc2025/323/)
- [Eine UIKit-App mit dem neuen Design entwickeln](https://developer.apple.com/videos/play/wwdc2025/284/)
- [Neuerungen in SwiftUI](https://developer.apple.com/videos/play/wwdc2025/256/)

## Fordere erst einen Migrationsplan und dann eine Teilmigration an

Migrationen zu Liquid Glass gelingen besser, wenn Codex die Frage „Wo sollte Liquid Glass zum Einsatz kommen?“ von der Aufforderung „Schreibe jetzt den gesamten Code.“ trennt. Fordere zuerst eine kurze Prüfung an und lass den Agenten anschließend eine in sich geschlossene Teilmigration mit Validierung im Simulator umsetzen.

## Praktische Tipps

### Nicht alles mit Liquid Glass gestalten

Liquid Glass sollte eine klar erkennbare Bedienebene über den Inhalten schaffen und nicht jede Karte in eine leuchtende Fläche verwandeln. Bitte Codex, dekorative Hintergründe zu entfernen, die mit den Systemmaterialien konkurrieren, schlichte Inhaltsflächen dort beizubehalten, wo Lesbarkeit besonders wichtig ist, und Einfärbungen semantischen Hervorhebungen oder primären Aktionen vorzubehalten.

### Mit einem häufig genutzten Ablauf beginnen

Als erstes Migrationsziel eignet sich die Stammansicht eines Tabs, eine Detailansicht, ein Sheet, eine Suchoberfläche oder ein Onboarding-Ablauf meist besser als eine Überarbeitung der gesamten App. Das erleichtert die Überprüfung und verdeutlicht, welche Entscheidungen zu Liquid Glass in wiederverwendbare Komponentenmuster überführt werden sollten.

### Fallback-Verhalten gezielt überprüfen

Wenn dein Bereitstellungsziel unter iOS 26 liegt, bitte Codex, die Fallback-Implementierung neben der Version mit Liquid Glass zu zeigen. Dieser Prüfschritt deckt versehentliche Regressionen bei der API-Verfügbarkeit auf und verhindert, dass du eine Migration auslieferst, die nur im neuesten Simulator funktioniert.
